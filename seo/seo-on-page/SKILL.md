---
name: seo-on-page
description: >
  Implementación y auditoría de meta tags on-page: title tags, meta descriptions,
  Open Graph, Twitter Cards, canonical, favicon, theme-color, optimización para
  Google Discover y control de title link. Úsala cuando el usuario diga "meta tags",
  "title tag", "meta description", "Open Graph", "og:image", "Twitter Card",
  "vista previa social", "social preview", "Google Discover", "favicon", o cuando
  configure el <head> de páginas nuevas o corrija meta tags faltantes o duplicados.
version: 2.0.0
license: Proprietary - Pragma (uso interno y confidencial)
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
  - WebSearch
metadata:
  version: "1.0"
  author: Pragma
---

# SEO: Meta Tags y Open Graph

## Cuándo usarlo
Usa esta skill cuando:
- Crees páginas nuevas que necesiten aparecer en resultados de búsqueda.
- Optimices vistas previas de uso compartido en redes sociales (Facebook, Twitter/X, LinkedIn, Slack).
- Configures meta tags dinámicos para sitios con CMS o páginas plantilladas.
- Audites o corrijas meta tags faltantes o duplicados.

## Entradas requeridas
- El título de la página y una descripción concisa (150-160 caracteres).
- Una imagen representativa para compartir en redes sociales (1200×630px recomendado).
- La URL canónica de la página.
- El nombre del sitio y el usuario de Twitter (si aplica).

## Procedimiento

### 1. Etiqueta Title
- Cada página DEBE tener un `<title>` único.
- Mantén los títulos por debajo de 60 caracteres para evitar truncamiento en SERPs.
- Usa el formato: `Palabra Clave Principal — Palabra Clave Secundaria | Nombre de Marca`.

```html
<title>Guía Completa de SEO Técnico | Example Corp</title>
```

**Ejemplos de meta títulos optimizados** (patrón: keyword principal al inicio, marca o ubicación al final, modificadores que aumentan el CTR):

| Palabra clave | Meta título |
|---------------|-------------|
| catálogo de productos Ikea | Descarga el catálogo de productos Ikea para Colombia |
| ropa para senderismo | Tienda de ropa para senderismo - Decathlon Colombia |
| Licencia para volar drones | Licencia para volar drones en Colombia: Nueva ley 2024 |
| Productos para bebés | Productos para Bebés: carritos, sillas, cunas y más |
| Comprar vino de marca | Comprar vino de marca online \| Tienda de vino Carrefour |
| Tenis deportivos para mujer | Tenis deportivos para mujer - Envíos gratis en Colombia |
| Presupuesto SEO | Presupuesto SEO: todo lo que necesitas saber - Semrush |
| Ventajas del iPhone 14 Pro Max | Ventajas del iPhone 14 Pro Max vs iPhone 15 - Apple |

> Patrones que destacan: incluir el modificador de intención ("comprar", "online", "envíos gratis"), el año para frescura ("2024"), la comparación ("vs"), o el formato de lista ("carritos, sillas, cunas y más"), siempre cerrando con la marca o la ubicación.

### 2. Meta Description
- Cada página DEBE tener un `<meta name="description">` único.
- Mantén las descripciones entre 120-160 caracteres.
- Incluye una propuesta de valor clara y un llamado a la acción cuando sea apropiado.

```html
<meta name="description" content="Aprende las mejores prácticas de SEO técnico incluyendo Core Web Vitals, datos estructurados y optimización de rastreo. Actualizado para 2025." />
```

**Ejemplos de meta descripciones optimizadas** (incluyen la keyword de forma natural, una propuesta de valor y un CTA; longitud ~120-160 caracteres):

