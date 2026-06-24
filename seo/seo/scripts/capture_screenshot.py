#!/usr/bin/env python3
"""
Captura screenshots de páginas web usando Playwright.

Uso:
    python capture_screenshot.py https://example.com
    python capture_screenshot.py https://example.com --mobile
    python capture_screenshot.py https://example.com --output screenshots/
"""

import argparse
import ipaddress
import os
import socket
import sys
from urllib.parse import ParseResult, urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("Error: se requiere playwright. Instálalo con: pip install playwright && playwright install chromium")
    sys.exit(1)


VIEWPORTS = {
    "desktop": {"width": 1920, "height": 1080},
    "laptop": {"width": 1366, "height": 768},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 812},
}


def normalize_url(url: str) -> tuple[str, ParseResult]:
    """Normaliza la URL y devuelve (url, parsed_url)."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Esquema de URL inválido: {parsed.scheme}")
    if not parsed.hostname:
        raise ValueError("URL inválida: falta el hostname")

    return url, parsed


def capture_screenshot(
    url: str,
    output_path: str,
    viewport: str = "desktop",
    full_page: bool = False,
    timeout: int = 30000,
) -> dict:
    """
    Captura un screenshot de una página web.

    Args:
        url: URL a capturar
        output_path: Ruta del archivo de salida
        viewport: Preset de viewport (desktop, laptop, tablet, mobile)
        full_page: Si se captura la página completa o solo el viewport
        timeout: Tiempo de espera de carga de la página en milisegundos

    Returns:
        Diccionario con los resultados de la captura
    """
    result = {
        "url": url,
        "output": output_path,
        "viewport": viewport,
        "success": False,
        "error": None,
    }

    if viewport not in VIEWPORTS:
        result["error"] = f"Viewport inválido: {viewport}. Elige entre: {list(VIEWPORTS.keys())}"
        return result

    try:
        url, parsed = normalize_url(url)
        result["url"] = url
    except ValueError as e:
        result["error"] = str(e)
        return result

    # Prevención de SSRF: bloquear IPs privadas/internas
    try:
        resolved_ip = socket.gethostbyname(parsed.hostname)
        ip = ipaddress.ip_address(resolved_ip)
        if ip.is_private or ip.is_loopback or ip.is_reserved:
            result["error"] = f"Bloqueado: la URL resuelve a una IP privada/interna ({resolved_ip})"
            return result
    except socket.gaierror:
        pass

    vp = VIEWPORTS[viewport]

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": vp["width"], "height": vp["height"]},
                device_scale_factor=2 if viewport == "mobile" else 1,
            )
            page = context.new_page()

            # Navegar y esperar a que la red esté inactiva
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # Esperar un poco más por contenido cargado de forma diferida (lazy)
            page.wait_for_timeout(1000)

            # Capturar el screenshot
            page.screenshot(path=output_path, full_page=full_page)

            result["success"] = True
            browser.close()

    except PlaywrightTimeout:
        result["error"] = f"La carga de la página expiró tras {timeout}ms"
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="Captura screenshots de páginas web")
    parser.add_argument("url", help="URL a capturar")
    parser.add_argument("--output", "-o", default="screenshots", help="Directorio de salida")
    parser.add_argument("--viewport", "-v", default="desktop", choices=VIEWPORTS.keys())
    parser.add_argument("--all", "-a", action="store_true", help="Capturar todos los viewports")
    parser.add_argument("--full", "-f", action="store_true", help="Capturar la página completa")
    parser.add_argument("--timeout", "-t", type=int, default=30000, help="Tiempo de espera en ms")

    args = parser.parse_args()

    # Sanear la ruta de salida — prevenir directory traversal
    output_dir = os.path.realpath(args.output)
    cwd = os.getcwd()
    home = os.path.expanduser("~")
    if not (output_dir.startswith(cwd) or output_dir.startswith(home)):
        print("Error: La ruta de salida debe estar dentro del directorio actual o del directorio home", file=sys.stderr)
        sys.exit(1)

    # Crear el directorio de salida
    os.makedirs(args.output, exist_ok=True)

    try:
        normalized_url, parsed_url = normalize_url(args.url)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Generar nombre de archivo a partir de la URL
    base_name = parsed_url.netloc.replace(".", "_")

    viewports = VIEWPORTS.keys() if args.all else [args.viewport]

    for viewport in viewports:
        filename = f"{base_name}_{viewport}.png"
        output_path = os.path.join(args.output, filename)

        print(f"Capturando screenshot {viewport}...")
        result = capture_screenshot(
            normalized_url,
            output_path,
            viewport=viewport,
            full_page=args.full,
            timeout=args.timeout,
        )

        if result["success"]:
            print(f"  ✓ Guardado en {output_path}")
        else:
            print(f"  ✗ Falló: {result['error']}")


if __name__ == "__main__":
    main()
