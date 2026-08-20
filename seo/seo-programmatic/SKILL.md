---
name: seo-programmatic
description: >
  Planificación y análisis SEO programático para páginas generadas a escala desde
  fuentes de datos. Cubre motores de plantillas, patrones de URL, automatización de
  enlazado interno, salvaguardas contra contenido thin y prevención de index bloat.
  Úsala cuando el usuario diga "SEO programático", "páginas a escala", "páginas
  dinámicas", "páginas de plantilla", "páginas generadas" o "SEO basado en datos".
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

# Análisis y Planificación SEO Programático

Construye y audita páginas SEO generadas a escala desde fuentes de datos estructurados.
Aplica quality gates para prevenir penalizaciones por contenido thin e index bloat.

## Evaluación de la Fuente de Datos

Evaluar los datos que alimentan las páginas programáticas:
- **Archivos CSV/JSON**: Conteo de filas, unicidad de columnas, valores faltantes
- **Endpoints API**: Estructura de respuesta, frescura de datos, límites de tasa
- **Consultas a base de datos**: Conteo de registros, completitud de campos, frecuencia de actualización
- Controles de calidad de datos:
  - Cada registro debe tener suficientes atributos únicos para generar contenido distinto
  - Marcar registros duplicados o casi duplicados (>80% de superposición de campos)
  - Verificar frescura de datos — datos desactualizados producen páginas desactualizadas

## Planificación del Motor de Plantillas

Diseñar plantillas que produzcan páginas únicas y valiosas:
- **Puntos de inyección de variables**: Título, H1, secciones del cuerpo, meta description, schema
- **Bloques de contenido**: Estáticos (compartidos entre páginas) vs dinámicos (únicos por página)
- **Lógica condicional**: Mostrar/ocultar secciones según disponibilidad de datos
- **Contenido suplementario**: Elementos relacionados, consejos contextuales, contenido generado por usuarios
- Lista de verificación de plantillas:
  - Cada página debe leerse como un recurso independiente y valioso
  - Sin patrones "mad-libs" (solo intercambiar nombres de ciudades/productos en texto idéntico)
  - Las secciones dinámicas deben agregar información genuina, no solo variaciones de keywords

## Estrategia de Patrones de URL

### Patrones Comunes
- `/tools/[tool-name]` — Páginas de directorio de herramientas/productos
- `/[city]/[service]` — Páginas de ubicación + servicio
- `/integrations/[platform]` — Páginas de aterrizaje de integraciones
- `/glossary/[term]` — Páginas de definición/referencia
- `/templates/[template-name]` — Páginas de plantillas descargables

### Reglas de URL
- Minúsculas, slugs con guiones derivados de los datos
- Jerarquía lógica que refleje la arquitectura del sitio
- Sin slugs duplicados — forzar unicidad al momento de generación
- Mantener URLs bajo 100 caracteres
- Sin parámetros de query para URLs de contenido principal
- Uso consistente de trailing slash (coincidir con el patrón existente del sitio)

## Automatización de Enlazado Interno

- **Modelo hub/spoke**: Páginas hub de categoría enlazando a páginas programáticas individuales
- **Elementos relacionados**: Auto-enlazar a 3-5 páginas relacionadas según atributos de datos
- **Migas de pan**: Generar schema BreadcrumbList desde la jerarquía de URL
- **Cross-linking**: Enlazar entre páginas programáticas que compartan atributos (misma categoría, misma ciudad, misma característica)
- **Anchor text**: Usar texto de anclaje descriptivo y variado — evitar repetición exacta de keyword
- Densidad de enlaces: 3-5 enlaces internos por cada 1000 palabras (coincidir con directrices seo-content)

## Salvaguardas contra Contenido Thin

### Quality Gates

| Métrica | Umbral | Acción |
|--------|-----------|--------|
| Páginas sin revisión de contenido | 100+ | ⚠️ ADVERTENCIA — requerir auditoría de contenido antes de publicar |
| Páginas sin justificación | 500+ | 🛑 DETENCIÓN — requerir aprobación explícita del usuario y auditoría de contenido thin |
| Contenido único por página | <40% | ❌ Marcar como contenido thin — probable riesgo de penalización |
| Recuento de palabras por página | <300 | ⚠️ Marcar para revisión — puede carecer de valor suficiente |

### Abuso de Contenido a Escala — Contexto de Aplicación (2025-2026)

La política de Abuso de Contenido a Escala de Google (introducida en marzo 2024) tuvo una escalada importante de aplicación en 2025:

- **Junio 2025:** Ola de acciones manuales targeting sitios web con contenido generado por IA a escala
- **Agosto 2025:** Actualización antispam de SpamBrain mejoró la detección de patrones para esquemas de enlaces generados por IA y content farms
- **Resultado:** Google reportó una reducción del 45% en contenido de baja calidad y no original en resultados de búsqueda tras la aplicación de marzo 2024

