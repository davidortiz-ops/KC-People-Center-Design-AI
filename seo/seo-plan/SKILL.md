---
name: seo-plan
description: >
  Planificación estratégica SEO para sitios web nuevos o existentes. Plantillas
  específicas por industria, análisis competitivo, estrategia de contenido y hoja
  de ruta de implementación. Úsala cuando el usuario diga "plan SEO", "estrategia SEO",
  "estrategia de contenido", "arquitectura de sitio" o "hoja de ruta SEO".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
  - WebSearch
---

# Planificación Estratégica SEO

## Proceso

### 1. Descubrimiento
- Tipo de negocio, audiencia objetivo, competidores, metas
- Evaluación del sitio actual (si existe)
- Restricciones de presupuesto y cronograma
- Indicadores clave de rendimiento (KPIs)

### 2. Análisis Competitivo
- Identificar top 5 competidores
- Analizar su estrategia de contenido, uso de schema, configuración técnica
- Identificar brechas de keywords y oportunidades de contenido
- Evaluar sus señales E-E-A-T
- Estimar su autoridad de dominio

### 3. Diseño de Arquitectura
- Cargar plantilla de industria desde el directorio `assets/`
- Diseñar jerarquía de URLs y pilares de contenido
- Planificar estrategia de enlazado interno
- Estructura de sitemap con quality gates aplicados
- Arquitectura de información para recorridos de usuario

### 4. Estrategia de Contenido
- Brechas de contenido vs competidores
- Tipos de página y cantidades estimadas
- Temas de blog/recursos y cadencia de publicación
- Plan de construcción de E-E-A-T (biografías de autor, credenciales, señales de experiencia)
- Calendario de contenido con prioridades

### 5. Base Técnica
- Requisitos de hosting y rendimiento
- Plan de schema markup por tipo de página
- Objetivos base de Core Web Vitals
- Requisitos de preparación para búsqueda con IA
- Consideraciones mobile-first

### 6. Hoja de Ruta de Implementación (4 fases)

#### Fase 1 — Base (semanas 1-4)
- Configuración técnica e infraestructura
- Páginas principales (inicio, about, contacto, servicios principales)
- Implementación de schema esencial
- Configuración de analítica y tracking

#### Fase 2 — Expansión (semanas 5-12)
- Creación de contenido para páginas principales
- Lanzamiento de blog con artículos iniciales
- Estructura de enlazado interno
- Configuración de SEO Local (si aplica)

#### Fase 3 — Escalamiento (semanas 13-24)
- Desarrollo de contenido avanzado
- Link building y outreach
- Optimización GEO
- Optimización de rendimiento

#### Fase 4 — Autoridad (meses 7-12)
- Contenido de liderazgo de pensamiento
- RRPP y menciones en medios
- Implementación de schema avanzado
- Optimización continua

## Plantillas por Industria

Cargar desde el directorio `assets/`:
- `saas.md` — Empresas SaaS/software
- `local-service.md` — Negocios de servicios locales
- `ecommerce.md` — Tiendas de e-commerce
- `publisher.md` — Editores de contenido/medios
- `agency.md` — Agencias y consultorías
- `generic.md` — Plantilla general de negocios

## Salida

### Entregables
- `SEO-STRATEGY.md` — Plan estratégico completo
- `COMPETITOR-ANALYSIS.md` — Insights competitivos
- `CONTENT-CALENDAR.md` — Hoja de ruta de contenido
- `IMPLEMENTATION-ROADMAP.md` — Plan de acción por fases
- `SITE-STRUCTURE.md` — Jerarquía de URLs y arquitectura

### Objetivos de KPI
| Métrica | Línea Base | 3 Meses | 6 Meses | 12 Meses |
|--------|----------|---------|---------|----------|
| Tráfico Orgánico | ... | ... | ... | ... |
| Rankings de Keywords | ... | ... | ... | ... |
| Autoridad de Dominio | ... | ... | ... | ... |
| Páginas Indexadas | ... | ... | ... | ... |
| Core Web Vitals | ... | ... | ... | ... |

### Criterios de Éxito
- Metas claras y medibles por fase
- Requisitos de recursos definidos
- Dependencias identificadas
- Estrategias de mitigación de riesgos
