# SEO

> Chapter de **People Center Design - Pragma**.

Colección de **21 skills de SEO** para Claude Code, diseñadas para ser **agnósticas**
(no dependen de ningún sitio, dominio ni stack concreto) y **completamente en español**.
Cubren auditoría, SEO técnico, contenido y E-E-A-T, datos de Google, SEO local y
e-commerce, GEO (búsqueda con IA), estrategia y SEO programático.

> **Convenciones del repositorio**
> - Cada skill es una carpeta con un archivo `SKILL.md` (frontmatter `name` + `description` con frases de activación).
> - Todo el contenido, comentarios de código y mensajes están en español.
> - No hay credenciales, dominios ni rutas hardcodeadas: la configuración se lee de variables de entorno (ver [Configuración](#configuración)).

---

## Estructura

```
seo/
├── README.md                  ← este archivo
├── seo/                       ← skill orquestador + recursos compartidos
│   ├── SKILL.md
│   ├── references/            ← documentación cargada bajo demanda
│   │   ├── cwv-thresholds.md
│   │   ├── eeat-framework.md
│   │   ├── gsc-ga4-integration.md
│   │   ├── quality-gates.md
│   │   └── schema-types.md
│   ├── pdf/google-seo-reference.md
│   ├── schema/templates.json  ← plantillas JSON-LD (schema.org)
│   ├── scripts/               ← utilidades (fetch, parse, screenshot, visual)
│   └── hooks/                 ← hooks pre-commit y validación de schema
├── seo-google/
│   ├── SKILL.md
│   └── scripts/gsc_query.py   ← consulta agnóstica a Search Console
├── seo-plan/
│   ├── SKILL.md
│   └── assets/                ← plantillas de estrategia por industria
└── seo-<...>/SKILL.md         ← resto de skills especializadas
```

---

## Catálogo de skills

### Orquestación
| Skill | Qué hace |
|-------|----------|
| **seo** | Skill maestra. Orquesta las otras 20 sub-skills mediante delegación paralela a subagentes; detecta el tipo de negocio y produce un SEO Health Score (0-100) con plan de acción priorizado. |

### Auditoría y página
| Skill | Qué hace |
|-------|----------|
| **seo-audit** | Auditoría completa del sitio. Rastrea hasta 500 páginas, detecta el tipo de negocio, delega a especialistas y genera un health score. |
| **seo-page** | Análisis SEO profundo de una página individual: on-page, contenido, meta tags técnicos, schema, imágenes y rendimiento. |

### SEO técnico, on-page e infraestructura
| Skill | Qué hace |
|-------|----------|
| **seo-technical** | Rastreo e indexación: canonical, contenido duplicado, robots, automatización de sitemaps, crawlers de IA, códigos HTTP. |
| **seo-on-page** | Meta tags: title, meta description, Open Graph, Twitter Cards, favicon, Google Discover, title link. Incluye ejemplos reales. |
| **seo-performance** | Core Web Vitals (LCP, INP, CLS), indexación mobile-first y experiencia de página. |
| **seo-accessibility** | Accesibilidad (ARIA, skip links, foco en SPAs, WCAG 2.1 AA) con impacto SEO. |
| **seo-schema** | Datos estructurados JSON-LD, Featured Snippets y cobertura completa de tipos de schema. |
| **seo-sitemap** | Sitemaps XML/HTML, índices, sitemaps de video/imagen/noticias, envío a Google/Bing/IndexNow. |
| **seo-images** | Optimización de imágenes y video: WebP/AVIF, alt text, imágenes responsivas, lazy loading, CLS. |
| **seo-hreflang** | SEO internacional y multilenguaje: hreflang, geotargeting, páginas adaptativas por ubicación. |

### Contenido
| Skill | Qué hace |
|-------|----------|
| **seo-content** | Calidad de contenido y E-E-A-T, preparación para citas de IA, palabras LSI, detección de patrones de escritura por IA. |
| **seo-cluster** | Clustering semántico de topics por superposición de SERP; arquitectura hub-and-spoke con enlazado interno. |
| **seo-competitor-pages** | Generación de páginas de comparación de competidores (X vs Y, alternativas, matrices de características). |

### Datos y APIs de Google
| Skill | Qué hace |
|-------|----------|
| **seo-google** | APIs de Google: Search Console, PageSpeed Insights v5 + CrUX, Indexing API v3, GA4, NLP. Incluye el workflow **Oportunidades de Keywords (GSC Insights)** con el script propio `gsc_query.py`. |

### Local y e-commerce
| Skill | Qué hace |
|-------|----------|
| **seo-local** | SEO local: GBP, NAP, citas, reseñas, schema local, multi-ubicación, recomendaciones por industria. |
| **seo-ecommerce** | SEO de e-commerce: schema de producto, Google Shopping, brechas en marketplaces, páginas de producto. |

### Búsqueda con IA y experiencia
| Skill | Qué hace |
|-------|----------|
| **seo-geo** | Generative Engine Optimization: AI Overviews, ChatGPT Search, Perplexity; llms.txt, citabilidad a nivel de pasaje, señales de marca. |
| **seo-sxo** | Search Experience Optimization: detección de page-type mismatch, user stories desde la intención, scoring por persona. |

### Estrategia y escala
| Skill | Qué hace |
|-------|----------|
| **seo-plan** | Planificación estratégica con plantillas por industria (ver `seo-plan/assets/`). |
| **seo-programmatic** | SEO programático para páginas a escala: plantillas, patrones de URL, enlazado automático, salvaguardas contra contenido thin. |

---

## Configuración

Las skills no requieren configuración para el análisis basado en web. Algunas
capacidades opcionales usan APIs externas mediante **variables de entorno** (se pueden
definir en el entorno o en un archivo `.env`):

| Variable | Usada por | Propósito |
|----------|-----------|-----------|
| `GOOGLE_APPLICATION_CREDENTIALS` | `seo-google` (`gsc_query.py`) | Ruta al JSON de la cuenta de servicio de Google Cloud (acceso a Search Console). |
| `GSC_SITE` | `seo-google` (`gsc_query.py`) | Propiedad de Search Console (ej. `sc-domain:tu-sitio.com`). Si se omite, se deriva del dominio de la URL. |
| `CMS_API_URL` | `seo-google` (workflow GSC Insights) | URL base de la API del CMS para extraer el contenido real de la página (opcional). |
| `SEO_DOTENV` | scripts | Ruta explícita a un archivo `.env`. Si se omite, se busca automáticamente subiendo desde el directorio actual. |

> Para usar scripts adicionales de tu propio stack (extracción combinada de GSC+GA4,
> conectores, etc.), las skills referencian rutas genéricas tipo `<tu-stack>/scripts/...`
> que debes ajustar a la estructura de tu proyecto. No se incluyen en este repositorio.

### Dependencias de los scripts en Python

```bash
pip install requests beautifulsoup4 lxml playwright python-dotenv \
    google-api-python-client google-auth
playwright install chromium   # solo para capture_screenshot.py y analyze_visual.py
```

---

## Recursos compartidos (carpeta `seo/`)

### Scripts (`seo/scripts/`)
| Script | Propósito |
|--------|-----------|
| `fetch_page.py` | Descarga una página con cabeceras adecuadas, manejo de errores y prevención de SSRF. Detecta renderizado dinámico con el UA de Googlebot. |
| `parse_html.py` | Extrae elementos SEO del HTML (title, meta, encabezados, imágenes, enlaces, schema, hreflang, conteo de palabras). |
| `capture_screenshot.py` | Captura screenshots por viewport (desktop/laptop/tablet/mobile) con Playwright. |
| `analyze_visual.py` | Analiza above-the-fold, responsividad móvil y tipografía con Playwright. |

### Referencias (`seo/references/`)
Documentación cargada **bajo demanda** por las skills (no toda al inicio):
`cwv-thresholds.md`, `eeat-framework.md`, `quality-gates.md`, `schema-types.md`,
`gsc-ga4-integration.md`, y la referencia rápida `seo/pdf/google-seo-reference.md`.

### Plantillas de schema (`seo/schema/templates.json`)
Plantillas JSON-LD listas para usar (VideoObject, ProductGroup, ProfilePage,
Certification, OfferShippingDetails, etc.). Las claves y valores de schema.org se
mantienen en su forma estándar; las descripciones y placeholders están en español.

### Hooks (`seo/hooks/`)
| Hook | Propósito |
|------|-----------|
| `validate-schema.py` | Valida JSON-LD tras editar archivos (PostToolUse). Bloquea (exit 2) ante placeholders, tipos obsoletos o JSON inválido. |
| `pre-commit-seo-check.sh` | Verificación SEO previa al commit: placeholders, longitud de title/meta, alt text, schema obsoleto, referencias a FID. |

Ambos detectan placeholders tanto en inglés como en español.

### Plantillas de estrategia (`seo-plan/assets/`)
Plantillas por industria para `seo-plan`: `generic.md`, `saas.md`, `ecommerce.md`,
`local-service.md`, `publisher.md`, `agency.md`.

---

## Convenciones

- **Agnosticismo:** las skills y los scripts leen su configuración de variables de entorno
  y no contienen dominios, usuarios, contraseñas ni rutas absolutas hardcodeadas.
- **Idioma:** el contenido está en español. Los términos técnicos estándar y los valores
  literales (schema.org, cabeceras HTTP, nombres de API) permanecen en su forma original.
- **Formato:** cada skill vive en su propia carpeta con un `SKILL.md` (frontmatter `name`
  + `description` con frases de activación).