**Quality Gates mejorados para páginas programáticas:**
- **Diferenciación de contenido:** ≥30-40% del contenido debe ser genuinamente único entre dos páginas programáticas (no solo reemplazo de ciudad/keyword)
- **Revisión humana:** Mínimo 5-10% de muestra revisada de páginas generadas antes de publicar
- **Implementación progresiva:** Publicar en lotes de 50-100 páginas. Monitorear indexación y rankings por 2-4 semanas antes de expandir. Nunca publicar 500+ páginas programáticas simultáneamente sin revisión de calidad explícita.
- **Prueba de valor independiente:** Cada página debe pasar: "¿Vale la pena publicar esta página aunque no existieran otras páginas similares?"
- **Abuso de reputación del sitio:** Si publicas contenido programático bajo un dominio de alta autoridad (no propio), esto puede activar penalizaciones por abuso de reputación del sitio. Google comenzó a aplicar esto agresivamente en noviembre de 2024.

> **Recomendación:** El gate de ADVERTENCIA en `<40% contenido único` sigue siendo apropiado. Considera una DETENCIÓN en `<30%` contenido único para prevenir riesgo de abuso de contenido a escala.

### Páginas Programáticas Seguras (OK a escala)
✅ Páginas de integraciones (con docs de configuración reales, detalles de API, capturas de pantalla)
✅ Páginas de plantillas/herramientas (con contenido descargable, instrucciones de uso)
✅ Páginas de glosario (definiciones de 200+ palabras con ejemplos, términos relacionados)
✅ Páginas de producto (especificaciones únicas, reseñas, datos de comparación)
✅ Páginas basadas en datos (estadísticas únicas, gráficos, análisis por registro)

### Riesgo de Penalización (evitar a escala)
❌ Páginas de ubicación con solo el nombre de la ciudad intercambiado en texto idéntico
❌ "Mejor [herramienta] para [industria]" sin valor específico de la industria
❌ "Alternativa a [competidor]" sin datos de comparación reales
❌ Páginas generadas por IA sin revisión humana y valor añadido único
❌ Páginas donde >60% del contenido es boilerplate compartido de plantilla

### Cálculo de Unicidad
% contenido único = (palabras únicas de esta página) / (total de palabras en la página) × 100

Medir contra todas las demás páginas del conjunto programático. Los encabezados, pies de página y navegación compartidos se excluyen del cálculo. El texto boilerplate de plantilla SÍ se incluye.

## Estrategia de Canonical

- Cada página programática debe tener un tag canonical auto-referenciado
- Variaciones de parámetros (ordenar, filtrar, paginación) canonical a la URL base
- Series paginadas: canonical a página 1 o usar rel=next/prev
- Si las páginas programáticas se superponen con páginas manuales, la página manual es la canonical
- Sin canonical a un dominio diferente a menos que sea configuración intencional cross-domain

## Integración con Sitemap

- Auto-generar entradas de sitemap para todas las páginas programáticas
- Dividir en 50,000 URLs por archivo de sitemap (límite del protocolo)
- Usar índice de sitemap si se necesitan múltiples archivos de sitemap
- `<lastmod>` refleja la marca de tiempo real de actualización de datos (no la hora de generación)
- Excluir páginas programáticas no indexables del sitemap
- Registrar sitemap en robots.txt
- Actualizar sitemap dinámicamente a medida que se agreguen nuevos registros a la fuente de datos

## Prevención de Index Bloat

- **Noindex en páginas de bajo valor**: Páginas que no cumplen con los quality gates
- **Paginación**: Noindex en resultados paginados más allá de página 1 (o usar rel=next/prev)
- **Navegación facetada**: Noindex en vistas filtradas, canonical a la categoría base
- **Presupuesto de crawl**: Para sitios con >10k páginas programáticas, monitorear estadísticas de crawl en Search Console
- **Consolidación de páginas thin**: Fusionar registros con datos insuficientes en páginas agregadas
- **Auditorías regulares**: Revisión mensual del recuento de páginas indexadas vs recuento previsto

## Salida

### Puntuación SEO Programático: XX/100

### Resumen de Evaluación
| Categoría | Estado | Puntuación |
|----------|--------|-------|
| Calidad de Datos | ✅/⚠️/❌ | XX/100 |
| Unicidad de Plantilla | ✅/⚠️/❌ | XX/100 |
| Estructura de URL | ✅/⚠️/❌ | XX/100 |
| Enlazado Interno | ✅/⚠️/❌ | XX/100 |
| Riesgo de Contenido Thin | ✅/⚠️/❌ | XX/100 |
| Gestión de Indexación | ✅/⚠️/❌ | XX/100 |

### Problemas Críticos (corregir inmediatamente)
### Prioridad Alta (corregir en 1 semana)
### Prioridad Media (corregir en 1 mes)
### Prioridad Baja (backlog)

### Recomendaciones
- Mejoras en la fuente de datos
- Modificaciones de plantilla
- Ajustes de patrón de URL
- Acciones de cumplimiento de quality gates
