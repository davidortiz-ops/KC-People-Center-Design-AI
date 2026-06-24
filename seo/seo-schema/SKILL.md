---
name: seo-schema
description: >
  Guía de implementación de datos estructurados JSON-LD, optimización para Featured
  Snippets (párrafo, lista, tabla) y cobertura completa de schema (Article, FAQ,
  Product, LocalBusiness, Review, Recipe, Event, etc.). Úsala cuando el usuario diga
  "schema", "datos estructurados", "JSON-LD", "structured data", "rich results",
  "featured snippet", "FAQ schema", "Product schema", o cuando agregue marcado para
  mejorar la elegibilidad de resultados enriquecidos.
version: 2.0.0
---

# Schema Avanzado y Snippets para SEO

## Cuándo usarlo
Usa esta skill cuando:
- Crees páginas con mucho contenido (blogs, artículos, FAQs, páginas de producto, páginas de negocio local).
- Escribas bloques de texto informativo que podrían calificar para Featured Snippets.
- Agregues datos estructurados para mejorar la elegibilidad de resultados enriquecidos en SERPs.
- Implementes marcado de productos de comercio electrónico o agregación de reseñas.

## Entradas requeridas
- El tipo de contenido de la página (artículo, FAQ, producto, negocio local, receta, evento, etc.).
- Puntos de datos clave: autor, fechas, precios, calificaciones, direcciones, etc.
- Si el contenido apunta a Featured Snippets de párrafo, lista o tabla.

## Procedimiento

### 1. Implementación de Schema JSON-LD
- Inserta un bloque `<script type="application/ld+json">` en el `<head>` o al final del `<body>`.
- Siempre establece `@context` como `"https://schema.org"`.
- Haz coincidir `@type` con el contenido de la página.

```html
<!-- Página de artículo -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Guía Completa de SEO Técnico",
  "author": {
    "@type": "Person",
    "name": "Jane Smith"
  },
  "datePublished": "2025-01-15",
  "dateModified": "2025-02-01",
  "image": "https://example.com/images/guia-seo.webp",
  "publisher": {
    "@type": "Organization",
    "name": "Example Corp",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
</script>
```

```html
<!-- Página de FAQ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Qué es el SEO técnico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "El SEO técnico se refiere a las optimizaciones que ayudan a los motores de búsqueda a rastrear e indexar tu sitio de manera más efectiva."
      }
    }
  ]
}
</script>
```

### 2. La Pirámide Invertida
- Las primeras 40-50 palabras de un bloque informativo DEBEN responder directamente a la consulta del usuario.
- Proporciona la respuesta concisa primero, luego expande con detalles.

```html
<!-- ✅ CORRECTO — Respuesta directa primero -->
<p>El SEO técnico es la práctica de optimizar la infraestructura de un sitio web
para que los motores de búsqueda puedan rastrearlo, indexarlo y renderizarlo
de manera efectiva. Cubre velocidad del sitio, compatibilidad móvil, datos
estructurados y eficiencia de rastreo. A diferencia del SEO de contenido, se
enfoca en el código y la arquitectura en lugar de las palabras en la página.</p>

<!-- ❌ INCORRECTO — Entierra la respuesta -->
<p>En el panorama digital actual, las empresas necesitan entender muchos
aspectos del marketing online. Un área importante que a menudo se pasa por
alto es algo llamado SEO técnico, que explicaremos más adelante después de
algún contexto de fondo...</p>
```

### 3. Formatos de Extracción de Datos
- Usa `<ul>` / `<ol>` para snippets basados en listas.
- Usa `<table>` para datos comparativos/tabulares.
- Nunca renderices datos estructurados como texto separado por comas en una etiqueta `<p>`.

