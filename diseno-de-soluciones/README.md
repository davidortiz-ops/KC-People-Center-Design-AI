# Diseño de Soluciones

> Chapter de **People Center Design - Pragma**.

Artefactos para la fase de **diseño de soluciones**: evaluación de usabilidad,
accesibilidad, experiencia conductual y madurez de design systems. Incluye skills
estructurados (con carpeta, scripts y evals) y skills planos (archivo único).

---

## Qué tiene

**6 artefactos** organizados en tres categorías:

### Skills de usabilidad y accesibilidad

| Artefacto | Tipo | Versión | ¿Qué problema resuelve? |
|-----------|------|---------|-------------------------|
| **Heuristy — Evaluación Heurística Nielsen** | Skill estructurado | 2.0 | Identifica problemas de usabilidad en interfaces digitales usando las 10 heurísticas de Nielsen + 4 extensiones para banca/retail. Genera score global, matriz de priorización y roadmap. |
| **Accesibilidad Digital WCAG 2.2** | Skill estructurado | 2.0 | Audita sitios web contra los 87 criterios WCAG 2.2 (A, AA, AAA). Detecta barreras de acceso, calcula contraste, verifica lectores de pantalla. Adaptado a normativa colombiana. |
| **Tognazzini — Créditos de Vivienda** | Skill plano | 1.0 | Evalúa la experiencia de usuario en solicitudes de crédito de vivienda aplicando las 16 heurísticas de Bruce Tognazzini. Enfocado en flujos completos, no solo interfaz. |

### Skills de evaluación conductual y organizacional

| Artefacto | Tipo | Versión | ¿Qué problema resuelve? |
|-----------|------|---------|-------------------------|
| **Proto-Persona Banca Top Tier** | Skill estructurado | 1.0 | Evalúa experiencias digitales bancarias desde la perspectiva del cliente de altos ingresos. Calcula TTES, genera behavioral insights, se integra con otros skills. |
| **Consultor de Madurez de Design Systems** | Skill plano | 1.0 | Diagnostica el nivel de madurez de un Design System (5 niveles: Located → Opened) y su modelo de gestión/operación (4 pilares). Entrega hoja de ruta MoSCoW. |

### Guías

| Artefacto | ¿Qué problema resuelve? |
|-----------|-------------------------|
| **Lineamientos para Skills** | Estandariza la creación y modificación de skills dentro del chapter. Define estructura de directorios, frontmatter, scripts, evals y control de versiones. |

---

## Para qué sirve cada uno

| Artefacto | Úsalo cuando |
|-----------|-------------|
| Heuristy | Necesites una auditoría rápida de usabilidad antes de un lanzamiento. Quieras priorizar problemas de UX con datos (severidad, impacto, esfuerzo). Trabajes en banca digital o e-commerce y necesites cubrir normativa. |
| Accesibilidad WCAG | Te exijan cumplimiento legal de accesibilidad (Circular SFC, Ley 1618, MinTIC). Quieras certificar nivel A/AA/AAA. Necesites reportes técnicos + ejecutivos + declaración de conformidad. |
| Tognazzini | Estés diseñando o auditando el flujo de crédito de vivienda. Necesites una evaluación centrada en la experiencia del usuario, no solo en la interfaz. |
| Proto-Persona Top Tier | Quieras validar que tu producto bancario cumple las expectativas del segmento premium. Necesites behavioral insights del cliente de altos ingresos. Quieras reinterpretar hallazgos de otros skills desde la perspectiva Top Tier. |
| Consultor Madurez DS | Necesites diagnosticar el estado actual de tu Design System. Quieras una hoja de ruta para evolucionarlo. Estés en una organización que busca estandarizar su DS. |
| Lineamientos Skills | Vayas a crear un skill nuevo en este chapter. Necesites saber la estructura obligatoria, el formato de frontmatter o los estándares de scripts Python. |

---

## Cómo usarlos

Cada skill opera en **dos modos** que se detectan automáticamente:

### Modo ID (Claude Desktop / Claude.ai)
1. Copia el contenido del `SKILL.md` (o del archivo plano) y pégalo en el chat.
2. Sigue las instrucciones del skill — normalmente comienza pidiendo contexto.
3. El skill evalúa, analiza y entrega el reporte completo dentro de la conversación.
4. No requiere terminal, scripts ni instalación.

### Modo CLI (Claude Code)
1. El skill se activa por palabras clave definidas en su frontmatter.
2. El modelo sigue el workflow documentado en el `SKILL.md`.
3. Además, los scripts Python están disponibles para automatizar cálculos y reportes.
4. Los scripts usan solo biblioteca estándar de Python 3.8+, sin dependencias externas.

### Ejemplos de activación

| Skill | Modo ID (en el chat) | Modo CLI (Claude Code) |
|-------|----------------------|------------------------|
| Heuristy | _"Evalúa heurísticamente el flujo de login de [URL]"_, _"Haz una auditoría UX del checkout de [URL] para retail"_ | `python scripts/calculate_score.py hallazgos.json`, `python scripts/generate_report.py hallazgos.json` |
| Accesibilidad WCAG | _"Audita la accesibilidad de [URL] nivel AA"_, _"Revisa el contraste de color de [URL]"_ | `python scripts/check_contrast.py --foreground #fff --background #000` |
| Tognazzini | _"Evalúa el flujo de solicitud de crédito de vivienda de [URL] usando heurísticas de Tognazzini"_ | No tiene scripts (skill plano) |
| Proto-Persona Top Tier | _"Evalúa el login de [URL] como cliente Top Tier"_, _"Dame behavioral insights sobre wealth management"_ | `python scripts/calculate_tte_score.py hallazgos.json`, `python scripts/extract_insights.py hallazgos.json` |
| Consultor Madurez DS | _"Necesito un test de madurez de mi Design System"_, _"Diagnostica la gestión y operación de mi DS"_ | No tiene scripts (skill plano) |

