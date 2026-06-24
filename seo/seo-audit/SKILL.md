---
name: seo-audit
description: >
  Auditoría SEO completa de sitios web con delegación paralela a subagentes.
  Rastrea hasta 500 páginas, detecta el tipo de negocio, delega a 7 especialistas,
  genera un puntaje de salud. Usar cuando el usuario diga "audit", "full SEO check",
  "analyze my site" o "website health check".
---

# Auditoría SEO Completa de Sitio Web

## Proceso

0. **Obtener datos reales de GSC + GA4** — Paso recomendado, ejecutar antes que nada si tu stack
   cuenta con un script para extraer datos de GSC/GA4 (ajusta la ruta a tu proyecto):
   ```bash
   python <tu-stack>/scripts/fetch_gsc_ga4.py <url> --pretty
   ```
   Parsear la salida JSON y almacenar como `gsc_ga4_data`. Si `errors` no está vacío o el script
   no se encuentra, anotarlo en el reporte y continuar. Nunca saltar este paso silenciosamente.

1. **Obtener homepage** — recuperar HTML vía solicitud HTTP
2. **Detectar tipo de negocio** — analizar señales de la homepage según el orquestador SEO
3. **Rastrear sitio** — seguir enlaces internos hasta 500 páginas, respetar robots.txt
4. **Delegar a subagentes** (si están disponibles, si no ejecutar en línea secuencialmente):
   - `seo-technical` — robots.txt, sitemaps, canónicas, Core Web Vitals, headers de seguridad, renderizado JS, IndexNow
   - `seo-content` — E-E-A-T, legibilidad, contenido thin, preparación para citas de IA
   - `seo-schema` — detección, validación, recomendaciones de generación
   - `seo-sitemap` — análisis de estructura, controles de calidad, páginas faltantes
   - `seo-geo` — acceso de crawlers de IA, llms.txt, citabilidad, señales de menciones de marca
   - `seo-google` — datos reales de GSC, PSI, datos de campo CrUX + oportunidades de keywords
   - `seo-local` — GBP, NAP, citas, salud de reseñas (si se detecta negocio local)
   - `seo-sxo` — detección de desajuste de tipo de página para landing pages clave
   - `seo-ecommerce` — schema de producto y SEO on-page de producto (si se detecta e-commerce)
5. **Puntuar** — agregar en Puntaje de Salud SEO (0-100)
6. **Reportar** — generar plan de acción priorizado enriquecido con datos reales de GSC + GA4

## Configuración de Rastreo

```
Max pages: 500
Respect robots.txt: Yes
Follow redirects: Yes (max 3 hops)
Timeout per page: 30 seconds
Concurrent requests: 5
Delay between requests: 1 second
```

## Archivos de Salida

- `FULL-AUDIT-REPORT.md` — Hallazgos completos
- `FULL-AUDIT-REPORT.html` — Mismo contenido que el reporte Markdown pero con diseño profesional, CSS integrado, layout responsivo, codificación de colores por prioridad y una sección "AI Specs" con instrucciones legibles por máquina para corregir automáticamente los problemas identificados.
- `ACTION-PLAN.md` — Recomendaciones priorizadas (Crítico → Alto → Medio → Bajo)
- `screenshots/` — Capturas de escritorio + móvil (si Playwright está disponible)

## Especificaciones del Reporte HTML

El reporte HTML DEBE ser completamente autónomo: todo CSS inline en `<style>`, sin enlaces externos a CDN,
sin URLs de Google Fonts, sin JS externo. Usar solo pila de fuentes del sistema: `font-family: -apple-system,
BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`. El archivo debe funcionar al abrirse sin conexión.

Al generar el `FULL-AUDIT-REPORT.html`, DEBES incluir:
1. **Sistema de Diseño Profesional**: Solo CSS embebido. Sombras suaves, amplio espacio en blanco, diseño limpio.
2. **Codificación de Colores**: Crítico=`#dc2626`, Alto=`#ea580c`, Medio=`#ca8a04`, Bajo=`#2563eb`, Bueno=`#16a34a`.
3. **Layout Responsivo**: Mobile-first. Barra lateral en escritorio, apilado en móvil.
4. **Dashboard de Datos Reales** (solo si `gsc_ga4_data` se obtuvo correctamente): Una sección destacada
   al inicio con tarjetas de métricas que muestren: clics GSC, impresiones, CTR, posición promedio; sesiones GA4,
   usuarios, tasa de engagement, canal principal. Usar una cuadrícula de 4 columnas con tarjetas de estadísticas con icono, valor, etiqueta.
5. **Elementos Estructurados/Interactivos**: Tablas, tarjetas, badges de severidad, secciones colapsables.
6. **Sección AI Fix Specs**: Al final, JSON legible por máquina con instrucciones de corrección precisas.

**IMPORTANTE:** DEBES GENERAR TAMBIÉN `FULL-AUDIT-REPORT.md`. Ambos archivos son requeridos.

## Pesos de Puntuación

| Categoría | Peso |
|----------|--------|
| SEO Técnico | 22% |
| Calidad de Contenido | 23% |
| SEO On-Page | 20% |
| Schema / Datos Estructurados | 10% |
| Rendimiento (CWV) | 10% |
| Preparación para Búsqueda IA | 10% |
| Imágenes | 5% |