```html
<!-- ✅ CORRECTO — Lista estructurada -->
<h2>Beneficios del SEO Técnico</h2>
<ul>
  <li>Tiempos de carga de página más rápidos</li>
  <li>Mejor eficiencia de rastreo</li>
  <li>Mejor experiencia móvil</li>
  <li>Resultados enriquecidos mejorados en SERPs</li>
</ul>

<!-- ✅ CORRECTO — Tabla comparativa -->
<table>
  <thead>
    <tr><th>Característica</th><th>SEO Técnico</th><th>SEO de Contenido</th></tr>
  </thead>
  <tbody>
    <tr><td>Enfoque</td><td>Infraestructura</td><td>Calidad del contenido</td></tr>
    <tr><td>Herramientas</td><td>Lighthouse, GSC</td><td>Ahrefs, SEMrush</td></tr>
  </tbody>
</table>
```

### 4. Schema WebSite (Cuadro de Búsqueda de Sitelinks y Nombre del Sitio)
- Agrega schema `WebSite` a tu página de inicio para habilitar un cuadro de búsqueda de sitelinks en los resultados de Google.
- Esto también controla el nombre del sitio que se muestra en SERPs.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Example Corp",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
</script>
```

### 5. Schema VideoObject
- Agrega datos estructurados `VideoObject` al incrustar videos para habilitar resultados enriquecidos de video.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Cómo Optimizar Core Web Vitals",
  "description": "Guía paso a paso para mejorar puntajes de LCP, CLS e INP.",
  "thumbnailUrl": "https://example.com/thumbnails/guia-cwv.jpg",
  "uploadDate": "2025-01-15",
  "duration": "PT8M30S",
  "contentUrl": "https://example.com/videos/guia-cwv.mp4",
  "embedUrl": "https://www.youtube.com/embed/abc123"
}
</script>
```

### 6. Mejores Prácticas de Sitelinks
- Google genera automáticamente sitelinks para sitios con estructura clara.
- Para mejorar la calidad de los sitelinks:
  - Usa títulos de página descriptivos y únicos.
  - Crea una jerarquía de sitio lógica.
  - Asegúrate de que las páginas importantes estén enlazadas desde la navegación.
  - Usa schema `BreadcrumbList` para definir la jerarquía de la página.

### 7. Schema Organization
Agrega schema `Organization` en tu página de inicio para elegibilidad del Panel de Conocimiento:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Corp",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Ayudamos a desarrolladores a construir aplicaciones web optimizadas para SEO.",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-123-4567",
    "contactType": "servicio al cliente"
  },
  "sameAs": [
    "https://twitter.com/examplecorp",
    "https://www.linkedin.com/company/examplecorp",
    "https://www.facebook.com/examplecorp"
  ]
}
</script>
```

### 8. Schema Event
Usa datos estructurados `Event` para páginas de eventos:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Conferencia de SEO Técnico 2025",
  "startDate": "2025-06-15T09:00:00-07:00",
  "endDate": "2025-06-15T17:00:00-07:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "Place",
    "name": "Centro de Convenciones",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Calle Principal 123",
      "addressLocality": "San Francisco",
      "addressRegion": "CA",
      "postalCode": "94105",
      "addressCountry": "US"
    }
  },
  "image": "https://example.com/events/conf-seo-tecnico.jpg",
  "description": "Conferencia anual que cubre lo último en SEO técnico.",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/events/conf-seo-tecnico/boletos",
    "price": "199.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "validFrom": "2025-01-01"
  },
  "organizer": {
    "@type": "Organization",
    "name": "Example Corp",
    "url": "https://example.com"
  }
}
</script>
```

### 9. Schema Speakable (Búsqueda por Voz)
Marca el contenido como adecuado para texto a voz con `speakable`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "¿Qué es el SEO Técnico?",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".resumen-articulo", ".puntos-clave"]
  },
  "url": "https://example.com/blog/que-es-seo-tecnico"
}
</script>
```

### 10. SEO de Entidades mediante `@id` y `sameAs`
Construye confianza de entidad para elegibilidad del Panel de Conocimiento y atribución en IA:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Example Corp",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://www.wikidata.org/wiki/Q12345678",
    "https://www.linkedin.com/company/examplecorp",
    "https://twitter.com/examplecorp",
    "https://www.crunchbase.com/organization/examplecorp",
    "https://www.facebook.com/examplecorp"
  ]
}
</script>
```