| Palabra clave | Meta descripción | Caracteres |
|---------------|------------------|:----------:|
| cómo hacer el tono de voz para mi marca | Aprende a desarrollar un tono de voz para tu marca y a usarlo con trucos rápidos y fáciles. Utiliza nuestra plantilla. Descárgala gratis aquí. | 151 |
| collares para perros | Collares para perros de todos los tamaños. Encuentra collares y otros accesorios para tus mascotas en nuestra tienda online. ¡Tenemos ofertas! | 154 |
| zapatos para senderismo | Encuentra los mejores zapatos para senderismo o trekking en Colombia. Vive tu próxima aventura con nosotros. Envíos gratis a todo el país. | 155 |
| practicar inglés gratis | Practica gratis tu inglés escrito con Cambridge Academy. Recibe feedback sobre lo que escribes en segundos y aprende cómo mejorar. ¡Empieza ya! | 153 |
| qué es inbound marketing | El inbound marketing es una metodología comercial para captar clientes mediante contenido de valor. Aquí te enseñamos a usarla en tu negocio. | 149 |
| CRMs para empresas pequeñas | Descubre 7 opciones de software de CRM para empresas pequeñas y cómo pueden ayudarte a retener clientes y aumentar tus ventas. | 155 |

> Cada descripción abre con la keyword, comunica un beneficio concreto y cierra con un llamado a la acción ("Descárgala gratis", "Envíos gratis", "¡Empieza ya!").

### 3. Etiquetas Open Graph (Facebook, LinkedIn, Slack)
- Requeridas para vistas previas enriquecidas al compartir en redes sociales.

```html
<meta property="og:type" content="website" />
<meta property="og:title" content="Guía Completa de SEO Técnico" />
<meta property="og:description" content="Aprende las mejores prácticas de SEO técnico incluyendo Core Web Vitals, datos estructurados y optimización de rastreo." />
<meta property="og:image" content="https://example.com/images/og-guia-seo.png" />
<meta property="og:url" content="https://example.com/blog/seo-tecnico" />
<meta property="og:site_name" content="Example Corp" />
```

### 4. Etiquetas Twitter Card
- Usa `summary_large_image` para contenido de artículos/blogs.

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Guía Completa de SEO Técnico" />
<meta name="twitter:description" content="Aprende las mejores prácticas de SEO técnico incluyendo Core Web Vitals, datos estructurados y optimización de rastreo." />
<meta name="twitter:image" content="https://example.com/images/og-guia-seo.png" />
<meta name="twitter:site" content="@examplecorp" />
```

### 5. Plantilla Completa del Head

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Título de Página | Marca</title>
  <meta name="description" content="Descripción de página menor a 160 caracteres." />
  <link rel="canonical" href="https://example.com/pagina-actual" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Título de Página" />
  <meta property="og:description" content="Descripción de página." />
  <meta property="og:image" content="https://example.com/og-image.png" />
  <meta property="og:url" content="https://example.com/pagina-actual" />
  <meta property="og:site_name" content="Nombre de Marca" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Título de Página" />
  <meta name="twitter:description" content="Descripción de página." />
  <meta name="twitter:image" content="https://example.com/og-image.png" />
</head>
```

### 6. Ejemplos en Frameworks

```jsx
// Next.js App Router (exportación de metadata)
export const metadata = {
  title: 'Título de Página | Marca',
  description: 'Descripción de página menor a 160 caracteres.',
  openGraph: {
    title: 'Título de Página',
    description: 'Descripción de página.',
    images: [{ url: 'https://example.com/og-image.png', width: 1200, height: 630 }],
    url: 'https://example.com/pagina-actual',
    siteName: 'Nombre de Marca',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Título de Página',
    description: 'Descripción de página.',
    images: ['https://example.com/og-image.png'],
  },
};
```

### 7. Favicon en Resultados de Búsqueda
- Google muestra favicons en resultados de búsqueda móvil y de escritorio junto al nombre del sitio.
- Proporciona un favicon para el reconocimiento de marca en SERPs.

```html
<link rel="icon" href="/favicon.ico" sizes="48x48" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
```

