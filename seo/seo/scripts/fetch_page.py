#!/usr/bin/env python3
"""
Obtiene una página web con cabeceras adecuadas y manejo de errores.

Uso:
    python fetch_page.py https://example.com
    python fetch_page.py https://example.com --output page.html
"""

import argparse
import ipaddress
import socket
import sys
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Error: se requiere la librería requests. Instálala con: pip install requests")
    sys.exit(1)


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 ClaudeSEO/1.2"
)

# UA de Googlebot para detectar prerender/renderizado dinámico.
# Los servicios de prerender (Prerender.io, Rendertron) sirven HTML totalmente
# renderizado a Googlebot pero shells de JS crudos a otros UAs. Comparar el tamaño
# de las respuestas entre DEFAULT_USER_AGENT y GOOGLEBOT_USER_AGENT revela si un
# sitio usa renderizado dinámico — una señal clave para detectar SPAs.
GOOGLEBOT_USER_AGENT = (
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
)

DEFAULT_HEADERS = {
    "User-Agent": DEFAULT_USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}


def fetch_page(
    url: str,
    timeout: int = 30,
    follow_redirects: bool = True,
    max_redirects: int = 5,
    user_agent: Optional[str] = None,
) -> dict:
    """
    Obtiene una página web y devuelve los detalles de la respuesta.

    Args:
        url: La URL a obtener
        timeout: Tiempo de espera de la solicitud en segundos
        follow_redirects: Si se deben seguir las redirecciones
        max_redirects: Número máximo de redirecciones a seguir

    Returns:
        Diccionario con:
            - url: URL final tras las redirecciones
            - status_code: Código de estado HTTP
            - content: Cuerpo de la respuesta
            - headers: Cabeceras de la respuesta
            - redirect_chain: Lista de URLs de redirección
            - error: Mensaje de error si falló
    """
    result = {
        "url": url,
        "status_code": None,
        "content": None,
        "headers": {},
        "redirect_chain": [],
        "error": None,
    }

    # Validar URL
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        result["error"] = f"Esquema de URL inválido: {parsed.scheme}"
        return result

    # Prevención de SSRF: bloquear IPs privadas/internas
    try:
        resolved_ip = socket.gethostbyname(parsed.hostname)
        ip = ipaddress.ip_address(resolved_ip)
        if ip.is_private or ip.is_loopback or ip.is_reserved:
            result["error"] = f"Bloqueado: la URL resuelve a una IP privada/interna ({resolved_ip})"
            return result
    except (socket.gaierror, ValueError):
        pass  # El fallo de resolución DNS lo maneja requests más abajo

    try:
        session = requests.Session()
        session.max_redirects = max_redirects

        headers = dict(DEFAULT_HEADERS)
        if user_agent:
            headers["User-Agent"] = user_agent

        response = session.get(
            url,
            headers=headers,
            timeout=timeout,
            allow_redirects=follow_redirects,
        )

        result["url"] = response.url
        result["status_code"] = response.status_code
        result["content"] = response.text
        result["headers"] = dict(response.headers)

        # Registrar la cadena de redirecciones
        if response.history:
            result["redirect_chain"] = [r.url for r in response.history]

    except requests.exceptions.Timeout:
        result["error"] = f"La solicitud expiró tras {timeout} segundos"
    except requests.exceptions.TooManyRedirects:
        result["error"] = f"Demasiadas redirecciones (máx {max_redirects})"
    except requests.exceptions.SSLError as e:
        result["error"] = f"Error SSL: {e}"
    except requests.exceptions.ConnectionError as e:
        result["error"] = f"Error de conexión: {e}"
    except requests.exceptions.RequestException as e:
        result["error"] = f"La solicitud falló: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(description="Obtiene una página web para análisis SEO")
    parser.add_argument("url", help="URL a obtener")
    parser.add_argument("--output", "-o", help="Ruta del archivo de salida")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="Tiempo de espera en segundos")
    parser.add_argument("--no-redirects", action="store_true", help="No seguir redirecciones")
    parser.add_argument("--user-agent", help="Cadena de User-Agent personalizada")
    parser.add_argument(
        "--googlebot",
        action="store_true",
        help=(
            "Usar el UA de Googlebot para detectar renderizado dinámico / servicios de prerender. "
            "Compara el tamaño de la respuesta con el UA por defecto para identificar la configuración de prerender de SPAs."
        ),
    )

    args = parser.parse_args()

    ua = args.user_agent
    if args.googlebot:
        ua = GOOGLEBOT_USER_AGENT

    result = fetch_page(
        args.url,
        timeout=args.timeout,
        follow_redirects=not args.no_redirects,
        user_agent=ua,
    )

    if result["error"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result["content"])
        print(f"Guardado en {args.output}")
    else:
        print(result["content"])

    # Imprimir metadatos en stderr
    print(f"\nURL: {result['url']}", file=sys.stderr)
    print(f"Estado: {result['status_code']}", file=sys.stderr)
    if result["redirect_chain"]:
        print(f"Redirecciones: {' -> '.join(result['redirect_chain'])}", file=sys.stderr)


if __name__ == "__main__":
    main()
