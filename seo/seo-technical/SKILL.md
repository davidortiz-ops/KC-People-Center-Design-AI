---
name: seo-technical
description: >
  Reglas de rastreo e indexación: canonicalización, prevención de contenido
  duplicado, directivas robots (robots.txt y meta robots), automatización de sitemaps,
  gestión de rastreadores de IA y códigos de estado HTTP. Úsala cuando el usuario diga
  "rastreo", "indexación", "robots.txt", "meta robots", "noindex", "canonical",
  "contenido duplicado", "crawl", "indexación mobile-first", o cuando cree rutas/URLs
  nuevas, migre URLs o defina la estrategia de canonicalización de un sitio.
version: 2.0.0
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
---

# SEO: Rastreo e Indexación

## Cuándo usarlo
Usa esta skill cuando:
- Crees nuevas rutas, páginas o segmentos de URL dinámicos.
- Gestiones páginas de estado de usuario (dashboards, configuraciones, carritos, áreas de cuenta).
- Configures reglas de indexación o estrategia de canonicalización.
- Configures, modifiques o depures sitemaps XML.
- Implementes un sitio nuevo o migres URLs.

## Entradas requeridas
- El dominio del sitio y la estructura de URLs.
- Qué páginas son públicas vs. privadas/de estado de usuario.
- El mecanismo de enrutamiento del framework (basado en archivos, basado en configuración, dinámico).
- Si el sitio usa SSR, SSG o CSR.

## Procedimiento

### 1. Canonicalización
- Cada página pública DEBE incluir una etiqueta canónica autorreferenciada en el `<head>`.
- Usa la URL absoluta incluyendo el protocolo y el dominio.

```html
<!-- En la página: https://example.com/blog/guia-seo -->
<head>
  <link rel="canonical" href="https://example.com/blog/guia-seo" />
</head>
```

```jsx
// Ejemplo en Next.js
export const metadata = {
  alternates: {
    canonical: 'https://example.com/blog/guia-seo',
  },
};
```

### 2. Directivas Robots
- Las páginas privadas o de estado de usuario NO deben ser indexadas.
- Inyecta `noindex, nofollow` en el `<head>` para estas rutas.

```html
<!-- Páginas de dashboard, carrito, configuraciones, cuenta -->
<meta name="robots" content="noindex, nofollow" />
```

- Para reglas de rastreo a nivel de sitio, mantén un archivo `robots.txt`:

```txt
# robots.txt
User-agent: *
Allow: /
Disallow: /dashboard/
Disallow: /cart/
Disallow: /account/
Sitemap: https://example.com/sitemap.xml
```

- **Cabecera HTTP X-Robots-Tag:** Úsala para archivos no HTML (PDFs, imágenes) o cuando no puedas agregar meta tags.

```http
# Cabecera de respuesta HTTP
X-Robots-Tag: noindex, nofollow
```

| Método | Cuándo usarlo |
|---|---|
| `<meta name="robots">` | Páginas HTML — más común |
| Cabecera `X-Robots-Tag` | PDFs, imágenes o recursos no HTML |
| `robots.txt Disallow` | Prevenir rastreo (pero NO indexación) |

### 3. Automatización de Sitemap
- Asegúrate de que todas las rutas públicas estén incluidas en `sitemap.xml`.
- Incluye etiquetas `<lastmod>` con fechas ISO 8601.
- Excluye rutas privadas, duplicados de paginación y páginas de utilidad.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2025-01-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/blog/guia-seo</loc>
    <lastmod>2025-01-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

### 4. Archivos de Índice de Sitemap (Sitios Grandes)
Para sitios con más de 50,000 URLs, usa un archivo de índice de sitemap:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-paginas.xml</loc>
    <lastmod>2025-01-15</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-blog.xml</loc>
    <lastmod>2025-01-10</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-productos.xml</loc>
    <lastmod>2025-01-12</lastmod>
  </sitemap>
</sitemapindex>
```

> **Límites:** Cada archivo de sitemap puede contener máximo 50,000 URLs y debe estar por debajo de 50MB sin comprimir. Un índice de sitemap puede referenciar hasta 50,000 sitemaps.

### 5. Calificación de Enlaces Salientes
- Usa atributos `rel` para indicar a Google tu relación con las páginas enlazadas.
- Los enlaces editoriales regulares no necesitan ningún atributo `rel`.

```html
<!-- Enlace patrocinado/de pago -->
<a rel="sponsored" href="https://partner.com/product">Producto de Socio</a>

