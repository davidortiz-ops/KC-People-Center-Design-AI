---
name: seo-local
description: >
  Análisis SEO local que cubre optimización de Google Business Profile,
  consistencia NAP, salud de citas, señales de reseñas, schema markup local,
  calidad de páginas de ubicación, SEO multi-ubicación y recomendaciones
  específicas por industria. Detecta tipo de negocio (brick-and-mortar, SAB,
  hybrid) y vertical de industria. Usar cuando el usuario diga "local SEO",
  "Google Business Profile", "GBP", "map pack", "local pack", "citations",
  "NAP", "local rankings", "service area", "multi-location", "local search".
license: Proprietary - Pragma (uso interno y confidencial)
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
metadata:
  version: "1.0"
  author: Pragma
---

# Análisis SEO Local

## Detección de Tipo de Negocio

### Brick-and-Mortar
- Dirección física visible en footer o contacto
- Google Maps embebido
- "Visítanos en", "Ubicado en"
- Schema LocalBusiness con streetAddress

### Service Area Business (SAB)
- Sin dirección visible
- "Sirviendo a [ciudad/región]"
- "Vamos a tu ubicación", "Servicio en sitio"
- areaServed en schema sin streetAddress

### Hybrid
- Ambos: dirección física + lenguaje de área de servicio

## Detección de Vertical de Industria

| Vertical | Señales de Detección |
|----------|----------------------|
| Restaurante | /menu, tipos de cocina, reservaciones |
| Salud | seguros aceptados, citas, NPI |
| Legal | abogado, áreas de práctica, admisión al colegio de abogados |
| Servicios del Hogar | área de servicio, emergencias, "presupuesto gratis" |
| Bienes Raíces | listados, MLS, propiedades en venta |
| Automotriz | inventario, VIN, test drive, concesionario |

## Dimensiones de Análisis

### 1. Señales de GBP (25%)

La categoría principal es el factor individual más importante para el local pack.

**Verificar:**
- GBP embebido detectable en la página
- Adecuación de la categoría principal
- Evidencia de categorías secundarias (óptimo: 4+)
- Presencia de publicaciones en GBP
- Insignia de Google Verified
- Horario de atención visible en la página

### 2. Reseñas y Reputación (20%)

**Regla de los 18 días** (Sterling Sky): el ranking cae si no hay reseñas nuevas en 3 semanas.

**Verificar:**
- Cantidad total de reseñas (umbral mágico: 10)
- Calificación por estrellas (68% solo usan 4+)
- Relevancia de reseñas (74% solo importan los últimos 3 meses)
- aggregateRating en schema
- Presencia multi-plataforma
- Patrones de respuesta del dueño

### 3. SEO Local On-Page (20%)

Páginas de servicio dedicadas = factor #1 de SEO local orgánico.

**Verificar:**
- Title tag con keywords de ciudad/servicio
- H1 con intención local
- NAP visible en HTML
- Páginas de servicio dedicadas
- >60-70% contenido único por página de ubicación
- Google Map embebido
- Botón de click-to-call
- Enlazado interno hub-and-spoke

### 4. Consistencia NAP y Citas (15%)

Las citas = 3 de los 5 factores principales de visibilidad en IA (Whitespark 2026).

**Verificar:**
- Consistencia de NAP: HTML de página vs schema vs GBP
- Presencia de citas: Yelp, BBB, Facebook
- Apple Business Connect (uso duplicado al 27%)
- Bing Places (impulsa ChatGPT, Copilot, Alexa)
- Agregadores de datos: Data Axle, Foursquare, Neustar

### 5. Schema Markup Local (10%)

**Verificar:**
- Presencia de schema LocalBusiness
- Requerido: name, address, telephone
- Recomendado: geo (5+ decimales), openingHoursSpecification, priceRange
- Subtipo correcto según la industria
- SAB: areaServed ciudades
- Multi-ubicación: @id único por ubicación, branchOf

### 6. Señales de Autoridad Local (10%)

- Menciones en Cámara de Comercio
- Acreditación BBB
- Noticias/prensa local
- Participación comunitaria
- Apariciones en listas "Best of" (#1 factor de citación en visibilidad IA)

## Impacto de la Búsqueda IA en SEO Local

- AI Overviews en hasta el 68% de las búsquedas locales
- ChatGPT convierte al 15.9% vs Google orgánico 1.76%
- ChatGPT NO accede directamente a GBP — obtiene datos de Bing, Yelp, TripAdvisor, BBB, Reddit
- Bing Places es crítico (impulsa ChatGPT, Copilot, Alexa)

## Salida

```
## Puntuación SEO Local: XX/100

### Tipo de Negocio: [Brick-and-Mortar / SAB / Hybrid]
### Industria: [detectada]

### Desglose por Dimensión
| Dimensión | Puntuación | Problemas Clave |
|-----------|------------|-----------------|
| Señales GBP | XX/25 | ... |
| Reseñas y Reputación | XX/20 | ... |
| SEO Local On-Page | XX/20 | ... |
| NAP y Citas | XX/15 | ... |
| Schema | XX/10 | ... |
| Autoridad | XX/10 | ... |

### Top 10 Acciones Priorizadas
1. [Crítico] ...
2. [Alto] ...
...
```

## Ganancias Rápidas

1. Reclamar Apple Business Connect
2. Reclamar y optimizar Bing Places
3. Corregir discrepancias de NAP
4. Agregar schema LocalBusiness con el subtipo correcto
5. Agregar coordenadas geo (precisión de 5+ decimales)
6. Agregar enlace tel: para click-to-call

## Integración entre Skills

| Skill | Integración |
|-------|-------------|
| **seo-geo** | Visibilidad en búsqueda IA para consultas locales |
| **seo-schema** | Generación de schema LocalBusiness |
| **seo-images** | Optimización de fotos de negocio local |
