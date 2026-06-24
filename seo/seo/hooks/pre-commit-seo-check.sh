#!/usr/bin/env bash
set -euo pipefail

# Hook de validación SEO pre-commit para Claude Code.
#
# Configuración del hook en ~/.claude/settings.json:
# {
#   "hooks": {
#     "PreToolUse": [
#       {
#         "matcher": "Bash",
#         "hooks": [
#           {
#             "type": "command",
#             "command": "~/.claude/skills/seo/hooks/pre-commit-seo-check.sh"
#           }
#         ]
#       }
#     ]
#   }
# }
#
# NOTA: El matcher es "Bash" (solo nombre de herramienta). Este script se ejecuta en
# TODOS los usos de la herramienta Bash. Verifica si hay archivos en stage antes de
# continuar. Si no hay cambios en stage, sale con 0 de inmediato.

ERRORS=0
WARNINGS=0

# Verificar si hay cambios en stage — salir temprano si no los hay
if ! git diff --cached --quiet 2>/dev/null; then
    : # Hay cambios en stage, continuar con las verificaciones
else
    exit 0  # Sin cambios en stage, nada que verificar
fi

echo "🔍 Ejecutando verificaciones SEO pre-commit..."

# Verificar archivos de tipo HTML en stage
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null | grep -E '\.(html|htm|php|jsx|tsx|vue|svelte)$' || true)

if [ -z "${STAGED_FILES}" ]; then
    echo "✓ No hay archivos HTML en stage — se omiten las verificaciones SEO"
    exit 0
fi

for file in ${STAGED_FILES}; do
    if [ ! -f "${file}" ]; then
        continue
    fi

    # Verificar texto de marcador de posición (placeholder) en el schema, inglés y español
    if grep -qiE '\[(Business Name|City|State|Phone|Address|Your|INSERT|REPLACE|Nombre del Negocio|Nombre de la Empresa|Ciudad|Región|Estado|Teléfono|Dirección|Tu|INSERTAR|REEMPLAZAR|Correo)\]' "${file}" 2>/dev/null; then
        echo "🛑 ${file}: Contiene texto de marcador de posición en el marcado de schema"
        ERRORS=$((ERRORS + 1))
    fi

    # Verificar la longitud del title tag
    TITLE=$(grep -oP '(?<=<title>).*?(?=</title>)' "${file}" 2>/dev/null | head -1 || true)
    if [ -n "${TITLE}" ]; then
        TITLE_LEN=${#TITLE}
        if [ "${TITLE_LEN}" -lt 30 ] || [ "${TITLE_LEN}" -gt 60 ]; then
            echo "⚠️  ${file}: Longitud del title tag ${TITLE_LEN} caracteres (recomendado 30-60)"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi

    # Verificar imágenes sin alt text
    if grep -qP '<img(?![^>]*alt=)' "${file}" 2>/dev/null; then
        echo "⚠️  ${file}: Se encontraron imágenes sin alt text"
        WARNINGS=$((WARNINGS + 1))
    fi

    # Verificar tipos de schema obsoletos
    if grep -qE '"@type"\s*:\s*"(HowTo|SpecialAnnouncement)"' "${file}" 2>/dev/null; then
        echo "🛑 ${file}: Contiene un tipo de schema obsoleto"
        ERRORS=$((ERRORS + 1))
    fi

    # Verificar referencias a FID (debería ser INP)
    if grep -qi 'First Input Delay\|"FID"' "${file}" 2>/dev/null; then
        echo "⚠️  ${file}: Hace referencia a FID — debería usar INP (Interaction to Next Paint)"
        WARNINGS=$((WARNINGS + 1))
    fi

    # Verificar la longitud de la meta description
    META_DESC=$(grep -oP '(?<=<meta name="description" content=").*?(?=")' "${file}" 2>/dev/null | head -1 || true)
    if [ -n "${META_DESC}" ]; then
        META_LEN=${#META_DESC}
        if [ "${META_LEN}" -lt 120 ] || [ "${META_LEN}" -gt 160 ]; then
            echo "⚠️  ${file}: Longitud de la meta description ${META_LEN} caracteres (recomendado 120-160)"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done

echo ""
if [ "${ERRORS}" -gt 0 ]; then
    echo "🛑 ${ERRORS} error(es) crítico(s) encontrado(s) — commit bloqueado"
    echo "Corrige los errores anteriores e inténtalo de nuevo."
    exit 2
elif [ "${WARNINGS}" -gt 0 ]; then
    echo "⚠️  ${WARNINGS} advertencia(s) encontrada(s) — commit permitido"
    exit 0
else
    echo "✓ Todas las verificaciones SEO pasaron"
    exit 0
fi
