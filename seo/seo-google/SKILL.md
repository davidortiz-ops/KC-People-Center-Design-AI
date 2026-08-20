---
name: seo-google
description: >
  APIs de Google para SEO en directo: Search Console (clics, impresiones, CTR,
  posición, URL Inspection), PageSpeed Insights v5 + CrUX field data con historial
  25 semanas, Indexing API v3, GA4 tráfico orgánico y NLP entity extraction.
  Incluye un workflow de Oportunidades de Keywords (GSC Insights) con script propio
  `gsc_query.py` que detecta la zona de oportunidad (posición 5-15, altas impresiones,
  CTR bajo) y la cruza con el contenido real de la página para generar un reporte de
  brechas. Usar cuando el usuario diga "search console", "GSC", "PageSpeed", "CrUX",
  "field data", "GA4", "URL inspection", "LCP", "INP", "CLS", "FCP", "TTFB",
  "analiza keywords", "oportunidades GSC", "qué palabras optimizar", "impresiones y
  posición", o pida insights de rendimiento de búsqueda para cualquier URL.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - Bash
  - WebFetch
---

# Google SEO APIs — Google APIs Unificadas

Acceso directo a datos SEO de Google. Puente entre análisis crawl-based y datos
reales de campo: métricas Chrome reales, estado de indexación, rendimiento en
búsqueda y tráfico orgánico.

## Scripts Disponibles

**Incluido con este skill** (autocontenido y agnóstico):

| Script | Propósito |
|--------|-----------|
| `scripts/gsc_query.py --url "<URL>" --days 90` | Datos de Search Console por consulta (clics, impresiones, CTR, posición) para una URL o el dominio completo. Base del workflow de Oportunidades de Keywords. |

**Opcionales, de tu propio stack** (si los tienes disponibles; ajusta las rutas a la
estructura de tu proyecto):

| Script | Propósito |
|--------|-----------|
| `<tu-stack>/scripts/fetch_gsc_ga4.py <url> --pretty` | GSC + GA4 combinados para cualquier URL |
| `<tu-stack>/scripts/google_connector.py --list` | Listar propiedades GSC disponibles |
| `<tu-stack>/scripts/google_connector.py --refresh` | Redescubrir propiedades |
| `<tu-stack>/scripts/seo_monthly_analysis.py <url>` | Análisis mensual GSC + GA4 |

## Referencia Rápida

| Comando | Propósito |
|---------|-----------|
| `/seo google pagespeed <url>` | PageSpeed Insights + CrUX field data |
| `/seo google crux <url>` | CrUX field data solo (p75) |
| `/seo google crux-history <url>` | Tendencia CWV 25 semanas |
| `/seo google gsc <property>` | Search Analytics: clics, impresiones, CTR, posición (28d) |
| `/seo google inspect <url>` | URL Inspection: estado real de indexación |
| `/seo google sitemaps <property>` | Estado de sitemaps en GSC |
| `/seo google index <url>` | Indexing API — notificar a Google |
| `/seo google ga4 [property-id]` | Reporte GA4 tráfico orgánico |
| `/seo google ga4-pages [property-id]` | Top páginas de aterrizaje orgánicas |
| `/seo google nlp <url-or-text>` | NLP entity extraction + sentimiento + clasificación |
| `/seo google entities <url-or-text>` | Entity analysis solo (E-E-A-T) |
| `/seo google entity <query>` | Verificación de entidad en Knowledge Graph |
| `/seo google safety <url>` | Verificación de seguridad Web Risk |
| `/seo google report <type>` | Generar reporte PDF/HTML |

## Niveles de Credenciales

| Nivel | Detección | Comandos Disponibles |
|-------|-----------|---------------------|
| 0 (API Key) | `api_key` presente | pagespeed, crux, crux-history, nlp, entities, entity, safety |
| 1 (Service Account) | `GOOGLE_APPLICATION_CREDENTIALS` en .env | Nivel 0 + gsc, inspect, sitemaps, index, ga4 |

Detectar automáticamente (si tu stack incluye el conector):
```bash
python <tu-stack>/scripts/google_connector.py --list
```

## PageSpeed + CrUX

### pagespeed <url>
Combina datos de laboratorio Lighthouse + CrUX field data (28 días de Chrome de usuarios reales).

Métrica objetivo: LCP <2.5s, INP <200ms, CLS <0.1

### crux-history <url>
25 semanas de tendencia CrUX. Muestra si CWV mejora, empeora o se mantiene.

## Search Console

### gsc <property>
Search Analytics 28 días con detección de quick wins (posición 4-10, altas impresiones).

### inspect <url>
URL Inspection real de Google: veredicto (PASS/FAIL), estado coverage, canonical, rich results.

## Oportunidades de Keywords (GSC Insights)

Workflow autocontenido que conecta Search Console con el contenido real de la página
para encontrar las keywords que están *casi* rankeando bien y que con pequeños ajustes
pueden saltar a las primeras posiciones. Usa el script incluido `scripts/gsc_query.py`.

**Configuración (variables de entorno):**
- `GOOGLE_APPLICATION_CREDENTIALS` — ruta al JSON de la cuenta de servicio de Google.
- `GSC_SITE` — propiedad GSC (o se deriva del dominio de la URL objetivo).
- `CMS_API_URL` — URL base de la API del CMS, para obtener el contenido de la página (opcional).

### Paso 1 — Obtener datos de GSC
```bash
python scripts/gsc_query.py --url "<URL>" --days 90
```
Sin `--url`, trae datos del dominio completo (requiere `GSC_SITE`). Devuelve un JSON con
`query`, `clicks`, `impressions`, `ctr`, `position`.

