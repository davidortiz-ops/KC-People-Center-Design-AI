#!/usr/bin/env python3
"""
Parsea HTML y extrae elementos relevantes para SEO.

Uso:
    python parse_html.py page.html
    python parse_html.py --url https://example.com
"""

import argparse
import json
import os
import re
import sys
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: se requiere beautifulsoup4. Instálalo con: pip install beautifulsoup4")
    sys.exit(1)

try:
    import lxml  # noqa: F401
    _HTML_PARSER = "lxml"
except ImportError:
    _HTML_PARSER = "html.parser"


def parse_html(html: str, base_url: Optional[str] = None) -> dict:
    """
    Parsea HTML y extrae elementos relevantes para SEO.

    Args:
        html: Contenido HTML a parsear
        base_url: URL base para resolver enlaces relativos

    Returns:
        Diccionario con los datos SEO extraídos
    """
    soup = BeautifulSoup(html, _HTML_PARSER)

    result = {
        "title": None,
        "meta_description": None,
        "meta_robots": None,
        "canonical": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "images": [],
        "links": {
            "internal": [],
            "external": [],
        },
        "schema": [],
        "open_graph": {},
        "twitter_card": {},
        "word_count": 0,
        "hreflang": [],
    }

    # Title
    title_tag = soup.find("title")
    if title_tag:
        result["title"] = title_tag.get_text(strip=True)

    # Meta tags
    for meta in soup.find_all("meta"):
        name = meta.get("name", "").lower()
        property_attr = meta.get("property", "").lower()
        content = meta.get("content", "")

        if name == "description":
            result["meta_description"] = content
        elif name == "robots":
            result["meta_robots"] = content

        # Open Graph
        if property_attr.startswith("og:"):
            result["open_graph"][property_attr] = content

        # Twitter Card
        if name.startswith("twitter:"):
            result["twitter_card"][name] = content

    # Canonical
    canonical = soup.find("link", rel="canonical")
    if canonical:
        result["canonical"] = canonical.get("href")

    # Hreflang
    for link in soup.find_all("link", rel="alternate"):
        hreflang = link.get("hreflang")
        if hreflang:
            result["hreflang"].append({
                "lang": hreflang,
                "href": link.get("href"),
            })

    # Encabezados
    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                result[tag].append(text)

    # Imágenes
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if base_url and src:
            src = urljoin(base_url, src)

        result["images"].append({
            "src": src,
            "alt": img.get("alt"),
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading"),
        })

    # Enlaces
    if base_url:
        base_domain = urlparse(base_url).netloc

        for a in soup.find_all("a", href=True):
            href = a.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue

            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)

            link_data = {
                "href": full_url,
                "text": a.get_text(strip=True)[:100],
                "rel": a.get("rel", []),
            }

            if parsed.netloc == base_domain:
                result["links"]["internal"].append(link_data)
            else:
                result["links"]["external"].append(link_data)

    # Schema (JSON-LD)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            schema_data = json.loads(script.string)
            result["schema"].append(schema_data)
        except (json.JSONDecodeError, TypeError):
            pass

    # Conteo de palabras (solo texto visible)
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r"\b\w+\b", text)
    result["word_count"] = len(words)

    return result


def main():
    parser = argparse.ArgumentParser(description="Parsea HTML para análisis SEO")
    parser.add_argument("file", nargs="?", help="Archivo HTML a parsear")
    parser.add_argument("--url", "-u", help="URL base para resolver enlaces")
    parser.add_argument("--json", "-j", action="store_true", help="Salida en formato JSON")

    args = parser.parse_args()

    if args.file:
        real_path = os.path.realpath(args.file)
        if not os.path.isfile(real_path):
            print(f"Error: Archivo no encontrado: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(real_path, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    result = parse_html(html, args.url)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Título: {result['title']}")
        print(f"Meta Description: {result['meta_description']}")
        print(f"Canonical: {result['canonical']}")
        print(f"Etiquetas H1: {len(result['h1'])}")
        print(f"Etiquetas H2: {len(result['h2'])}")
        print(f"Imágenes: {len(result['images'])}")
        print(f"Enlaces internos: {len(result['links']['internal'])}")
        print(f"Enlaces externos: {len(result['links']['external'])}")
        print(f"Bloques de Schema: {len(result['schema'])}")
        print(f"Conteo de palabras: {result['word_count']}")


if __name__ == "__main__":
    main()
