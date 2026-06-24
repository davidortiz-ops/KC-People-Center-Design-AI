<!-- Actualizado: 2026-02-07 -->
# Plantilla de estrategia SEO para negocio de servicio local

## Características de la industria

- Búsquedas con enfoque geográfico
- Alta intención, toma de decisiones rápida
- Las reseñas influyen fuertemente en las decisiones
- Las llamadas telefónicas son la conversión principal
- Comportamiento de usuario mobile-first
- Necesidades de servicio de emergencia/urgentes

## Arquitectura de sitio recomendada

```
/
├── Inicio
├── /servicios
│   ├── /servicio-1
│   ├── /servicio-2
│   └── ...
├── /ubicaciones
│   ├── /ciudad-1
│   │   ├── /servicio-1-ciudad-1
│   │   └── ...
│   ├── /ciudad-2
│   └── ...
├── /acerca-de
├── /resenas
├── /galeria (o /portafolio)
├── /blog
├── /contacto
├── /emergencias (si aplica)
└── /faq
```

## Umbrales de calidad

### Límites de páginas de ubicación
- ⚠️ **ADVERTENCIA** a partir de 30+ páginas de ubicación
- 🛑 **PARADA OBLIGATORIA** a partir de 50+ páginas de ubicación

### Requisitos de contenido único
| Tipo de página | Palabras mín. | % único |
|-----------|-----------|----------|
| Ubicación principal | 600 | 60%+ |
| Área de servicio | 500 | 40%+ |
| Página de servicio | 800 | 100% |

### Qué hace únicas a las páginas de ubicación
- Puntos de referencia y barrios locales
- Servicios específicos ofrecidos en esa ubicación
- Miembros del equipo local
- Testimonios específicos de la ubicación
- Participación en la comunidad
- Regulaciones o consideraciones locales

## Recomendaciones de schema

| Tipo de página | Tipos de schema |
|-----------|-------------|
| Homepage | LocalBusiness, Organization |
| Páginas de servicio | Service, LocalBusiness |
| Páginas de ubicación | LocalBusiness (con geo) |
| Contacto | ContactPage, LocalBusiness |
| Reseñas | LocalBusiness (con AggregateRating) |

### Ejemplo de schema LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Nombre del Negocio",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Principal 123",
    "addressLocality": "Ciudad",
    "addressRegion": "Región",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "openingHours": "Mo-Fr 08:00-18:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  },
  "areaServed": ["Ciudad 1", "Ciudad 2"],
  "priceRange": "$$"
}
```

## Integración con Google Business Profile

- Asegurar consistencia NAP (Nombre, Dirección, Teléfono)
- Sincronizar categorías de servicio
- Actualizaciones regulares de publicaciones
- Subir fotos
- Estrategia de respuesta a reseñas

### Actualizaciones de Google Business Profile (2025-2026)

- **La verificación por video** ahora es estándar — la verificación por postal se ha eliminado en gran medida. Prepárate para un proceso corto de verificación por video que muestre la ubicación del negocio o el área de servicio.
- **La integración con WhatsApp** reemplazó a Google Business Chat (obsoleto). Los negocios pueden conectar WhatsApp como su canal principal de mensajería.
- **Q&A eliminado de Maps** — reemplazado por respuestas generadas por IA. Asegúrate de que tu descripción de GBP, servicios y FAQ del sitio sean exhaustivos, ya que la IA de Google los usa para responder consultas.
- **El horario del negocio es un factor de ranking top-5** — "El negocio está abierto al momento de la búsqueda" se ubicó por primera vez como un factor individual top (Whitespark 2026 Local Search Ranking Factors Report). Mantén el horario preciso; considera horarios extendidos si es factible.
- **Formato de "Stories" de reseñas** — Google Maps ahora muestra fragmentos de reseñas en un formato deslizable tipo Stories en móvil. Fomenta reseñas detalladas y descriptivas con fotos.

### Actualización de Service Area Business (SAB) (junio 2025)

Google actualizó las directrices de SAB para **prohibir estados o países enteros** como áreas de servicio. Los SAB deben especificar: ciudades, códigos postales o barrios. Si das servicio a un área metropolitana entera, lista las ciudades principales dentro de ella en lugar del estado.

### Visibilidad en IA para negocios locales

Los AI Overviews aparecen solo para ~0.14% de las keywords locales (datos de marzo 2025) — el SEO local enfrenta significativamente menos disrupción por IA que otras verticales. Sin embargo, ChatGPT y Perplexity se usan cada vez más para recomendaciones locales.

Para optimizar la visibilidad local en IA:
- Asegurar presencia en listas "best of" curadas por expertos (factor #1 de visibilidad en IA según el reporte Whitespark 2026)
- Mantener NAP consistente (Nombre, Dirección, Teléfono) en todas las plataformas
- Construir volumen y calidad genuinos de reseñas
- Usar schema LocalBusiness con propiedades completas (geo, openingHours, priceRange, areaServed)

## Prioridades de contenido

### Alta prioridad
1. Homepage con área de servicio clara
2. Páginas principales de servicio
3. Página de la ciudad principal
4. Página de contacto con todas las ubicaciones

### Prioridad media
1. Páginas de combinación servicio + ubicación
2. Página de FAQ
3. Página de equipo/acerca de
4. Página de reseñas/testimonios

### Temas de blog
- Consejos de mantenimiento estacional
- Cómo elegir un [proveedor de servicio]
- Señales de advertencia de [problema]
- Comparaciones DIY vs profesional
- Regulaciones y permisos locales

## Métricas clave a monitorear

- Rankings en el local pack
- Volumen de llamadas desde orgánico
- Solicitudes de indicaciones (direcciones)
- Insights de Google Business Profile
- Cantidad de reseñas y calificación

## Generative Engine Optimization (GEO) para local

- [ ] Incluir descripciones de servicio y rangos de precio claros y citables
- [ ] Usar schema LocalBusiness con geo, openingHours y areaServed completos
- [ ] Construir presencia en listas "best of" curadas y directorios locales
- [ ] Mantener NAP consistente en todas las plataformas (Google, Yelp, Apple Maps)
- [ ] Incluir fotos originales del trabajo, el equipo y la ubicación
- [ ] Estructurar contenido de FAQ para preguntas comunes de servicio local
- [ ] Monitorear la citación por IA en recomendaciones locales de ChatGPT y Perplexity