### Paso 2 — Filtrar zona de oportunidad
Filtra las keywords que cumplan **todas** estas condiciones:
- `position` entre **5.0 y 15.0** (promedio)
- `impressions` ≥ **100** en el período
- `clicks` / `impressions` < **0.10** (CTR bajo = está siendo ignorada)

Ordena por `impressions` descendente y toma las top 20.

### Paso 3 — Obtener contenido real de la página
Si el usuario pasó una URL específica, obtén el contenido vía la API del CMS (ajusta la
ruta según el CMS del proyecto activo):
```bash
GET {CMS_API_URL}/posts?slug=<slug-del-articulo>&context=edit
```
Del campo de contenido extrae H2/H3/H4, párrafos y texto limpio (sin HTML) para el análisis.

### Paso 4 — Análisis semántico de brechas
Para cada keyword de oportunidad, determina:

| Estado | Criterio |
|--------|---------|
| ✅ **Presente** | La keyword (o sinónimo directo) aparece en H1/H2/H3 o en las primeras 200 palabras |
| ⚠️ **Parcial** | Aparece en el cuerpo pero no en encabezados ni en los primeros párrafos |
| ❌ **Ausente** | No aparece de ninguna forma en el contenido |

Para detectar sinónimos y variaciones, considera stemming básico (SEO/seo,
optimización/optimizar), variaciones de número (singular/plural) y keywords compuestas
(si "SEO tradicional" está presente, "SEO" y "tradicional" por separado no son brechas).

### Paso 5 — Reporte de oportunidades
Genera un reporte con esta estructura exacta:

```
## 📊 Reporte GSC Insights — [URL o Dominio]
**Período analizado**: [fecha_inicio] → [fecha_fin]
**Total keywords con datos**: [N]
**Keywords en zona de oportunidad (pos. 5-15)**: [N]

### 🎯 Top Oportunidades
| # | Keyword | Impresiones | Pos. promedio | CTR | En contenido |
|---|---------|-------------|---------------|-----|--------------|
| 1 | ejemplo keyword | 1,240 | 6.3 | 2.1% | ⚠️ Parcial |

### 🔴 Brechas críticas (ausentes con alta demanda)
- **"[keyword]"** — [N] impresiones, pos. [X] — No aparece en el contenido
  - *Acción*: Añadir sección o párrafo específico sobre este tema

### ⚠️ Oportunidades de refuerzo (parcial — mover a encabezados)
- **"[keyword]"** — [N] impresiones, pos. [X] — Presente en cuerpo, no en H2/H3
  - *Acción*: Incluir en un H2 o en los primeros 2 párrafos

### ✅ Ya optimizadas (mantener)
- "[keyword]" — [N] impresiones, pos. [X]

### 📌 Recomendaciones prioritarias
1. [Acción concreta más impactante]
2. [Segunda acción]
3. [Tercera acción]
```

## GA4 Traffic

### ga4 [property-id]
Reporte tráfico orgánico 28 días: sesiones, usuarios, pageviews, engagement rate.

```bash
python <tu-stack>/scripts/seo_monthly_analysis.py <url>
```

## PageSpeed + CrUX + GSC integrados (opcional, de tu stack)

Si tu stack provee un script de datos combinados, para obtenerlos en un solo comando:
```bash
python <tu-stack>/scripts/fetch_gsc_ga4.py <url> --pretty
```

## Indexing API

### index <url>
Notificar a Google sobre actualización de URL. Cuota: 200 publish/día.

> Nota: La Indexing API es oficialmente para JobPosting y BroadcastEvent/VideoObject.
> Usar con precaución.

Script (opcional, de tu stack):
```bash
python <tu-stack>/scripts/ping_indexing.py --site <s> --all
```

## NLP Content Analysis

Entity + sentimiento de Google Cloud NLP. Útil para puntuación E-E-A-T.

## Reportes

```bash
python <tu-stack>/scripts/audit_report.py --site <s>
```

Genera reporte HTML/MD profesional con los datos recolectados.

## Integración entre Skills

| Skill | Punto de Integración |
|-------|----------------------|
| **seo-audit** | Invoca `seo-google` para CWV + indexación real |
| **seo-technical** | CrUX field data complementa datos de laboratorio Lighthouse |
| **seo-content** | Datos de consultas GSC informan el targeting de keywords |
| **seo-geo** | GSC search appearance incluye referencias de AI Overview |

## Salida

```
## Reporte de APIs de Google: [URL/Propiedad]

### PageSpeed + CrUX
- LCP (p75): X.Xs [Bueno/Mejorable/Deficiente]
- INP (p75): Xms [Bueno/Mejorable/Deficiente]
- CLS (p75): X.XX [Bueno/Mejorable/Deficiente]

### Rendimiento en GSC (28 días)
- Clics totales: X
- Impresiones totales: X
- CTR: X%
- Posición promedio: X.X

### Quick Wins (posición 4-10, altas impresiones)
| Consulta | Pos | Impresiones | Clics | CTR |

### Tráfico orgánico GA4 (28 días)
- Sesiones: X
- Usuarios: X
- Tasa de interacción: X%

### Indexación
- Estado: [PASS/FAIL]
- Cobertura: [tipo]

### Recomendaciones
```

## Regla Bilingüe

Cuando el sitio está en inglés, generar el reporte en dos archivos:
- `GOOGLE-API-REPORT.md` (inglés)
- `GOOGLE-API-REPORT-ES.md` (español)

## Manejo de Errores

| Error | Resolución |
|-------|-----------|
| Sin credenciales | Verificar `GOOGLE_APPLICATION_CREDENTIALS` en .env |
| Propiedad GSC no encontrada | `python google_connector.py --refresh` |
| CrUX 404 | Tráfico insuficiente de Chrome. Fallback a datos de laboratorio PSI. |
| Propiedad GA4 no encontrada | Verificar ID de propiedad GA4 en config |
