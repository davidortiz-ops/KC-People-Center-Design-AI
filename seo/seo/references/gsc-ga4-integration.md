# Integración de datos reales GSC + GA4

Si trabajas en un proyecto cuyo stack incluye un script tipo `fetch_gsc_ga4.py`,
ejecútalo ANTES de iniciar cualquier análisis SEO para enriquecer la auditoría con
datos reales. Ajusta la ruta a la estructura de tu proyecto.

## Cómo obtener datos reales

```bash
python <tu-stack>/scripts/fetch_gsc_ga4.py <url> --pretty
```

Si el script no está disponible, omite este paso y continúa solo con los datos
obtenidos vía web.

## Datos disponibles

### GSC (Google Search Console)
- `gsc.site` — clics, impresiones, CTR y posición promedio a nivel de sitio
- `gsc.page` — las mismas métricas para la URL específica que se audita
- `gsc.keywords` — top 20 de consultas que traen tráfico a la página (ordenadas por clics)
- `gsc.opportunities` — consultas en posición 5-20 con buenas impresiones (quick wins)
- `gsc.top_pages` — top 10 de páginas por clics en todo el sitio

### GA4 (Google Analytics 4)
- `ga4.site` — sesiones, usuarios, vistas de página, duración media de sesión, tasa de rebote, tasa de interacción
- `ga4.page` — las mismas métricas para la ruta de página específica
- `ga4.channels` — desglose de tráfico por canal (Orgánico, Directo, Referido, etc.)
- `ga4.top_pages` — top 10 de páginas por sesiones en todo el sitio

## Cómo usarlos en auditorías

**Reemplazar estimaciones con números reales:**
- En vez de "se estiman X visitantes" → usa `ga4.site.sessions`
- En vez de "parece rankear para Y" → usa `gsc.keywords`

**Sección de Oportunidades de Keywords:**
- Lista `gsc.opportunities` como Quick Wins (ya rankean, solo necesitan optimización)
- Marca consultas con altas impresiones + bajo CTR como objetivos de optimización de título/meta

**Sección de Calidad de Contenido:**
- `ga4.page.avg_session_duration_s` < 30s = usuarios sin interacción → señal de contenido thin
- `ga4.page.bounce_rate_pct` > 75% = desajuste de intención
- `ga4.page.engagement_rate_pct` < 40% = el contenido no satisface las necesidades del usuario

**Sección de Salud del Tráfico:**
- Mezcla de canales: depender mucho de un solo canal = riesgo (marcar si >80% proviene de una sola fuente)
- Proporción orgánico vs pago: muestra el nivel de dependencia del SEO

## Manejo de errores

Si el arreglo `errors` no está vacío:
- "No se encontró propiedad" → sitio no conectado, auditar sin datos reales y anotar la brecha
- Errores de "GA4 Admin API" → API no habilitada, usar solo datos de GSC
- Errores de red → reintentar una vez, luego continuar sin datos reales

## Caché

Los datos se cachean en `properties_cache.json` (TTL de 6h).
Para forzar la actualización: `python <tu-stack>/scripts/google_connector.py --refresh`
