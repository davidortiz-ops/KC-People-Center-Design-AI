<!-- Actualizado: 2026-02-07 -->
# Umbrales de Core Web Vitals (febrero 2026)

## Métricas actuales

| Métrica | Bueno | Mejorable | Deficiente |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5s–4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 |

## Datos clave
- INP reemplazó a FID (First Input Delay) el **12 de marzo de 2024**. FID se eliminó por completo de todas las herramientas de Chrome (CrUX API, PageSpeed Insights, Lighthouse) el **9 de septiembre de 2024**. INP es la única métrica de interactividad.
- La evaluación usa el **percentil 75** de datos de usuarios reales (datos de campo de CrUX).
- Google evalúa a **nivel de página** y a **nivel de origen**.
- Core Web Vitals es una señal de ranking de **desempate** — importa más cuando la calidad de contenido es similar entre competidores.
- **Los umbrales no han cambiado desde sus definiciones originales** — ignora las afirmaciones de "umbrales más estrictos" de los blogs de SEO.
- La actualización core de diciembre 2025 pareció ponderar **más fuertemente los CWV móviles**.
- A octubre de 2025: el **57.1%** de los sitios de escritorio y el **49.7%** de los móviles aprueban las tres CWV.

## Subpartes de LCP (añadidas a CrUX en febrero 2025)

LCP ahora puede desglosarse en subpartes de diagnóstico:

| Subparte | Qué mide | Objetivo |
|---------|------------------|--------|
| **TTFB** | Time to First Byte (respuesta del servidor) | <800ms |
| **Resource Load Delay** | Tiempo desde TTFB hasta el inicio de la solicitud del recurso | Minimizar |
| **Resource Load Time** | Tiempo para descargar el recurso LCP | Depende del tamaño |
| **Element Render Delay** | Tiempo desde recurso cargado hasta renderizado | Minimizar |

**LCP total = TTFB + Resource Load Delay + Resource Load Time + Element Render Delay**

Usa este desglose para identificar qué fase está causando los problemas de LCP.

## Soft Navigations API (experimental)

**Origin Trial de Chrome 139+ (julio 2025)** — Primer paso hacia la medición de CWV en SPAs.

- Aborda el antiguo punto ciego de medición en SPAs
- Actualmente experimental, **aún sin impacto en ranking**
- Detecta "soft navigations" (cambios de URL sin recarga completa de página)
- Puede afectar la futura medición de CWV en SPAs

**Detección:** Verifica frameworks SPA (React, Vue, Angular, Svelte) y advierte sobre las limitaciones actuales de medición de CWV.

## Fuentes de medición

### Datos de campo (usuarios reales)
- Chrome User Experience Report (CrUX)
- PageSpeed Insights (usa datos de CrUX)
- Reporte de Core Web Vitals de Search Console

### Datos de laboratorio (simulados)
- Lighthouse
- WebPageTest
- Chrome DevTools

> Los datos de campo son los que Google usa para el ranking. Los datos de laboratorio son útiles para depurar.

## Cuellos de botella comunes

### LCP (Largest Contentful Paint)
- Imágenes hero sin optimizar (comprimir, usar WebP/AVIF, agregar preload)
- CSS/JS que bloquean el renderizado (defer, async, inline de CSS crítico)
- Respuesta lenta del servidor (TTFB >200ms — usar CDN en el edge, caché)
- Scripts de terceros que bloquean (diferir analytics, widgets de chat)
- Retraso en la carga de fuentes web (usar font-display: swap + preload)

### INP (Interaction to Next Paint)
- Tareas largas de JavaScript en el hilo principal (dividir en tareas menores <50ms)
- Manejadores de eventos pesados (debounce, usar requestAnimationFrame)
- DOM excesivo (>1.500 elementos es preocupante)
- Scripts de terceros que secuestran el hilo principal
- Operaciones síncronas de XHR o localStorage
- Layout thrashing (múltiples reflows forzados)

### CLS (Cumulative Layout Shift)
- Imágenes/iframes sin dimensiones width/height
- Contenido inyectado dinámicamente encima del contenido existente
- Fuentes web que causan desplazamiento de diseño (usar font-display: swap + preload)
- Anuncios/embeds sin espacio reservado
- Contenido de carga tardía que empuja la página hacia abajo

## Prioridad de optimización

1. **LCP** — El de mayor impacto en el rendimiento percibido
2. **CLS** — El problema más común que afecta la experiencia de usuario
3. **INP** — El que más importa para aplicaciones interactivas

## Herramientas

```bash
# PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=API_KEY"

# Lighthouse CLI
npx lighthouse URL --output json --output-path report.json
```

## Actualizaciones de herramientas de rendimiento (2025)

- **Lighthouse 13.0** (octubre 2025): Reestructuración importante de auditorías con categorías de rendimiento reorganizadas y pesos de puntuación actualizados. Lighthouse es una herramienta de laboratorio (condiciones simuladas) — siempre contrasta con los datos de campo de CrUX para el rendimiento del mundo real.
- **CrUX Vis** reemplazó al CrUX Dashboard (noviembre 2025). El antiguo dashboard de Looker Studio quedó obsoleto. Usa [CrUX Vis](https://cruxvis.withgoogle.com) o la CrUX API directamente.
- **Subpartes de LCP** añadidas a CrUX (febrero 2025): Time to First Byte (TTFB), resource load delay, resource load time y element render delay ahora están disponibles como subcomponentes de LCP en los datos de CrUX.
- **Funciones de Google Search Console 2025** (diciembre 2025): Configuración asistida por IA para análisis automatizado. Filtro de consultas de marca vs. sin marca. Datos por hora disponibles en la API. Anotaciones personalizadas en gráficos. Seguimiento de canales sociales.

> La **indexación mobile-first** está 100% completa desde el 5 de julio de 2024. Google ahora rastrea e indexa TODOS los sitios web exclusivamente con el user-agent móvil de Googlebot. Asegúrate de que tu versión móvil contenga todo el contenido crítico, datos estructurados y meta tags.
