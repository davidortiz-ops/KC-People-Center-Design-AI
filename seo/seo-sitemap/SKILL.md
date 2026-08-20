---
name: seo-sitemap
description: >
  Reglas para sitemaps XML y HTML, archivos de índice de sitemap, sitemaps
  especializados (video, imagen, noticias), prioridad/lastmod y envío de sitemaps a
  Google, Bing e IndexNow. Úsala cuando el usuario diga "sitemap", "sitemap XML",
  "generar sitemap", "índice de sitemap", "sitemap de imágenes", "sitemap de video",
  "IndexNow", "errores de sitemap", o cuando configure o depure el sitemap de un sitio.
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
metadata:
  version: "1.0"
  author: Pragma
---

# SEO: Sitemaps y Gestión de URLs

## Cuándo usarlo
Usa esta skill cuando:
- Configures o depures un sitemap XML para un sitio nuevo.
- Agregues nuevas secciones o tipos de contenido que necesiten entradas en el sitemap.
- Gestiones sitios grandes con 10,000+ URLs que requieran archivos de índice de sitemap.
- Implementes sitemaps especializados (video, imagen, noticias).
- Soluciones errores de sitemap en Google Search Console.
- Envíes sitemaps a Google, Bing o motores con IndexNow habilitado.

## Entradas requeridas
- Lista completa de URLs públicas e indexables del sitio.
- Tipos de contenido presentes (páginas, posts de blog, productos, videos, imágenes, artículos de noticias).
- Jerarquía de prioridad de URLs (qué páginas son más importantes).
- Fechas de última modificación para cada URL (desde CMS o sistema de archivos).
- Dominio del sitio y cualquier subdominio.

## Procedimiento

### 1. Fundamentos del Sitemap XML
- Todo sitio público debería tener un `sitemap.xml` en la raíz.
- Los sitemaps ayudan a los motores de búsqueda a descubrir URLs, especialmente páginas nuevas o huérfanas.
- Los sitemaps son una **pista**, no una directiva — Google puede ignorarlos para páginas de baja calidad.

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

### 2. Límites Técnicos
- **Máximo 50,000 URLs** por archivo de sitemap.
- **Máximo 50MB sin comprimir** por archivo de sitemap.
- Usa **compresión gzip** (`sitemap.xml.gz`) para reducir el ancho de banda.
- Los sitemaps deben estar codificados en UTF-8.
- Las URLs deben estar completamente calificadas (absolutas, con `https://`).

### 3. Archivos de Índice de Sitemap (Sitios Grandes)
Para sitios que exceden 50,000 URLs, usa un archivo de índice de sitemap:

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

> Un índice de sitemap puede referenciar hasta 50,000 sitemaps, dando un máximo teórico de 2.5 mil millones de URLs.

### 4. Qué Incluir (y Excluir)

**Incluir en el sitemap:**
- Todas las páginas canónicas e indexables
- Posts de blog, artículos, landing pages
- Páginas de producto (comercio electrónico)
- Páginas de categoría/taxonomía (si tienen contenido único)
- Páginas de video e imagen (mediante sitemaps especializados)

**Excluir del sitemap:**
- Páginas paginadas (page/2/, page/3/) — canónicas a page/1/
- Variantes de parámetros de URL (`?sort=price`, `?color=red`)
- Páginas de estado de usuario (dashboard, carrito, cuenta, inicio de sesión)
- Páginas de etiquetas/archivo con contenido escaso
- Páginas 404/de error
- URLs redirigidas
- Páginas noindex

### 5. Actualizaciones Dinámicas de `<lastmod>`
- Usa siempre valores dinámicos de `<lastmod>` basados en el contenido.
- Nunca codifiques fechas — se volverán obsoletas.

```jsx
// Ejemplo de generación de sitemap en Next.js
import { getServerSideSitemap } from 'next-sitemap';

export async function GET() {
  const posts = await fetchPosts();
  const entries = posts.map((post) => ({
    loc: `https://example.com/blog/${post.slug}`,
    lastmod: post.updatedAt,  // Dinámico desde la base de datos
    changefreq: 'weekly',
    priority: 0.7,
  }));
  return getServerSideSitemap(entries);
}
```

### 6. Sitemaps de Imágenes
Para mejor descubribilidad en Google Images:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://example.com/products/zapatillas-running</loc>
    <image:image>
      <image:loc>https://example.com/images/zapatillas-azules-running.webp</image:loc>
      <image:caption>Zapatillas running azules con suela acolchada</image:caption>
      <image:geo_location>San Francisco, California</image:geo_location>
      <image:title>Zapatillas Running Azules - Vista Lateral</image:title>
      <image:license>https://example.com/licencia</image:license>
    </image:image>
  </url>
</urlset>
```

### 7. Sitemaps de Video
Para mejor descubribilidad en búsqueda de video:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://example.com/blog/guia-zapatillas-running</loc>
    <video:video>
      <video:thumbnail_loc>https://example.com/thumbnails/guia.jpg</video:thumbnail_loc>
      <video:title>Cómo Elegir Zapatillas para Correr</video:title>
      <video:description>Una guía completa para seleccionar zapatillas running.</video:description>
      <video:content_loc>https://example.com/videos/guia.mp4</video:content_loc>
      <video:duration>330</video:duration>
      <video:publication_date>2025-01-15</video:publication_date>
      <video:family_friendly>yes</video:family_friendly>
    </video:video>
  </url>