**Reglas clave de SEO de Entidades:**
- Usa una URI `@id` persistente (ej., `https://example.com/#organization`) y refiérete a ella de manera consistente en todos los schemas del sitio.
- Enlaza `sameAs` a perfiles autoritativos y verificados (Wikidata es el más fuerte).
- Asegúrate de que el nombre de la marca, el logotipo y la URL sean idénticos en el sitio web, schema y todos los perfiles externos.
- Anida `author` dentro del schema `Article` y referencia una entidad `Person` con su propio `@id`.

```html
<!-- Referencias cruzadas de entidades entre páginas -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Mejores Prácticas SEO 2025",
  "publisher": { "@id": "https://example.com/#organization" },
  "author": {
    "@type": "Person",
    "@id": "https://example.com/#person-jane-smith",
    "name": "Jane Smith",
    "url": "https://example.com/autores/jane-smith",
    "sameAs": [
      "https://www.linkedin.com/in/janesmith",
      "https://twitter.com/janesmith"
    ]
  }
}
</script>
```

### 11. Schema LocalBusiness
Para negocios con ubicaciones físicas:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://example.com/#business",
  "name": "Agencia de Marketing Example",
  "image": "https://example.com/photos/fachada.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Principal 123",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94105",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  "telephone": "+1-555-123-4567",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "priceRange": "$$"
}
</script>
```

### 12. Tipos de Schema Retirados (2025)
Google retiró el soporte de resultados enriquecidos para estos tipos de schema. Elimínalos o despriorízalos:

| Schema Retirado | Estado |
|---|---|
| Book Actions | Ya no genera resultados enriquecidos |
| Course Info | Obsoleto |
| Claim Review | Eliminado |
| Estimated Salary | Eliminado |
| Learning Video | Obsoleto |
| Special Announcement | Eliminado |
| Vehicle Listing | Eliminado |
| Practice Problem | Obsoleto (Enero 2026) |

> **Enfócate en su lugar en schemas de alto impacto:** Organization, Product, Person, LocalBusiness, Article, Event, FAQ, HowTo, Breadcrumb, Video, Review Snippet.

## Verificación
- **Validación JSON-LD:** Pega el resultado en [Google Rich Results Test](https://search.google.com/test/rich-results) o [Schema.org Validator](https://validator.schema.org/).
- **Revisión de contenido:** Verifica si los bloques informativos comienzan con una respuesta directa dentro de las primeras ~50 palabras.
- **Verificación de estructura HTML:** Confirma que se usen elementos `<ul>`, `<ol>` y `<table>` para datos estructurados — no `<p>` con texto separado por comas.
- **Verificación de entidad:** Verifica que `@id` sea consistente en todas las páginas que referencien la misma entidad.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| Errores de "Campo faltante" en Rich Results Test | Propiedades requeridas omitidas (ej., `author`, `datePublished`) | Agrega todas las propiedades requeridas para el `@type` de schema |
| Schema no detectado | Error de sintaxis JSON-LD (comas finales, comillas sin escapar) | Valida el JSON con un linter antes de implementar |
| Sin Featured Snippet a pesar de buen contenido | Respuesta no está en las primeras 40-50 palabras, o no usa HTML estructurado | Reestructura el contenido usando el patrón de pirámide invertida |
| Schema duplicado en la página | Múltiples componentes inyectan el mismo tipo de schema | Centraliza la inyección de schema a nivel de página/layout |
| Panel de Conocimiento no aparece | Baja confianza de entidad, `sameAs` inconsistente | Asegura consistencia de `@id`, `sameAs` y nombre de marca en todos los perfiles |
| Schema retirado no genera resultados enriquecidos | Google eliminó el soporte en 2025 | Elimina schemas retirados, enfócate en tipos de alto impacto |

## Escalamiento
- Si la página requiere un schema anidado complejo (ej., `Product` con `AggregateRating`, `Offer` y `Review`), consulta la [documentación de Schema.org](https://schema.org/) o a un ingeniero SEO humano.
- Si el schema entra en conflicto con datos estructurados generados por el CMS, escala al administrador de la plataforma.
- Para disputas del Panel de Conocimiento, usa el [proceso de reclamo del Panel de Conocimiento](https://support.google.com/knowledgepanel/answer/7534842) de Google.
