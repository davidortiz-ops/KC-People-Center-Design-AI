---
name: seo-images
description: >
  Mejores prácticas para optimizar imágenes y videos para Google Search, Google
  Images y resultados de búsqueda de video: formatos modernos (WebP/AVIF), alt text,
  imágenes responsivas (picture/srcset), lazy loading, sitemaps de imagen/video y
  prevención de CLS. Úsala cuando el usuario diga "optimización de imágenes",
  "imágenes SEO", "alt text", "WebP", "AVIF", "srcset", "Google Images", "video SEO",
  "sitemap de imágenes", o cuando agregue imágenes o videos a una página.
version: 2.0.0
---

# SEO: Imágenes y Video

## Cuándo usarlo
Usa esta skill cuando:
- Agregues imágenes a páginas (imágenes principales, fotos de producto, ilustraciones de blog).
- Incrustes videos (YouTube, autoalojados o reproductores de terceros).
- Optimices para Google Images o resultados de búsqueda de video.
- Crees sitemaps de imágenes o video.
- Implementes imágenes responsivas con `<picture>` y `srcset`.

## Entradas requeridas
- Los tipos de medios en la página (fotos, ilustraciones, infografías, videos).
- Si los videos son autoalojados o incrustados (YouTube, Vimeo).
- La experiencia de búsqueda objetivo (resultados web, Google Images, carrusel de video).
- Formatos de archivo de imagen disponibles (WebP, AVIF, JPEG, PNG).

## Procedimiento

### 1. Optimización de Archivos de Imagen
- Sirve imágenes en formatos modernos: **WebP** o **AVIF** con respaldo JPEG/PNG.
- Comprime imágenes para reducir el tamaño de archivo sin pérdida visible de calidad.
- Usa nombres de archivo descriptivos y ricos en palabras clave (no `IMG_1234.jpg`).

```
✅ /images/zapatillas-running-azules-vista-lateral.webp
❌ /images/IMG_20250115_143022.jpg
❌ /images/photo1.png
```

### 2. Mejores Prácticas HTML para Imágenes
- Cada `<img>` DEBE tener texto `alt` descriptivo.
- Establece `width` y `height` explícitos para prevenir CLS.
- Usa `loading="lazy"` para imágenes que están debajo del pliegue.
- Usa `fetchpriority="high"` para la imagen LCP.

```html
<!-- Imagen principal/LCP -->
<img src="/images/product-hero.webp"
     alt="Zapatillas running rojas con suela acolchada — Nike Air Max"
     width="1200" height="630"
     fetchpriority="high" />

<!-- Imagen debajo del pliegue -->
<img src="/images/product-detail.webp"
     alt="Primer plano de la parte superior de malla transpirable del zapato"
     width="800" height="450"
     loading="lazy" />
```

### 3. Imágenes Responsivas
- Usa `<picture>` con `<source>` para dirección de arte o selección de formato.
- Usa `srcset` para cambio de resolución.

```html
<!-- Selección de formato (AVIF > WebP > JPEG) -->
<picture>
  <source srcset="/images/hero.avif" type="image/avif" />
  <source srcset="/images/hero.webp" type="image/webp" />
  <img src="/images/hero.jpg" alt="Equipo colaborando en la oficina"
       width="1200" height="630" />
</picture>

<!-- Cambio de resolución -->
<img src="/images/product-400.webp"
     srcset="/images/product-400.webp 400w,
             /images/product-800.webp 800w,
             /images/product-1200.webp 1200w"
     sizes="(max-width: 600px) 400px,
            (max-width: 1000px) 800px,
            1200px"
     alt="Foto de producto" width="1200" height="800" loading="lazy" />
```

### 4. Sitemap de Imágenes
- Incluye imágenes importantes en tu sitemap para una mejor descubribilidad.

```xml
<url>
  <loc>https://example.com/products/zapatillas-running</loc>
  <image:image>
    <image:loc>https://example.com/images/zapatillas-azules-running.webp</image:loc>
    <image:caption>Zapatillas running azules con suela acolchada</image:caption>
  </image:image>
</url>
```