</urlset>
```

### 8. Sitemaps de Noticias (Google News)
Para sitios elegibles para Google News:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url>
    <loc>https://example.com/noticias/actualizacion-seo-tecnico</loc>
    <news:news>
      <news:publication>
        <news:name>Example Times</news:name>
        <news:language>es</news:language>
      </news:publication>
      <news:publication_date>2025-01-15</news:publication_date>
      <news:title>Google Actualiza los Requisitos de SEO Técnico</news:title>
      <news:keywords>SEO, Google, actualización de búsqueda</news:keywords>
    </news:news>
  </url>
</urlset>
```

### 9. Envío de Sitemaps

**Google Search Console:**
```
1. Ve a Search Console > Sitemaps
2. Ingresa la URL del sitemap: https://example.com/sitemap.xml
3. Haz clic en Enviar
```

**Bing Webmaster Tools:**
```
1. Ve a Bing Webmaster Tools > Sitemaps
2. Ingresa la URL del sitemap
3. Haz clic en Enviar
```

**Referencia en robots.txt (descubrimiento automático):**
```txt
Sitemap: https://example.com/sitemap.xml
Sitemap: https://example.com/sitemap-noticias.xml
```

**IndexNow (Bing, Yandex, Naver, Seznam):**
```bash
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

### 10. Hreflang en Sitemaps
Para sitios multilingües, incluye anotaciones hreflang en los sitemaps:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/es/acerca-de</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/about" />
    <xhtml:link rel="alternate" hreflang="es" href="https://example.com/es/acerca-de" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/a-propos" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/en/about" />
  </url>
</urlset>
```

### 11. Sitemaps HTML (Para Usuarios)
Un sitemap HTML es una página que enumera enlaces a todas las páginas importantes de tu sitio, formateada para humanos.

```
✅ Ayuda a los usuarios a encontrar contenido
✅ Proporciona enlaces internos (ayuda al rastreo)
❌ No es un reemplazo del sitemap XML
```

```html
<!-- Ejemplo de estructura de sitemap HTML -->
<nav aria-label="Sitemap">
  <h2>Páginas</h2>
  <ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about">Acerca de</a></li>
    <li><a href="/services">Servicios</a></li>
  </ul>
  <h2>Blog</h2>
  <ul>
    <li><a href="/blog/guia-seo">Guía SEO</a></li>
    <li><a href="/blog/rendimiento">Consejos de Rendimiento</a></li>
  </ul>
</nav>
```

### 12. Antipatrones Comunes de Sitemap

```xml
<!-- ❌ INCORRECTO — Incluir páginas noindex en el sitemap -->
<url>
  <loc>https://example.com/dashboard</loc>
</url>

<!-- ❌ INCORRECTO — URLs relativas -->
<url>
  <loc>/blog/post</loc>
</url>

<!-- ❌ INCORRECTO — IDs de sesión o parámetros de seguimiento -->
<url>
  <loc>https://example.com/product?sid=abc123</loc>
</url>

<!-- ✅ CORRECTO — URL limpia, absoluta y canónica -->
<url>
  <loc>https://example.com/product/zapatos-azules</loc>
</url>
```

## Verificación
- **Search Console:** Revisa el informe de Sitemaps para errores, advertencias y recuento indexado.
- **Validación de sitemap:** Usa [xml-sitemaps.com/validate-xml-sitemap](https://www.xml-sitemaps.com/validate-xml-sitemap) o validadores similares.
- **Verificación de robots.txt:** Confirma que las URLs del sitemap estén listadas y sean accesibles.
- **Inspección de URL:** Verifica URLs individuales del sitemap usando la herramienta de Inspección de URLs de Search Console.
- **Verificación de cobertura:** Asegúrate de que las URLs del sitemap coincidan con el recuento real de páginas indexables del sitio.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| El sitemap devuelve 404 | Ruta incorrecta o no generado durante la compilación | Verifica que el pipeline de compilación genere sitemap.xml en la raíz |
| Errores de sitemap en Search Console | XML mal formado o codificación de URL inválida | Valida la sintaxis XML y la codificación de URLs |
| URLs en el sitemap no indexadas | Baja calidad de contenido o sin enlaces internos | Mejora las señales E-E-A-T y el enlazado interno |
| Fechas `<lastmod>` obsoletas | Fechas codificadas en lugar de dinámicas | Usa marcas de tiempo de última modificación del contenido desde CMS/base de datos |
| Presupuesto de rastreo desperdiciado en URLs de bajo valor | Paginación, filtros, etiquetas en el sitemap | Excluye URLs no canónicas y de contenido escaso |
| Sitemap demasiado grande | Más de 50,000 URLs o 50MB | Divide en múltiples sitemaps y usa índice de sitemap |
| Imágenes/videos no aparecen en búsqueda | Falta sitemap de imagen/video | Agrega sitemaps especializados con metadatos requeridos |

## Escalamiento
- Si el plugin del CMS genera sitemaps automáticamente con URLs incorrectas, escala al administrador del CMS.
- Para sitios con 100,000+ URLs, consulta a un ingeniero SEO humano para la estrategia de sitemap y gestión del presupuesto de rastreo.
- Si existen problemas persistentes de indexación a pesar de tener sitemaps válidos, el problema probablemente es de autoridad de contenido, no técnico.