> Requisitos de Google: el favicon debe ser múltiplo de 48×48px, accesible para Googlebot (no bloqueado por robots.txt) y visualmente representativo de tu marca.

### 8. Nombre del Sitio en Resultados de Búsqueda
- Usa datos estructurados `WebSite` para controlar el nombre del sitio que se muestra en los resultados de búsqueda.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Example Corp",
  "alternateName": "EC",
  "url": "https://example.com"
}
</script>
```

### 9. Fechas de Publicación y Autoría
- Google puede mostrar fechas de artículos en los resultados de búsqueda.
- Usa datos estructurados (`datePublished`, `dateModified`) y fechas visibles en la página.

```html
<!-- Fecha visible en la página -->
<time datetime="2025-01-15">15 de enero de 2025</time>

<!-- En JSON-LD de Article -->
"datePublished": "2025-01-15T08:00:00+00:00",
"dateModified": "2025-02-01T10:30:00+00:00"
```

> Google recomienda mostrar una fecha visible en la página que coincida con los datos estructurados. No cambies `dateModified` sin cambios significativos en el contenido.

### 10. Optimización para Google Discover
Para ser elegible en [Google Discover](https://developers.google.com/search/docs/appearance/google-discover):

- Usa imágenes de alta calidad y atractivas de al menos **1200px de ancho**.
- Habilita vistas previas de imágenes grandes con la meta etiqueta `max-image-preview`.
- Crea contenido oportuno y atractivo (Discover favorece temas de tendencia).

```html
<!-- Requerido para elegibilidad en Google Discover -->
<meta name="robots" content="max-image-preview:large" />
```

> **Nota:** Sin `max-image-preview:large`, Google puede no mostrar tu contenido con vistas previas de imagen grande en Discover.

### 11. Mejores Prácticas para Title Link
Según la [documentación de title link de Google](https://developers.google.com/search/docs/appearance/title-link), Google puede reescribir tu etiqueta `<title>` en SERPs. Para evitar reescrituras no deseadas:

- Haz los títulos descriptivos y concisos (menos de 60 caracteres).
- No uses títulos con relleno de palabras clave, genéricos o vagos.
- No uses el mismo título para múltiples páginas.
- Refleja con precisión el contenido de la página.
- Incluye el nombre de la marca al final, no al principio.

### 12. Color del Tema
- Usa la meta etiqueta `theme-color` para personalizar la interfaz del navegador.

```html
<meta name="theme-color" content="#1a1a2e" />
```

## Verificación
- **Vista previa en SERP de Google:** Usa [mangools.com/free-seo-tools/serp-simulator](https://mangools.com/free-seo-tools/serp-simulator) para previsualizar cómo aparecen el título y la descripción.
- **Vista previa social:** Usa [opengraph.xyz](https://www.opengraph.xyz/) para probar el renderizado de Open Graph.
- **Vista previa de Twitter:** Usa [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator) para probar el renderizado de Twitter Card.
- **Verificación de unicidad:** Asegúrate de que no haya dos páginas que compartan el mismo título o descripción.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| Título truncado en SERPs | El título excede 60 caracteres | Acorta el título; pon las palabras clave más importantes primero |
| Compartir en redes muestra imagen incorrecta | Falta `og:image` o dimensiones incorrectas | Agrega `og:image` con imagen de 1200×630px usando URL absoluta |
| Meta descriptions duplicados | La plantilla no personaliza por página | Usa generación dinámica de meta desde el contenido de la página o campos del CMS |
| Descripción no se muestra en Google | Google reescribe descripciones por relevancia | Escribe descripciones que coincidan directamente con consultas de búsqueda comunes |

## Escalamiento
- Si el CMS genera meta tags automáticamente que entran en conflicto con las sobrescrituras manuales, escala al administrador del CMS.
- Si las plataformas sociales almacenan en caché vistas previas antiguas, usa sus respectivas herramientas de depuración/validador para forzar un nuevo rastreo.
