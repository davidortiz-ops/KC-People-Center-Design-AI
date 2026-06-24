#!/usr/bin/env python3
"""Hook de validación de schema tras edición para Claude Code.

Valida el schema JSON-LD después de editar archivos. Devuelve el código de salida 2
para bloquear si se encuentran errores de validación críticos.

Configuración del hook en ~/.claude/settings.json:
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/seo/hooks/validate-schema.py \"$FILE_PATH\"",
            "exitCodes": { "2": "block" }
          }
        ]
      }
    ]
  }
}

Nota: el matcher filtra solo por nombre de herramienta (Edit, Write). El propio script
verifica si el archivo contiene marcado de schema antes de validar.
"""

import json
import re
import sys
import os
from typing import List


def validate_jsonld(content: str) -> List[str]:
    """Valida los bloques JSON-LD dentro del contenido HTML."""
    errors = []
    pattern = r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>'
    blocks = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)

    if not blocks:
        return []  # No se encontró schema — no es un error

    for i, block in enumerate(blocks, 1):
        block = block.strip()
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"Bloque {i}: JSON inválido — {e}")
            continue

        if isinstance(data, list):
            for item in data:
                errors.extend(_validate_schema_object(item, i))
        elif isinstance(data, dict):
            errors.extend(_validate_schema_object(data, i))

    return errors


def _validate_schema_object(obj: dict, block_num: int) -> List[str]:
    """Valida un único objeto de schema."""
    errors = []
    prefix = f"Bloque {block_num}"

    # Verificar @context
    if "@context" not in obj:
        errors.append(f"{prefix}: Falta @context")
    elif obj["@context"] not in ("https://schema.org", "http://schema.org"):
        errors.append(f"{prefix}: @context debería ser 'https://schema.org'")

    # Verificar @type
    if "@type" not in obj:
        errors.append(f"{prefix}: Falta @type")

    # Verificar texto de marcador de posición (placeholder), en inglés y español
    placeholders = [
        "[Business Name]",
        "[City]",
        "[State]",
        "[Phone]",
        "[Address]",
        "[Your",
        "[INSERT",
        "REPLACE",
        "[URL]",
        "[Email]",
        "[Nombre del Negocio]",
        "[Nombre de la Empresa]",
        "[Ciudad]",
        "[Región]",
        "[Estado]",
        "[Teléfono]",
        "[Dirección]",
        "[Tu",
        "[INSERTAR",
        "REEMPLAZAR",
        "[Correo]",
        "[Email]",
    ]
    text = json.dumps(obj)
    for p in placeholders:
        if p.lower() in text.lower():
            errors.append(f"{prefix}: Contiene texto de marcador de posición: {p}")

    # Verificar tipos obsoletos
    schema_type = obj.get("@type", "")
    deprecated = {
        "HowTo": "obsoleto desde septiembre 2023",
        "SpecialAnnouncement": "obsoleto desde el 31 de julio de 2025",
        "CourseInfo": "retirado en junio 2025",
        "EstimatedSalary": "retirado en junio 2025",
        "LearningVideo": "retirado en junio 2025",
        "ClaimReview": "retirado en junio 2025 — rich results de fact-check descontinuados",
        "VehicleListing": "retirado en junio 2025 — datos estructurados de listados de vehículos descontinuados",
    }
    if schema_type in deprecated:
        errors.append(f"{prefix}: el @type '{schema_type}' está {deprecated[schema_type]}")

    # Verificar tipos restringidos usados incorrectamente
    restricted = {"FAQPage": "restringido solo a sitios de gobierno y salud (ago 2023)"}
    if schema_type in restricted:
        errors.append(f"{prefix}: el @type '{schema_type}' está {restricted[schema_type]} — verifica que el sitio califique")

    return errors


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        sys.exit(0)

    # Validar solo archivos de tipo HTML
    valid_extensions = (".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".php", ".ejs")
    if not filepath.endswith(valid_extensions):
        sys.exit(0)

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except (OSError, IOError):
        sys.exit(0)

    errors = validate_jsonld(content)

    if not errors:
        sys.exit(0)

    # Categorizar errores
    critical_keywords = ["marcador de posición", "obsoleto", "retirado"]
    critical = [e for e in errors if any(kw in e.lower() for kw in critical_keywords)]
    warnings = [e for e in errors if e not in critical]

    if warnings:
        print("⚠️  Advertencias de validación de schema:")
        for w in warnings:
            print(f"  - {w}")

    if critical:
        print("🛑 ERRORES de validación de schema (bloqueantes):")
        for e in critical:
            print(f"  - {e}")
        sys.exit(2)  # Bloquear la edición

    sys.exit(1)  # Solo advertencias — continuar


if __name__ == "__main__":
    main()
