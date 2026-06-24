<!-- Actualizado: 2026-02-07 -->
# Plantilla de estrategia SEO para agencia/consultoría

## Características de la industria

- Basado en servicios, transacciones de alto valor
- La pericia y la confianza son primordiales
- Ciclos de consideración largos
- Decisiones impulsadas por portafolio/casos de estudio
- Ventas basadas en relaciones
- Beneficios de la especialización en nicho

## Arquitectura de sitio recomendada

```
/
├── Inicio
├── /servicios
│   ├── /servicio-1
│   │   ├── /sub-servicio-1
│   │   └── ...
│   └── /servicio-2
├── /industrias
│   ├── /industria-1
│   ├── /industria-2
│   └── ...
├── /trabajo (o /casos-de-estudio)
│   ├── /caso-de-estudio-1
│   ├── /caso-de-estudio-2
│   └── ...
├── /acerca-de
│   ├── /equipo
│   │   ├── /miembro-1
│   │   └── ...
│   ├── /cultura
│   └── /empleo
├── /insights (o /blog)
│   ├── /articulos
│   ├── /guias
│   ├── /webinars
│   └── /podcasts
├── /contacto
├── /proceso
└── /faq
```

## Recomendaciones de schema

| Tipo de página | Tipos de schema |
|-----------|-------------|
| Homepage | Organization, ProfessionalService |
| Página de servicio | Service, ProfessionalService |
| Caso de estudio | Article, Organization (cliente) |
| Miembro del equipo | Person, ProfilePage |
| Blog | Article, BlogPosting |

### Ejemplo de schema ProfessionalService
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Nombre de la Agencia",
  "description": "Lo que hace la agencia",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Agencia 123",
    "addressLocality": "Ciudad",
    "addressRegion": "Región",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "areaServed": "Nacional",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicios",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Servicio 1"
        }
      }
    ]
  }
}
```

## Requisitos de E-E-A-T

### Las páginas de equipo deben incluir
- Fotos profesionales
- Bios detalladas con credenciales
- Experiencia en la industria
- Ponencias/conferencias
- Publicaciones
- Perfiles sociales

### Los casos de estudio deben incluir
- Nombre del cliente (con permiso) o industria
- Planteamiento del reto/problema
- Enfoque/metodología
- Resultados con métricas específicas
- Cronología
- Cita de testimonio

## Prioridades de contenido

### Alta prioridad
1. Páginas de servicio (detalladas, específicas)
2. Páginas de industria (pericia vertical)
3. 3-5 casos de estudio detallados
4. Páginas de equipo/liderazgo

### Prioridad media
1. Página de metodología/proceso
2. Blog con liderazgo de pensamiento
3. Contenido de comparación (vs alternativas)
4. Página de FAQ

### Temas de liderazgo de pensamiento
- Análisis de tendencias de la industria
- Guías prácticas (no competitivas)
- Investigación/encuestas originales
- Resúmenes e insights de eventos
- Entrevistas a expertos
- Reseñas de herramientas/tecnología

## Estrategia de contenido

### Páginas de servicio (mín. 800 palabras)
- Propuesta de valor clara
- Resumen de metodología
- Lista de entregables
- Casos de estudio relevantes
- Miembros del equipo que prestan este servicio
- CTA para agendar consulta

### Páginas de industria (mín. 800 palabras)
- Retos específicos de la industria
- Cómo los resuelves de forma diferente
- Casos de estudio relevantes
- Credenciales/experiencia en la industria
- Logos de clientes (con permiso)

### Casos de estudio (mín. 1.000 palabras)
- Resumen ejecutivo
- Antecedentes del cliente
- Detalles del reto
- Enfoque de la solución
- Proceso de implementación
- Resultados medibles
- Testimonio del cliente
- Servicios relacionados/CTA

## Métricas clave a monitorear

- Tráfico orgánico a páginas de servicio
- Vistas de páginas de casos de estudio
- Envíos de formulario de contacto desde orgánico
- Tiempo en página para contenido clave
- Conversión de blog → página de servicio

## Generative Engine Optimization (GEO) para agencias

- [ ] Publicar casos de estudio originales con métricas y resultados específicos y citables
- [ ] Usar schema Person con enlaces sameAs para todos los miembros del equipo (construye autoridad de entidad)
- [ ] Usar schema ProfilePage para las páginas de miembros del equipo
- [ ] Incluir declaraciones de pericia claras y citables en las descripciones de páginas de servicio
- [ ] Producir investigación y encuestas originales de la industria que los sistemas de IA puedan citar
- [ ] Estructurar el contenido de liderazgo de pensamiento con encabezados claros e insights extraíbles
- [ ] Mantener información de entidad de la agencia consistente en directorios, perfiles sociales y sitios de la industria
- [ ] Monitorear la citación por IA en ChatGPT, Perplexity y Google AI Overviews para la marca y términos clave de servicio