<!-- Contenido generado por usuario (comentarios, foros) -->
<a rel="ugc" href="https://example.com/post-usuario">Post del usuario</a>

<!-- No pasar PageRank / no asociar -->
<a rel="nofollow" href="https://example.com/no-confiable">Enlace externo</a>

<!-- Combinar múltiples valores -->
<a rel="ugc nofollow" href="https://example.com/enlace-comentario">Enlace de comentario</a>
```

| Valor `rel` | Cuándo usarlo |
|---|---|
| `sponsored` | Anuncios, ubicaciones pagadas, enlaces de afiliados |
| `ugc` | Contenido generado por usuario (comentarios, posts de foro) |
| `nofollow` | No quieres respaldar ni pasar PageRank al enlace |

### 6. Directivas de Control de Snippets
- Controla cómo Google muestra tu contenido en los snippets de resultados de búsqueda.
- Usa `data-nosnippet` para excluir texto específico de los snippets.

```html
<!-- Controlar longitud del snippet y tamaño de vista previa de imagen -->
<meta name="robots" content="max-snippet:160, max-image-preview:large" />

<!-- Excluir texto específico de aparecer en snippets -->
<p>Este texto puede aparecer en snippets.</p>
<p data-nosnippet>Este texto NO aparecerá en snippets de Google.</p>
```

| Directiva | Efecto |
|---|---|
| `max-snippet:N` | Limita el snippet de texto a N caracteres |
| `max-image-preview:large` | Permite vistas previas de imagen grandes (none, standard, large) |
| `max-video-preview:N` | Limita la vista previa de video a N segundos (-1 = sin límite) |
| `nosnippet` | No mostrar ningún snippet |
| `data-nosnippet` | Excluir elementos HTML específicos de los snippets |

### 7. Códigos de Estado HTTP y Búsqueda de Google
- Usa códigos de estado HTTP correctos — afectan directamente cómo Google trata tus páginas.

| Código de Estado | Comportamiento de Google |
|---|---|
| `200` | La página se rastrea y es elegible para indexación |
| `301` | Redirección permanente — PageRank se transfiere a la nueva URL |
| `302` | Redirección temporal — la URL original permanece en el índice |
| `404` / `410` | Página eliminada del índice (410 es más rápido) |
| `503` | Indisponibilidad temporal — Google reintenta más tarde |
| `429` | Demasiadas solicitudes — Google reduce la velocidad de rastreo |

### 8. Protocolo IndexNow (Motores No Google)
IndexNow proporciona descubrimiento instantáneo de URLs para Bing, Yandex, Naver y Seznam.cz. **Google NO soporta IndexNow.**

```bash
# Notificar a Bing sobre una URL nueva/actualizada
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "example.com",
    "key": "tu-clave-api",
    "urlList": [
      "https://example.com/pagina-nueva",
      "https://example.com/pagina-actualizada"
    ]
  }'
```

| Motor | Soporte IndexNow | Alternativa para Google |
|---|---|---|
| **Bing** | ✅ Soportado | — |
| **Yandex** | ✅ Soportado | — |
| **Naver** | ✅ Soportado | — |
| **Google** | ❌ No soportado | Usa sitemaps + Search Console + enlazado interno |

### 9. Indexación Selectiva de Google
La indexación de Google ahora es selectiva — no todas las URLs se indexan:

- El contenido debe cumplir con los estándares E-E-A-T para justificar el "costo computacional" de la indexación.
- Las páginas huérfanas (sin enlaces internos) tienen significativamente menos probabilidad de ser indexadas.
- Las páginas con contenido escaso, duplicado o de bajo valor pueden ser descubiertas pero no indexadas.
- Enfócate en: contenido de alta calidad + enlazado interno adecuado + inclusión en sitemap.

> **Si las páginas no se están indexando:** Rara vez es un problema técnico que se pueda resolver con un push de API. Casi siempre es un problema de calidad de contenido o autoridad del sitio.

### 10. Gestión de Rastreadores de IA
Gestiona los rastreadores de IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) mediante robots.txt:

```txt
# robots.txt — Gestión de rastreadores de IA

# Permitir Google AI Overviews (Google-Extended) si se desea
User-agent: Google-Extended
Allow: /