## Estructura del Reporte

### 0. Datos de Tráfico Reales — GSC + GA4
**Siempre la primera sección después del Resumen Ejecutivo. Poblada desde `gsc_ga4_data`.**

#### Google Search Console (últimos 90 días)
- Tarjetas de métricas: Total Clicks · Total Impressions · CTR · Avg Position
- Top 10 páginas por clics (tabla: URL, clicks, impressions, CTR, posición)
- Top keywords activas para la URL auditada (tabla: query, clicks, impressions, CTR, posición)
- Oportunidades de keywords: queries posición 5-20 con gap `top_10_low_ctr` o `page_2`
  → Mostrar como "Quick Wins" con indicador de tipo de gap

#### Google Analytics 4 (últimos 90 días)
- Tarjetas de métricas: Sesiones · Usuarios · Pageviews · Avg Session Duration · Bounce Rate · Engagement Rate
- Canales de tráfico (tabla: canal, sesiones, usuarios, % del total)
- Top 10 páginas por sesiones (tabla: path, sesiones, pageviews, avg duration, bounce rate)
- Métricas específicas de la URL auditada (si está disponible): sesiones, pageviews, engagement, bounce

#### Interpretación de datos
- Señalar si CTR GSC < 2% con >10K impresiones → problema de título/meta
- Señalar si bounce rate GA4 > 70% → problema de intención de búsqueda
- Señalar si avg session duration < 60s → problema de contenido/relevancia
- Señalar canales con dependencia >80% → riesgo de concentración

### Resumen Ejecutivo
- Puntaje de Salud SEO General (0-100)
- Tipo de negocio detectado
- Período de datos: `gsc_ga4_data.period_days` días
- Top 5 problemas críticos
- Top 5 quick wins (incluir oportunidades de keywords de GSC si aplica)

### SEO Técnico
- Problemas de rastreabilidad
- Problemas de indexabilidad
- Problemas de seguridad
- Estado de Core Web Vitals

### Calidad de Contenido
- Evaluación E-E-A-T
- Páginas con contenido thin — cruzar con páginas de bajo engagement en GA4
- Problemas de contenido duplicado
- Puntajes de legibilidad

### SEO On-Page
- Problemas de title tag
- Problemas de meta description
- Estructura de encabezados
- Brechas de internal linking

### Schema y Datos Estructurados
- Implementación actual
- Errores de validación
- Oportunidades faltantes

### Rendimiento
- Puntajes LCP, INP, CLS
- Necesidades de optimización de recursos
- Impacto de scripts de terceros

### Imágenes
- Falta de alt text
- Imágenes sobredimensionadas
- Recomendaciones de formato

### Preparación para Búsqueda IA
- Puntaje de citabilidad
- Mejoras estructurales
- Señales de autoridad

## Definiciones de Prioridad

- **Crítico**: Bloquea la indexación o causa penalizaciones (corregir inmediatamente)
- **Alto**: Impacta significativamente los rankings (corregir en 1 semana)
- **Medio**: Oportunidad de optimización (corregir en 1 mes)
- **Bajo**: Deseable (backlog)

## Referencia Rápida entre Skills

| Necesidad | Skill |
|------|-------|
| Datos GSC + GA4 + oportunidades de keywords | `/seo google <url>` |
| Topic clustering | `/seo cluster plan <seed-kw>` |
| Análisis de tipo de página | `/seo sxo <url> <keyword>` |
| SEO Local | `/seo local <url>` |
| Auditoría e-commerce | `/seo ecommerce <url>` |
| Páginas de comparación de competidores | `/seo competitor-pages <url>` |

## Regla de Reporte Bilingüe

Cuando el sitio auditado está en inglés:
- `FULL-AUDIT-REPORT.md` (inglés)
- `FULL-AUDIT-REPORT-ES.md` (español)

## Scripts locales de automatización (opcional)

Si tu stack incluye scripts de automatización SEO, puedes complementar la auditoría con
datos del proyecto. No son requeridos. Ajusta las rutas (`<tu-stack>/...`) a la estructura
de tu proyecto:

**Antes de la auditoría:**
```bash
python <tu-stack>/scripts/site_health.py --site <s>               # Verificar conexiones
python <tu-stack>/scripts/audit_init.py --site <s>               # Crear carpeta de sesión con línea base
python <tu-stack>/scripts/detect_cannibalization.py --site <s> --save-to-audit  # Añadir sección de canibalización
python <tu-stack>/scripts/track_regressions.py --site <s> --save-to-audit       # Detectar regresiones previas
```

**Después de la auditoría (aplicar correcciones masivas identificadas):**
```bash
python <tu-stack>/scripts/fix_missing_alt.py --site <s>           # Cierra el gap de imágenes (5% del score)
python <tu-stack>/scripts/fix_missing_excerpts.py --site <s>      # Cierra el gap de meta descriptions
python <tu-stack>/scripts/evergreen_converter.py --site <s>       # Elimina señales de obsolescencia
```

**Generar entregable para cliente:**
```bash
python <tu-stack>/scripts/audit_diff.py --site <s>                # Delta vs auditoría anterior
python <tu-stack>/scripts/audit_report.py --site <s>              # CLIENT-REPORT.html + .md
```