### 5. SEO de Video
- Incrusta videos con HTML adecuado — Google necesita descubrir el video en la página.
- Agrega datos estructurados `VideoObject` para resultados enriquecidos de video.
- Proporciona una imagen de miniatura de alta calidad.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Cómo Elegir Zapatillas para Correr",
  "description": "Una guía completa para seleccionar las zapatillas running adecuadas para tu tipo de pie.",
  "thumbnailUrl": "https://example.com/thumbnails/guia-zapatillas-running.jpg",
  "uploadDate": "2025-01-15",
  "duration": "PT5M30S",
  "contentUrl": "https://example.com/videos/guia-zapatillas-running.mp4",
  "embedUrl": "https://www.youtube.com/embed/abc123"
}
</script>
```

### 6. Sitemap de Video
```xml
<url>
  <loc>https://example.com/blog/guia-zapatillas-running</loc>
  <video:video>
    <video:thumbnail_loc>https://example.com/thumbnails/guia.jpg</video:thumbnail_loc>
    <video:title>Cómo Elegir Zapatillas para Correr</video:title>
    <video:description>Una guía completa para seleccionar zapatillas running.</video:description>
    <video:content_loc>https://example.com/videos/guia.mp4</video:content_loc>
    <video:duration>330</video:duration>
  </video:video>
</url>
```

### 7. Evita Antipatrones Comunes en Imágenes
- No incrustes texto importante dentro de imágenes — Google no puede leerlo de forma confiable.
- No uses CSS `background-image` para imágenes de contenido significativo (no indexable).
- No bloquees URLs de imágenes en `robots.txt`.

```css
/* ❌ INCORRECTO — Las imágenes de fondo CSS NO son indexadas por Google Images */
.hero { background-image: url('/images/hero.webp'); }

/* ✅ Usa una etiqueta <img> en su lugar para imágenes indexables */
```

## Verificación
- **Búsqueda en Google Images:** Busca `site:tudominio.com` en Google Images para verificar que las imágenes estén indexadas.
- **Prueba de Resultados Enriquecidos:** Valida el esquema `VideoObject` en [search.google.com/test/rich-results](https://search.google.com/test/rich-results).
- **PageSpeed Insights:** Revisa los puntajes de optimización de imágenes y recomendaciones de formato.
- **Search Console:** Revisa los informes "Videos" e "Imágenes" para problemas de indexación.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| Imágenes no aparecen en Google Images | CSS background-image o imágenes bloqueadas por `robots.txt` | Usa etiquetas `<img>`; permite URLs de imágenes en robots.txt |
| Desplazamientos de diseño de imágenes (CLS) | Atributos `width`/`height` faltantes | Agrega `width` y `height` explícitos a todas las etiquetas `<img>` |
| Video no aparece en resultados de búsqueda | Falta esquema `VideoObject` o miniatura | Agrega `VideoObject` JSON-LD con `thumbnailUrl` |
| Archivos de imagen grandes afectan LCP | JPEG/PNG sin comprimir, sin formatos modernos | Convierte a WebP/AVIF, comprime y usa imágenes responsivas |
| Texto alt faltante | Omisión del desarrollador | Agrega `alt` descriptivo a cada `<img>` |

## Escalamiento
- Si las imágenes requieren un CDN o servicio de transformación de imágenes (Cloudinary, Imgix), consulta a un ingeniero DevOps.
- Si el alojamiento de video requiere DRM o autenticación, escala al equipo de la plataforma de video.

### Referencias
- [Google: Mejores Prácticas de SEO para Imágenes](https://developers.google.com/search/docs/appearance/google-images)
- [Google: Mejores Prácticas para Video](https://developers.google.com/search/docs/appearance/video)
- [Google: Datos Estructurados VideoObject](https://developers.google.com/search/docs/appearance/structured-data/video)
