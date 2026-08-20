---
name: seo-performance
description: >
  Optimización de Core Web Vitals — Largest Contentful Paint (LCP), Cumulative
  Layout Shift (CLS), Interaction to Next Paint (INP) — indexación mobile-first y
  experiencia de página. Reglas prácticas de precarga, fuentes, imágenes, scripts
  y carga diferida. Úsala cuando el usuario diga "Core Web Vitals", "LCP", "CLS",
  "INP", "PageSpeed", "Lighthouse", "página lenta", "layout shift", "rendimiento web",
  "web performance", o cuando depure cargas lentas o desplazamientos de diseño.
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

# SEO: Rendimiento y Core Web Vitals

## Cuándo usarlo
Usa esta skill cuando:
- Construyas u optimices páginas para las señales de ranking Core Web Vitals de Google.
- Depures cargas de página lentas, desplazamientos de diseño o interacciones lentas.
- Agregues fuentes, imágenes, scripts o recursos de terceros.
- Implementes CSS crítico, división de código o estrategias de carga diferida.

## Entradas requeridas
- Puntajes actuales de Lighthouse o PageSpeed Insights (si están disponibles).
- El framework y la estrategia de renderizado (SSR, SSG, CSR).
- Recursos clave en la página (fuentes, imágenes principales, scripts de terceros).

## Procedimiento

### 1. Largest Contentful Paint (LCP) — Objetivo: ≤ 2.5s
- Precarga el elemento LCP (generalmente la imagen principal o el encabezado principal).
- Usa `fetchpriority="high"` en la imagen LCP.
- Sirve imágenes en formatos modernos (WebP, AVIF).
- Incorpora CSS crítico o usa `<link rel="preload">` para hojas de estilo clave.

```html
<!-- Precargar imagen principal -->
<link rel="preload" as="image" href="/hero.webp" fetchpriority="high" />

<!-- Imagen LCP -->
<img src="/hero.webp" alt="Descripción del hero"
     width="1200" height="630" fetchpriority="high" />
```

### 2. Cumulative Layout Shift (CLS) — Objetivo: ≤ 0.1
- Siempre establece `width` y `height` explícitos en imágenes y videos.
- Reserva espacio para anuncios, incrustaciones y contenido cargado dinámicamente.
- Usa `font-display: swap` o `font-display: optional` para prevenir desplazamientos de diseño por carga de fuentes.

```html
<!-- Previene desplazamiento de diseño con dimensiones explícitas -->
<img src="/photo.webp" alt="Descripción" width="800" height="450" loading="lazy" />

<!-- Reserva espacio para un espacio de anuncio -->
<div style="min-height: 250px;">
  <!-- El anuncio se carga aquí -->
</div>
```

```css
/* Previene desplazamiento de diseño por carga de fuentes */
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-display: swap;
}
```

### 3. Interaction to Next Paint (INP) — Objetivo: ≤ 200ms
- Evita tareas de JavaScript de larga duración en el hilo principal.
- Usa `requestIdleCallback` o `setTimeout` para diferir trabajo no crítico.
- Minimiza el impacto de scripts de terceros con `async` o `defer`.

```html
<!-- Diferir scripts no críticos -->
<script src="/analytics.js" defer></script>

<!-- Async para scripts independientes -->
<script src="/chat-widget.js" async></script>
```

### 4. Carga de Fuentes
- Autoaloja las fuentes cuando sea posible.
- Precarga archivos de fuentes críticas.
- Usa `font-display: swap` para evitar texto invisible.

```html
<link rel="preload" as="font" type="font/woff2"
      href="/fonts/inter-var.woff2" crossorigin />
```

### 5. Sugerencias de Recursos
- Usa `<link rel="preconnect">` para orígenes de terceros.
- Usa `<link rel="dns-prefetch">` como respaldo.

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://cdn.example.com" crossorigin />
<link rel="dns-prefetch" href="https://analytics.example.com" />
```

### 6. Indexación Mobile-First
Google utiliza predominantemente la **versión móvil** de tu página para indexación y ranking.

- Usa siempre diseño responsivo con una meta etiqueta viewport.
- Asegura la paridad de contenido — no ocultes contenido importante en móvil.
- No uses carga diferida para contenido principal que requiera interacción del usuario en móvil.
- Los objetivos táctiles deben tener al menos 48×48px con espaciado adecuado.

```html
<!-- Requerido en cada página -->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

```css
/* Asegura que los objetivos táctiles sean suficientemente grandes */
a, button {
  min-height: 48px;
  min-width: 48px;
}
```

> **Crítico:** Si el contenido está oculto mediante CSS `display: none` en móvil, Google puede no indexarlo ya que usa indexación mobile-first.

### 7. Requisito HTTPS
- HTTPS es una señal de ranking confirmada de Google y parte de la Experiencia de Página.
- Sirve siempre todas las páginas a través de HTTPS.
- Evita el contenido mixto (cargar recursos HTTP en páginas HTTPS).

### 8. Intersticiales Intrusivos
Google penaliza las páginas con ventanas emergentes intrusivas que bloquean el contenido en móvil:

- ❌ Ventanas emergentes de pantalla completa antes de que cargue el contenido
- ❌ Intersticiales independientes que el usuario debe descartar
- ✅ Banners de consentimiento de cookies (legalmente requeridos)
- ✅ Diálogos de verificación de edad (legalmente requeridos)
- ✅ Banners pequeños que usan espacio razonable de la pantalla

