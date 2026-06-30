# Skill: Accesibilidad Digital WCAG 2.2 — Banca y Retail

Skill de auditoría de accesibilidad digital WCAG 2.2 (niveles A, AA, AAA)
para **banca** y **retail** en el contexto normativo colombiano.

Versión 2.1 · Pragma. Soporta dos modos de ejecución: **CLI** (Claude Code
con terminal) e **ID** (Claude Desktop / .ai, sin terminal). Es la evolución
del prompt `auditor-accesibilidad-digital-wcag.md` (v1.0), que se conserva
sin cambios.

## Estructura

```
accesibilidad-wcag/
├── SKILL.md                         # Núcleo: orquesta la auditoría de 6 fases
├── evals/
│   └── evals.json                   # Casos de prueba (4)
├── references/
│   ├── checklist-wcag-22.md         # 87 criterios con ejemplos banca/retail
│   ├── calculo-contraste-manual.md  # Fórmula de contraste sin Python (solo ID)
│   ├── normativa-colombiana.md      # Mapeo WCAG ↔ leyes/circulares CO
│   ├── metodologia-evaluacion.md    # Paso a paso y técnicas POUR
│   ├── protocolo-lectores-pantalla.md  # NVDA, JAWS, VoiceOver, TalkBack
│   ├── priorizacion-remediacion.md  # Matriz severidad × esfuerzo × riesgo
│   ├── patrones-remediacion-aria.md # Código: modal, tabs, acordeón, alertas, menú
│   ├── patrones-formularios.md      # Código: labels, errores, validación, auth
│   ├── patrones-navegacion.md       # Código: skip link, landmarks, breadcrumb
│   ├── presentacion-datos.md        # Código: tablas, gráficos, cifras
│   ├── estados-aplicacion.md        # Código: carga, vacío, error, sesión
│   ├── responsive-y-objetivos.md    # Código: reflujo, zoom, tamaño de objetivos
│   ├── seguridad-accesible.md       # Código: auth, CSRF, XSS, CSP, timeouts
│   └── verticales/
│       ├── banca.md                 # Flujos e issues de banca
│       └── retail.md                # Flujos e issues de retail
├── templates/
│   ├── reporte-auditoria.html       # Reporte técnico (print-friendly)
│   ├── reporte-ejecutivo.md         # Resumen para stakeholders
│   └── declaracion-conformidad.md   # Conformance claim
└── scripts/
    ├── run_pa11y_audit.sh           # Auditoría automática con pa11y (A/AA/AAA)
    ├── check_contrast.py            # Validador de contraste de color
    └── validate_semantic_html.py    # Validador de estructura semántica
```

> Las referencias se dividen en dos grupos: **evaluación** (cómo auditar:
> checklist, normativa, metodología, protocolos, priorización, verticales)
> y **remediación** (cómo corregir, con código: patrones ARIA, formularios,
> navegación, datos, estados, responsive, seguridad).

## Uso del skill

El agente AI debe leer `SKILL.md` y seguir el workflow de 6 fases:
alcance → automática → manual → priorización → reporte → remediación.
Los archivos de `references/` son material de consulta detallado.

## Modos de ejecución

El skill se adapta al entorno donde se ejecute:

| Característica | Modo CLI (Claude Code) | Modo ID (Desktop / .ai) |
|---|---|---|
| Terminal disponible | ✅ Sí | ❌ No |
| Scripts Python/Bash | ✅ Se ejecutan | ❌ No disponibles |
| Cálculo de contraste | `check_contrast.py` | Fórmula manual (`calculo-contraste-manual.md`) |
| Validación semántica | `validate_semantic_html.py` | Inspección directa del DOM |
| Subagentes paralelos | ✅ Sí | ⚠️ Según plataforma |
| Guardado de archivos | ✅ En disco | ❌ Entrega inline en conversación |
| Reporte técnico | Archivo .html | HTML renderizado inline |

Detección automática al iniciar (§0.1 del SKILL.md).

## Scripts

### Python (3.8+, sin dependencias externas)

```bash
# Contraste de color (--json para CI, exit 1 si no cumple AA)
python scripts/check_contrast.py --fg "#333333" --bg "#FFFFFF"
python scripts/check_contrast.py --tokens tokens.css --report contraste.html
python scripts/check_contrast.py --fg "#999" --bg "#fff" --json

# Estructura semántica HTML
python scripts/validate_semantic_html.py --url https://ejemplo.com
python scripts/validate_semantic_html.py --file index.html --report sem.html
```

> En consolas de Windows, los scripts Python reconfiguran la salida a UTF-8
> automáticamente para mostrar el semáforo (✅ ⚠️ ❌).

### Auditoría automática con pa11y (requiere Node.js 18+)

```bash
# Ejecutar desde Git Bash en Windows. La primera vez descarga Chromium.
bash scripts/run_pa11y_audit.sh --standard WCAG2AAA https://ejemplo.com
bash scripts/run_pa11y_audit.sh --urls urls.txt --report reporte.json
```

> pa11y (motor HTML_CodeSniffer) detecta ~30-40% de los issues; complementa
> siempre con revisión manual (teclado + lector de pantalla).

## Sin instalación ni configuración obligatoria

El skill produce un informe **completo sin instalar nada**: el modelo
recupera el HTML y lo evalúa contra el checklist y las guías. Los scripts
son **opcionales** y solo aplican en **Modo CLI**:

- Python (`check_contrast.py`, `validate_semantic_html.py`): solo si ya
  tienes Python; usan únicamente la biblioteca estándar.
- `run_pa11y_audit.sh`: solo si ya tienes Node.js; si no, se omite y el
  informe lo indica. **No hace falta instalarlo.**

En **Modo ID** (sin terminal): el skill sigue siendo autocontenido. El
contraste se calcula con la fórmula WCAG (`calculo-contraste-manual.md`)
y la validación semántica se hace inspeccionando el HTML directamente.

## Alcance y limitaciones

- Solo accesibilidad **web** (no mobile nativo iOS/Android).
- Las herramientas automáticas cubren ~30-40% de los criterios y **no**
  sustituyen la revisión manual con teclado y lectores de pantalla.
- La normativa colombiana citada debe verificarse en su versión vigente
  (ver `references/normativa-colombiana.md`).

## Licencia

Propiedad de Pragma. Uso interno y confidencial — ver `LICENSE`.
