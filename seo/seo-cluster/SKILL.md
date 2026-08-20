---
name: seo-cluster
description: >
  Agrupación semántica de topics basada en SERP para planificación de
  arquitectura de contenido. Agrupa keywords por superposición real en
  SERPs de Google (no por similitud de texto), diseña clusters de contenido
  hub-and-spoke con matrices de internal linking y genera visualizaciones
  interactivas. Usar cuando el usuario diga "topic cluster",
  "content cluster", "semantic clustering", "pillar page", "hub and spoke",
  "content architecture", "cluster plan".
license: Proprietary - Pragma (uso interno y confidencial)
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - Bash
  - WebFetch
  - WebSearch
metadata:
  version: "1.0"
  author: Pragma
---

# Agrupación Semántica de Topics

Agrupación de keywords impulsada por superposición en SERP para arquitectura de contenido. Agrupa keywords
por cómo Google realmente las rankea (resultados compartidos en top 10), no por similitud
de texto. Diseña clusters hub-and-spoke con matrices de internal linking.

## Referencia Rápida

| Comando | Qué hace |
|---------|-------------|
| `/seo cluster plan <seed-keyword>` | Flujo de planificación completo: expandir, agrupar, arquitecturar, visualizar |
| `/seo cluster plan --from strategy` | Importar desde salida existente de `/seo plan` |
| `/seo cluster execute` | Ejecutar plan: crear content briefs |
| `/seo cluster map` | Regenerar visualización interactiva del cluster |

## Flujo de Planificación

### Paso 1: Expansión de Seed Keyword

Expandir seed keyword en 30-50 variantes usando WebSearch:

1. **Búsquedas relacionadas** — Buscar seed, extraer "related searches" y "people also search for"
2. **People Also Ask (PAA)** — Extraer todas las preguntas PAA
3. **Modificadores de long-tail** — Agregar: "best", "how to", "vs", "for beginners", "tools", "guide"
4. **Minería de preguntas** — variantes who/what/when/where/why/how
5. **Modificadores de intención** — "pricing", "review", "alternative", "comparison"

Objetivo: 30-50 variantes de keyword únicas.

### Paso 2: Agrupación por Superposición en SERP

Diferenciador principal. Agrupar keywords por superposición real en SERPs.

**Proceso:**
1. Agrupar keywords por suposición inicial de intención
2. Para cada par, buscar ambas keywords en WebSearch
3. Contar URLs compartidas en los top 10 resultados orgánicos
4. Aplicar umbrales:

| Resultados Compartidos | Relación | Acción |
|---------------|-------------|--------|
| 7-10 | Mismo post | Fusionar en una sola página objetivo |
| 4-6 | Mismo cluster | Agrupar bajo el mismo spoke cluster |
| 2-3 | Interenlazar | Colocar en clusters adyacentes |
| 0-1 | Separado | Asignar a clusters diferentes |

### Paso 3: Clasificación de Intención

| Intención | Señales | ¿Incluir? |
|--------|---------|----------|
| Informacional | how, what, why, guide, tutorial | Sí |
| Comercial | best, top, review, comparison, vs | Sí |
| Transaccional | buy, price, discount, coupon | Sí |
| Navegacional | nombres de marca, login | No (excluir) |

### Paso 4: Arquitectura Hub-and-Spoke

1. **Seleccionar keyword pilar** — Mayor volumen, intención más amplia, más superposición en SERP
2. **Agrupar spokes en clusters** — 2-5 clusters por pilar
3. **Asignar posts a clusters** — 2-4 spoke posts por cluster
4. **Objetivos de word count:** Pilar: 2500-4000 palabras. Spokes: 1200-1800 palabras

### Paso 5: Matriz de Internal Linking

| Tipo de Enlace | Dirección | Requisito |
|-----------|-----------|-------------|
| Spoke a pilar | spoke -> pillar | Obligatorio (cada spoke) |
| Pilar a spoke | pillar -> spoke | Obligatorio (cada spoke) |
| Spoke a spoke (dentro del cluster) | spoke <-> spoke | 2-3 enlaces por post |

### Paso 6: Mapa de Cluster Interactivo

Generar `cluster-map.html` con visualización SVG interactiva de nodos y enlaces.

## Content Briefs (cuando no hay blog skill)

Generar content briefs detallados para cada post del cluster:
- Título y meta description
- Keywords primaria + secundarias
- Tipo de template y estructura sugerida (H2/H3)
- Objetivo de word count
- Internal links a incluir
- Puntos clave a cubrir

## Flujo de Ejecución

Cuando se invoca `/seo cluster execute`:

1. Leer `cluster-plan.json`
2. Ejecutar en orden de prioridad: pilar primero, spokes por volumen
3. Para cada post, generar brief con:
   - Rol en el cluster (pilar o spoke)
   - Keyword objetivo y keywords secundarias
   - Tipo de template y word count
   - Internal links a incluir
4. Integrar con script de content brief:
   ```bash
   python scripts/seo/content_brief.py --site <s> --keyword "kw"
   ```

## Archivos de Salida

| Archivo | Descripción |
|------|-------------|
| `cluster-plan.json` | Plan de cluster legible por máquina |
| `cluster-plan.md` | Resumen legible por humanos |
| `cluster-map.html` | Visualización SVG interactiva |
| `cluster-briefs/` | Content briefs para cada post |

## Integración entre Skills

| Skill | Relación |
|-------|-------------|
| **seo-plan** | Fuente de importación para estrategia |
| **seo-content** | Análisis E-E-A-T y guía de contenido para cada spoke |
| **seo-schema** | Schema para páginas del cluster (Article, BreadcrumbList) |
| **seo-google** | Datos de keywords y oportunidades desde GSC real |

## Manejo de Errores

| Error | Resolución |
|-------|-----------|
| Variantes de keyword insuficientes (<15) | Ejecutar segunda pasada de expansión con PAA |
| Datos SERP no disponibles | Reintentar después de 30s; usar agrupación solo por intención |
| Sin archivo de estrategia | Ejecutar `/seo plan` primero |