# Bloquear OpenAI del rastreo
User-agent: GPTBot
Disallow: /

# Bloquear Anthropic Claude
User-agent: ClaudeBot
Disallow: /

# Permitir Perplexity (o bloquear si se desea)
User-agent: PerplexityBot
Allow: /
```

| Rastreador de IA | Token robots.txt | Propósito |
|---|---|---|
| Google-Extended | `Google-Extended` | Google AI Overviews, Vertex AI |
| GPTBot | `GPTBot` | Datos de entrenamiento de OpenAI GPT |
| ClaudeBot | `ClaudeBot` | Datos de entrenamiento de Anthropic Claude |
| PerplexityBot | `PerplexityBot` | Búsqueda de Perplexity AI |
| CCBot | `CCBot` | Common Crawl / Entrenamiento de IA |

### 11. HTML Semántico y Enlaces Rastreables
Según la [guía oficial de Google](https://developers.google.com/search/docs/crawling-indexing/links-crawlable), solo los siguientes patrones de enlace son confiablemente rastreables:

```html
<!-- ✅ Rastreable por Google -->
<a href="/page">Texto del enlace</a>
<a href="/page">
  <img src="/img.webp" alt="Enlace de imagen" />
</a>

<!-- ❌ NO confiablemente rastreable -->
<a routerLink="/page">Angular routerLink sin href</a>
<span onclick="location='/page'">Manejador JS de clic</span>
<a href="javascript:goTo('/page')">JavaScript href</a>
```

> **Regla clave de Google:** Googlebot solo sigue enlaces en elementos `<a>` con un atributo `href` que se resuelva a una URL.

## Verificación
- **Inspección de rutas:** Asegúrate de que cada página pública tenga una etiqueta canónica autorreferenciada válida.
- **Validación de código fuente:** Verifica que las rutas privadas/de estado de usuario contengan `noindex, nofollow`.
- **Verificación de robots.txt:** Confirma que `robots.txt` exista, permita rutas públicas y bloquee las privadas.
- **Validación de sitemap:** Asegúrate de que `sitemap.xml` se compile correctamente, contenga solo URLs públicas y actualice dinámicamente `<lastmod>`.
- **Cobertura de indexación:** Monitorea el informe "Páginas" de Google Search Console para problemas de indexación.
- **IndexNow:** Si está implementado, verifica que el archivo de clave sea accesible en `https://example.com/{clave}.txt`.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| Penalización por contenido duplicado | Etiquetas canónicas faltantes o incorrectas | Agrega `<link rel="canonical">` autorreferenciado a cada página pública |
| Páginas privadas aparecen en búsqueda | Falta meta etiqueta `noindex` | Agrega `<meta name="robots" content="noindex, nofollow" />` |
| El sitemap devuelve 404 | No generado durante la compilación o ruta incorrecta | Verifica que el pipeline de compilación genere `sitemap.xml` en la raíz |
| Fechas `<lastmod>` obsoletas | Fechas codificadas en lugar de valores dinámicos | Usa marcas de tiempo de última modificación del contenido desde CMS o sistema de archivos |
| Desperdicio de presupuesto de rastreo | Demasiadas URLs de bajo valor en el sitemap | Excluye paginación, filtros y páginas de utilidad del sitemap |
| Páginas descubiertas pero no indexadas | Baja calidad de contenido o sin enlaces internos | Mejora señales E-E-A-T, agrega enlaces internos, asegura valor único |
| X-Robots-Tag no funciona | Cabecera no configurada en la respuesta del servidor | Verifica con `curl -I <URL>` que la cabecera aparezca en la respuesta |
| Rastreadores de IA extrayendo contenido | Sin directivas de rastreador en robots.txt | Agrega reglas específicas de User-agent para GPTBot, ClaudeBot, etc. |

## Escalamiento
- Si el sitio tiene miles de URLs dinámicas y el presupuesto de rastreo es un problema, consulta a un ingeniero SEO humano para la estrategia de paginación y archivos de índice de sitemap.
- Si las etiquetas canónicas entran en conflicto con las canónicas generadas por el CMS, escala al administrador de la plataforma.
- Si existen problemas persistentes de indexación a pesar de tener contenido de calidad, usa la herramienta de Inspección de URLs de Search Console y solicita indexación manualmente.
