---
name: seo
description: >
  Análisis SEO integral para cualquier sitio web o tipo de negocio. Realiza auditorías
  completas de sitio, análisis profundo de página individual, verificaciones técnicas
  SEO (crawlability, indexability, Core Web Vitals con INP), detección/validación/generación
  de schema markup, evaluación de calidad de contenido (framework E-E-A-T según la
  actualización de diciembre 2025 que se extiende a todas las consultas competitivas),
  optimización de imágenes, análisis de sitemap y Generative Engine Optimization (GEO)
  para AI Overviews, ChatGPT y citas en Perplexity. Analiza accesibilidad de crawlers
  de IA (GPTBot, ClaudeBot, PerplexityBot), cumplimiento de llms.txt, señales de mención
  de marca y citabilidad a nivel de pasaje. Detección de industria para SaaS, e-commerce,
  negocios locales, publishers, agencias. Se activa con: "SEO", "auditoría", "schema",
  "Core Web Vitals", "sitemap", "E-E-A-T", "AI Overviews", "GEO", "SEO técnico",
  "calidad de contenido", "velocidad de página", "datos estructurados".
---

# SEO — Skill de Análisis SEO Universal

Análisis SEO integral para todas las industrias (SaaS, servicios locales,
e-commerce, publishers, agencias). Orquesta 20 sub-skills especializadas mediante
delegación paralela a subagentes.

## Referencia Rápida

