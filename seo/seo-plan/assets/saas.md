<!-- Actualizado: 2026-02-07 -->
# Plantilla de estrategia SEO para SaaS

## Características de la industria

- Ciclos de venta largos con múltiples puntos de contacto
- Toma de decisiones enfocada en funcionalidades
- Comportamiento de comparación de compra
- Fase de investigación intensa antes de la compra
- Consideraciones de integración y ecosistema

## Arquitectura de sitio recomendada

```
/
├── Inicio
├── /producto (o /plataforma)
│   ├── /funcionalidades
│   │   ├── /funcionalidad-1
│   │   ├── /funcionalidad-2
│   │   └── ...
│   ├── /integraciones
│   │   ├── /integracion-1
│   │   └── ...
│   └── /seguridad
├── /soluciones
│   ├── /por-industria
│   │   ├── /industria-1
│   │   └── ...
│   └── /por-caso-de-uso
│       ├── /caso-de-uso-1
│       └── ...
├── /precios
├── /clientes
│   ├── /casos-de-estudio
│   │   ├── /caso-de-estudio-1
│   │   └── ...
│   └── /testimonios
├── /recursos
│   ├── /blog
│   ├── /guias
│   ├── /webinars
│   ├── /plantillas
│   └── /glosario
├── /docs (o /ayuda)
│   └── /api
├── /empresa
│   ├── /acerca-de
│   ├── /empleo
│   ├── /prensa
│   └── /contacto
└── /comparar
    ├── /vs-competidor-1
    └── /vs-competidor-2
```

## Prioridades de contenido

### Páginas de alta prioridad
1. Homepage (propuesta de valor, prueba social)
2. Resumen de funcionalidades
3. Página de precios
4. Integraciones clave
5. Top 3-5 páginas de caso de uso

### Páginas de prioridad media
1. Páginas individuales de funcionalidad
2. Páginas de solución por industria
3. Casos de estudio (2-3 detallados)
4. Páginas de comparación (vs competidores)

### Enfoque de marketing de contenido
1. Fondo del embudo: Guías de comparación, calculadoras de ROI
2. Mitad del embudo: Guías prácticas, mejores prácticas
3. Parte alta del embudo: Tendencias de la industria, contenido educativo

## Recomendaciones de schema

| Tipo de página | Tipos de schema |
|-----------|-------------|
| Homepage | Organization, WebSite, SoftwareApplication |
| Producto/Funcionalidades | SoftwareApplication, Offer |
| Precios | SoftwareApplication, Offer (con precios) |
| Blog | Article, BlogPosting |
| Casos de estudio | Article, Organization (cliente) |
| Documentación | TechArticle |

## Métricas clave a monitorear

- Tráfico orgánico a la página de precios
- Registros a demo/trial desde orgánico
- Conversión de blog → página de precios
- Rankings de páginas de comparación
- Rendimiento de páginas de integración

## Páginas de comparación y alternativas

Las páginas de comparación están entre los tipos de contenido con mayor conversión para SaaS, con tasas de conversión del **4-7%** vs. 0.5-1.8% del contenido de blog estándar (el 35.8% de los marketers reporta que el contenido de comparación rinde "mejor que nunca", según la encuesta de Intergrowth de noviembre de 2025).

**Tipos de página recomendados:**
- `/{producto}-vs-{competidor}` — Comparación directa 1:1
- `/{competidor}-alternativa` — Apuntando a búsquedas de marca del competidor
- `/comparar/{categoria}` — Hub de comparación por categoría
- `/mejores-herramientas-{categoria}` — Páginas tipo roundup

**Mejores prácticas:**
- Incluir tablas de comparación estructuradas con precios, funcionalidades, pros/contras
- Ser factualmente preciso sobre los competidores — verificar afirmaciones con regularidad
- Incluir testimonios de clientes que se cambiaron
- Agregar schema FAQ para preguntas comunes de comparación (valioso para búsqueda con IA)
- Actualizar con regularidad — los datos de comparación obsoletos dañan la credibilidad
- Consultar la skill `seo-competitor-pages` para frameworks detallados

**Consideraciones legales:**
- El uso legítimo nominativo generalmente permite mencionar marcas de competidores con fines de comparación
- NO impliques respaldo ni afiliación
- NO hagas afirmaciones falsas o no verificables sobre los productos de competidores
- Distintas jurisdicciones tienen distintas leyes de marcas — consulta asesoría legal

## Consideraciones competitivas

- Monitorear lanzamientos de funcionalidades de competidores
- Rastrear estrategias de contenido de competidores
- Identificar brechas de keywords en cobertura de funcionalidades
- Estar atento a nuevas oportunidades de comparación

## Generative Engine Optimization (GEO) para SaaS

- [ ] Incluir comparaciones de funcionalidades claras y estructuradas que los sistemas de IA puedan parsear y citar
- [ ] Usar schema SoftwareApplication con listas completas de funcionalidades y precios
- [ ] Publicar datos de benchmark originales, casos de estudio y métricas de ROI
- [ ] Construir clusters de contenido en torno a categorías de producto y casos de uso clave
- [ ] Asegurar que las páginas de integración tengan descripciones claras y citables
- [ ] Estructurar la información de precios en tablas que la IA pueda extraer
- [ ] Monitorear las citas de IA en Google AI Overviews, ChatGPT y Perplexity
