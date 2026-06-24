<!-- Actualizado: 2026-02-07 -->
# Plantilla de estrategia SEO para publisher/medios

## Características de la industria

- Alto volumen de contenido
- Contenido sensible al tiempo (noticias)
- Ingresos por publicidad dependientes del tráfico
- Autoridad y confianza críticas
- Compitiendo con plataformas sociales
- Impacto de los AI Overviews en el tráfico

## Arquitectura de sitio recomendada

```
/
├── Inicio
├── /noticias (o /ultimas)
├── /temas
│   ├── /tema-1
│   ├── /tema-2
│   └── ...
├── /autores
│   ├── /autor-1
│   └── ...
├── /opinion
├── /resenas
├── /guias
├── /videos
├── /podcasts
├── /newsletter
├── /acerca-de
│   ├── /politica-editorial
│   ├── /correcciones
│   └── /contacto
└── /[anio]/[mes]/[slug] (URLs de artículo)
```

## Recomendaciones de schema

| Tipo de página | Tipos de schema |
|-----------|-------------|
| Artículo | NewsArticle o Article, Person (autor), Organization (publisher) |
| Página de autor | Person, ProfilePage |
| Página de tema | CollectionPage, ItemList |
| Homepage | WebSite, Organization |
| Video | VideoObject |
| Podcast | PodcastEpisode, PodcastSeries |

### Ejemplo de schema NewsArticle
```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Titular del Artículo",
  "datePublished": "2026-02-07T10:00:00Z",
  "dateModified": "2026-02-07T14:30:00Z",
  "author": {
    "@type": "Person",
    "name": "Nombre del Autor",
    "url": "https://example.com/autores/nombre-autor"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Nombre de la Publicación",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "image": ["https://example.com/imagen-articulo.jpg"],
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/url-articulo"
  }
}
```

## Requisitos de E-E-A-T

Los publishers enfrentan el mayor escrutinio de E-E-A-T.

### Las páginas de autor deben incluir
- Nombre completo y foto
- Bio y credenciales
- Áreas de pericia
- Información de contacto
- Perfiles sociales (sameAs)
- Artículos previos de este autor

### Estándares editoriales
- Política de correcciones clara
- Proceso editorial transparente
- Procedimientos de verificación de hechos
- Divulgación de conflictos de interés

## Prioridades de contenido

### Alta prioridad
1. Noticias de última hora (la velocidad importa)
2. Guías evergreen sobre temas centrales
3. Páginas de autor con credenciales
4. Hubs de tema/páginas pilar

### Prioridad media
1. Piezas de opinión/análisis
2. Contenido de video
3. Contenido interactivo
4. Landing pages de newsletter

### Consideraciones GEO
- Hechos claros y citables en los artículos
- Tablas para contenido con muchos datos
- Citas de expertos con atribución
- Fechas de actualización mostradas de forma prominente
- Encabezados estructurados (H2/H3)
- Los datos de origen propio y la investigación original son muy citados por los sistemas de IA
- Asegurar que las entidades de autor estén claramente definidas con schema Person + enlaces sameAs
- Monitorear la frecuencia de citación por IA en Google AI Overviews, AI Mode, ChatGPT, Perplexity
- Tratar la citación por IA como un KPI independiente junto al tráfico orgánico

### Actualizaciones de SEO para publishers (2025-2026)

- **Inclusión automática en Google News:** Google News ya no acepta solicitudes manuales (desde marzo 2025). La inclusión es totalmente automática según los criterios de calidad de contenido de Google. Enfócate en el marcado del sitemap de Google News y en una cadencia de publicación consistente y de alta calidad.
- **Cambio de KPI:** Los KPI basados en tráfico (sesiones, vistas de página) pierden relevancia a medida que los AI Overviews reducen las tasas de click-through. Los publishers líderes están migrando a: conversiones de suscriptores, tiempo en página, profundidad de scroll, registros a newsletter, frecuencia de citación por IA e ingresos por visitante.
- **Riesgo de abuso de reputación del sitio:** Los publishers que alojan contenido de terceros (cupones, reseñas de producto, contenido de afiliados) bajo su dominio están en alto riesgo. Google penalizó a Forbes, WSJ, Time y CNN por esto a finales de 2024. Si alojas contenido de terceros, asegura una fuerte supervisión editorial y una clara participación de origen propio.

## Consideraciones técnicas

### Core Web Vitals
- La ubicación de anuncios afecta el CLS
- Lazy load de anuncios e imágenes bajo el pliegue
- Optimizar imágenes hero para LCP
- Minimizar recursos que bloquean el renderizado

### AMP (si se usa)
- Considera abandonar AMP (ya no es requerido para Top Stories)
- Asegura una configuración canonical correcta
- Monitorea el rendimiento vs no-AMP

### Paginación
- Paginación adecuada para artículos de varias páginas
- O scroll infinito con indexación adecuada
- Canonical a la página 1 o al artículo completo

## Métricas clave a monitorear

- Vistas de página desde orgánico
- Tiempo en página
- Páginas por sesión
- Registros a newsletter desde orgánico
- Tráfico de Google News/Discover
- Apariciones en AI Overview