| Comando | Qué hace |
|---------|---------|
| `/seo audit <url>` | Auditoría completa de sitio con delegación paralela de subagentes |
| `/seo page <url>` | Análisis profundo de página individual |
| `/seo sitemap <url or generate>` | Analizar o generar sitemaps XML |
| `/seo schema <url>` | Detectar, validar y generar Schema.org markup |
| `/seo images <url>` | Análisis de optimización de imágenes |
| `/seo technical <url>` | Auditoría técnica SEO (9 categorías) |
| `/seo content <url>` | Análisis E-E-A-T y calidad de contenido |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <tipo-de-negocio>` | Planificación estratégica SEO |
| `/seo programmatic [url|plan]` | Análisis y planificación SEO programático |
| `/seo competitor-pages [url|generate]` | Generación de páginas de comparación de competidores |
| `/seo hreflang [url]` | Auditoría y generación de hreflang/i18n SEO |
| `/seo google <url>` | APIs de Google (GSC, PSI, CrUX, GA4) + oportunidades de keywords |

## Lógica de Orquestación

Cuando el usuario invoca `/seo audit`, delegar a subagentes en paralelo:
1. Detectar tipo de negocio (SaaS, local, ecommerce, publisher, agencia, otro)
2. Lanzar subagentes: seo-technical, seo-content, seo-schema, seo-sitemap, seo-geo, seo-google, seo-local, seo-sxo
3. Recopilar resultados y generar reporte unificado con SEO Health Score (0-100)
4. Crear plan de acción priorizado (Crítico → Alto → Medio → Bajo)

Para comandos individuales, cargar el sub-skill relevante directamente.

## Detección de Industria

Detectar tipo de negocio desde señales de la página de inicio:
- **SaaS**: página de precios, /features, /integrations, /docs, "prueba gratuita", "registrarse"
- **Servicio Local**: número de teléfono, dirección, área de servicio, "sirviendo a [ciudad]", Google Maps embed
- **E-commerce**: /products, /collections, /cart, "añadir al carrito", schema de producto
- **Publisher**: /blog, /articles, /topics, schema de artículo, páginas de autor, fechas de publicación
- **Agencia**: /case-studies, /portfolio, /industries, "nuestro trabajo", logotipos de clientes

## Quality Gates

Leer `references/quality-gates.md` para umbrales de contenido thin por tipo de página.
Reglas estrictas:
- ⚠️ ADVERTENCIA en 30+ páginas de ubicación (exigir 60%+ contenido único)
- 🛑 DETENCIÓN en 50+ páginas de ubicación (requerir justificación del usuario)
- Nunca recomendar schema HowTo (obsoleto desde septiembre 2023)
- Schema FAQ para rich results de Google: solo sitios gubernamentales y de salud (restricción de agosto 2023); FAQPage existente en sitios comerciales → marcar como información (no Crítico), notando beneficio de citas en IA/LLM; agregar nuevo FAQPage → no recomendado para beneficio de Google
- Todas las referencias a Core Web Vitals usan INP, nunca FID

## Archivos de Referencia

Cargar bajo demanda según sea necesario — NO cargar todos al inicio:
- `references/cwv-thresholds.md` — Umbrales actuales de Core Web Vitals y detalles de medición
- `references/schema-types.md` — Todos los tipos de schema soportados con estado de deprecación
- `references/eeat-framework.md` — Criterios de evaluación E-E-A-T (actualización QRG de septiembre 2025)
- `references/quality-gates.md` — Mínimos de longitud de contenido, umbrales de unicidad

## Metodología de Puntuación

### SEO Health Score (0-100)
Agregado ponderado de todas las categorías:

| Categoría | Peso |
|----------|--------|
| SEO Técnico | 22% |
| Calidad de Contenido | 23% |
| SEO On-Page | 20% |
| Schema / Datos Estructurados | 10% |
| Rendimiento (CWV) | 10% |
| Preparación para Búsqueda con IA | 10% |
| Imágenes | 5% |

### Niveles de Prioridad
- **Crítico**: Bloquea indexación o causa penalizaciones (requiere corrección inmediata)
- **Alto**: Impacta significativamente los rankings (corregir en 1 semana)
- **Medio**: Oportunidad de optimización (corregir en 1 mes)
- **Bajo**: Deseable (backlog)

## Sub-Skills

Este skill orquesta 20 sub-skills especializadas:

1. **seo-audit** — Auditoría completa de sitio con delegación paralela
2. **seo-page** — Análisis profundo de página individual
3. **seo-technical** — Rastreo e indexación (canonical, robots, duplicados)
4. **seo-content** — E-E-A-T y calidad de contenido
5. **seo-schema** — Detección, validación y generación de schema markup
6. **seo-images** — Optimización de imágenes y video
7. **seo-on-page** — Meta tags, Open Graph, Twitter Cards, title link
8. **seo-sitemap** — Análisis y generación de sitemaps
9. **seo-geo** — AI Overviews / optimización GEO
10. **seo-performance** — Core Web Vitals (LCP, INP, CLS) y experiencia de página
11. **seo-accessibility** — Accesibilidad (ARIA, WCAG) con impacto SEO
12. **seo-plan** — Planificación estratégica con plantillas por industria
13. **seo-programmatic** — Análisis y planificación SEO programático
14. **seo-competitor-pages** — Generación de páginas de comparación de competidores
15. **seo-hreflang** — Auditoría y generación de hreflang/i18n SEO
16. **seo-google** — APIs SEO de Google (GSC, PSI, CrUX, GA4, Indexing) + oportunidades de keywords (GSC Insights)
17. **seo-local** — SEO Local: GBP, NAP, citas, reseñas
18. **seo-ecommerce** — SEO E-commerce: schema de producto, Shopping, brechas de marketplace
19. **seo-cluster** — Clustering temático basado en SERP y arquitectura hub-and-spoke
20. **seo-sxo** — Search Experience Optimization: detección de page-type mismatch

## Subagentes

Para análisis en paralelo durante auditorías:
- `seo-technical` — Rastreo, indexación, canonical, robots, duplicados
- `seo-content` — E-E-A-T, legibilidad, contenido thin
- `seo-schema` — Detección, validación, generación
- `seo-sitemap` — Estructura, cobertura, quality gates
- `seo-geo` — Acceso de crawlers IA, llms.txt, citabilidad, señales de mención de marca
- `seo-google` — Datos en vivo de GSC, PSI, CrUX, GA4 + oportunidades de keywords
- `seo-local` — GBP, NAP, citas, señales de reseñas
- `seo-sxo` — Page-type mismatch y scoring de personas

## Regla de Reporte Bilingüe

Cuando el sitio auditado está en inglés, todos los reportes deben generarse en dos
archivos separados:
- `FULL-AUDIT-REPORT.md` (inglés — para el cliente/equipo)
- `FULL-AUDIT-REPORT-ES.md` (español — para la agencia)

Para sitios en español, reporte único en español.