---

## Cómo instalarlos

Este repositorio es **privado**. Para acceder necesitas estar invitado e iniciar sesión en GitHub.

### Opción A — Leer directamente en GitHub (lo más simple)
1. Abre `https://github.com/davidortiz-ops/KC-People-Center-Design-AI`
2. Entra a `diseno-de-soluciones/` y haz clic en el archivo que necesites.
3. GitHub lo muestra formateado. Usa el botón **"Copy raw file"** para copiar el contenido.
4. Pégalo directamente en el chat de Claude (modo ID). No requiere instalación.

### Opción B — Descargar todo el repositorio
1. En la página principal del repo, haz clic en **`<> Code`** → **"Download ZIP"**.
2. Descomprime en tu computador.
3. Para los skills planos: abre el `.md` y copia el contenido al chat.
4. Para los skills estructurados: abre `SKILL.md` y copia el contenido al chat, o desde la terminal usa los scripts Python.

### Opción C — Clonar con Git (para uso frecuente)
```bash
git clone https://github.com/davidortiz-ops/KC-People-Center-Design-AI.git
cd KC-People-Center-Design-AI/diseno-de-soluciones
```

### Opción D — Usar el visor web
1. Desde la carpeta del repositorio, ejecuta: `python -m http.server 8000`
2. Abre `http://localhost:8000/index.html` en el navegador.
3. Filtra por el chapter **Diseño de Soluciones**.
4. Haz clic en cualquier tarjeta para ver y copiar el contenido completo.

---

## Estructura del chapter

```
diseno-de-soluciones/
├── accesibilidad-wcag/                          # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   ├── references/                              # 14 referencias
│   │   ├── checklist-wcag-22.md                 # 87 criterios WCAG 2.2
│   │   ├── calculo-contraste-manual.md          # Fórmula de contraste
│   │   ├── normativa-colombiana.md              # Leyes Colombia
│   │   ├── protocolo-lectores-pantalla.md       # NVDA, JAWS, VoiceOver
│   │   ├── patrones-*.md                        # 7 guías de remediación
│   │   ├── seguridad-accesible.md               # Auth, timeouts
│   │   ├── metodologia-evaluacion.md            # Paso a paso auditoría
│   │   ├── priorizacion-remediacion.md          # Matriz severidad × esfuerzo
│   │   ├── presentacion-datos.md               # Tablas, gráficos
│   │   ├── responsive-y-objetivos.md           # Zoom, reflujo
│   │   └── verticales/                          # banca.md, retail.md
│   ├── scripts/                                 # 3 scripts CLI
│   └── templates/                               # 3 plantillas de reporte
│
├── evaluacion-heuristica/                       # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   ├── references/                              # 4 referencias
│   │   ├── banking-heuristics.md                # H11-H14 banca
│   │   ├── retail-heuristics.md                 # H11-H14 retail
│   │   ├── severity-examples.md                 # Ejemplos por industria
│   │   └── report-templates.md                  # Plantillas
│   └── scripts/                                 # 4 scripts + 2 plantillas JSON
│
├── proto-persona-banca-top-tier/                # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Perfil fundacional
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   └── scripts/                                 # 3 scripts + 2 plantillas JSON
│
├── consultor-madurez-design-systems.md          # Skill plano
├── tognazzini-revision-heuristica-creditos-vivienda.md  # Skill plano
├── lineamientos-skills.md                       # Guía de estándares
└── README.md                                    # Este archivo
```

---

## Skills que se complementan

| Combinación | Para qué sirve |
|-------------|---------------|
| Heuristy + Accesibilidad WCAG | Auditoría completa: usabilidad + accesibilidad. Detecta problemas de diseño y barreras de acceso en una misma evaluación. |
| Heuristy / Tognazzini + Proto-Persona Top Tier | El skill base evalúa técnicamente; la proto-persona reinterpreta cada hallazgo desde la perspectiva del cliente premium. Ajusta severidad y prioridad según cómo los experimenta este segmento. |
| Proto-Persona Top Tier + Accesibilidad WCAG | Evalúa la accesibilidad desde la perspectiva de un usuario de altos ingresos con posibles discapacidades o preferencias de accesibilidad. |
| Consultor Madurez DS + Proto-Persona Top Tier | Evalúa si la madurez del Design System soporta adecuadamente las necesidades del segmento premium. |

---

## Archivos totales en el chapter

| Tipo | Cantidad |
|------|:--------:|
| Skills estructurados (carpeta) | 3 |
| Skills planos (archivo único) | 2 |
| Guías | 1 |
| **Total artefactos** | **6** |
| Referencias técnicas | 18 |
| Scripts Python / Shell | 11 |
| Plantillas de reporte | 3 |
| Archivos de evaluación (evals) | 3 |