### 9. Optimización para Google Discover
Para ser elegible en [Google Discover](https://developers.google.com/search/docs/appearance/google-discover):

- Usa imágenes de alta calidad de al menos **1200px de ancho**.
- Establece `max-image-preview:large` en la meta etiqueta robots.
- Proporciona contenido atractivo y oportuno.

```html
<meta name="robots" content="max-image-preview:large" />
```

### 10. CSS `content-visibility` para Rendimiento de Renderizado
Omite el renderizado de contenido fuera de la pantalla para reducir drásticamente la carga inicial y el INP:

```css
/* Aplicar a secciones de contenido fragmentadas debajo del pliegue */
.blog-post,
.comment-section,
.product-card {
  content-visibility: auto;
  contain-intrinsic-size: auto 500px; /* Previene CLS con altura estimada */
}
```

> **Crítico:** Siempre combina `content-visibility: auto` con `contain-intrinsic-size` para prevenir desplazamientos de diseño. A diferencia de `display: none`, el contenido permanece en el árbol de accesibilidad y es buscable.

### 11. Optimización Avanzada de INP
El INP tiene tres fases: **Retardo de Entrada**, **Duración de Procesamiento**, **Retardo de Presentación**.

```javascript
// ✅ Divide tareas largas con scheduler.yield() (moderno)
async function processData(items) {
  for (const item of items) {
    processItem(item);
    // Cede al navegador entre iteraciones
    if (navigator.scheduling?.isInputPending?.()) {
      await scheduler.yield();
    }
  }
}

// ✅ Descarga cálculos pesados a Web Workers
const worker = new Worker('/workers/data-processor.js');
worker.postMessage({ data: largeDataset });
worker.onmessage = (e) => updateUI(e.data);

// ✅ Debounce de eventos de alta frecuencia
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}
window.addEventListener('scroll', debounce(handleScroll, 100));
```

**Reglas clave:**
- Divide tareas que excedan 50ms usando `scheduler.yield()` o `setTimeout()`
- Mueve cálculos pesados a **Web Workers** (fuera del hilo principal)
- Aplica debounce/throttle a eventos `scroll`, `input`, `resize`
- Simplifica la profundidad del DOM — DOMs profundamente anidados causan re-renderizados más lentos
- Usa `requestIdleCallback()` para trabajo no crítico

### 12. API de Reglas de Especulación (Navegación Instantánea)
La API de Reglas de Especulación de Chrome permite transiciones de página casi instantáneas:

```html
<script type="speculationrules">
{
  "prerender": [
    {
      "where": { "href_matches": "/*" },
      "eagerness": "moderate"
    }
  ],
  "prefetch": [
    {
      "where": { "href_matches": "/*" },
      "eagerness": "conservative"
    }
  ]
}
</script>
```

| Eagerness | Cuándo se activa | Mejor para |
|---|---|---|
| `immediate` | Tan pronto como se observa la regla | Páginas siguientes críticas |
| `eager` | Al pasar el cursor (escritorio) o touchstart | Enlaces de alta confianza |
| `moderate` | Después de 200ms de pasar el cursor | Enlaces de navegación |
| `conservative` | Al hacer clic/pointerdown | Enlaces de menor confianza |

> **Impacto SEO:** Las páginas prerrenderizadas se cargan casi instantáneamente, mejorando drásticamente el LCP para navegaciones posteriores.

## Verificación
- **Auditoría Lighthouse:** Ejecuta Lighthouse en Chrome DevTools → Puntaje de rendimiento ≥ 90.
- **PageSpeed Insights:** Prueba la URL en vivo en [pagespeed.web.dev](https://pagespeed.web.dev/).
- **Extensión Web Vitals:** Instala la [extensión de Chrome Web Vitals](https://chrome.google.com/webstore/detail/web-vitals/) para monitoreo en tiempo real.
- **Panel de CrUX:** Revisa los datos de campo en [Chrome UX Report](https://developer.chrome.com/docs/crux/).
- **Panel de Rendimiento de Chrome DevTools:** Perfila interacciones para identificar Tareas Largas que causan problemas de INP.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| LCP > 2.5s | Imagen principal no precargada, imágenes grandes no optimizadas | Agrega `fetchpriority="high"`, convierte a WebP/AVIF, precarga recurso LCP |
| CLS > 0.1 | Imágenes sin dimensiones, anuncios o fuentes de carga tardía | Establece `width`/`height` en todos los medios, reserva espacio para contenido dinámico |
| INP > 200ms | Tareas largas de JavaScript bloqueando el hilo principal | Usa `scheduler.yield()`, Web Workers, debounce en eventos |
| INP > 200ms (DOM) | DOM profundamente anidado con 1000+ elementos | Aplana la estructura del DOM, usa `content-visibility: auto` para secciones fuera de pantalla |
| FOIT (Destello de Texto Invisible) | La carga de fuentes bloquea el renderizado de texto | Usa `font-display: swap` y precarga archivos de fuente |
| CLS por `content-visibility` | Falta `contain-intrinsic-size` | Siempre combina con `contain-intrinsic-size: auto <altura-estimada>` |
| Script de terceros bloqueando | Análisis/anuncios bloqueando el hilo principal | Diferir con `async`/`defer`, carga bajo interacción del usuario |

## Escalamiento
- Si Core Web Vitals requieren cambios de infraestructura (configuración de CDN, tiempos de respuesta del servidor), consulta a un ingeniero DevOps o de plataforma.
- Si los scripts de terceros (anuncios, análisis) son el principal cuello de botella, escala al proveedor o al equipo de operaciones de anuncios.
- Si los problemas de INP persisten a pesar de la optimización, usa la API de LoAF (Long Animation Frames) de Chrome DevTools para un perfilado granular.
