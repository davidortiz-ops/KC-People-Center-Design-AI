<!-- Actualizado: 2026-02-07 -->
# Plantilla de estrategia SEO para negocio genérico

## Visión general

Esta plantilla aplica a negocios que no encajan claramente en las categorías SaaS, servicio local, e-commerce, publisher o agencia. Personalízala según tu modelo de negocio específico.

## Arquitectura de sitio recomendada

```
/
├── Inicio
├── /productos (o /servicios)
│   ├── /producto-1
│   ├── /producto-2
│   └── ...
├── /soluciones (si aplica)
│   ├── /solucion-1
│   └── ...
├── /acerca-de
│   ├── /equipo
│   ├── /historia
│   └── /valores
├── /recursos
│   ├── /blog
│   ├── /guias
│   ├── /faq
│   └── /glosario
├── /contacto
├── /soporte
└── /legal
    ├── /privacidad
    └── /terminos
```

## Principios universales de SEO

### Cada página debe tener
- Title tag único (30-60 caracteres)
- Meta description única (120-160 caracteres)
- Un único H1 que coincida con la intención de la página
- Jerarquía de encabezados lógica (H1→H2→H3)
- Enlaces internos a contenido relacionado
- Llamado a la acción claro

### Schema para todos los sitios
| Tipo de página | Tipos de schema |
|-----------|-------------|
| Homepage | Organization, WebSite |
| Acerca de | Organization, AboutPage |
| Contacto | ContactPage |
| Blog | Article, BlogPosting |
| FAQ | (FAQPage solo para gobierno/salud) |
| Producto/Servicio | Product o Service |

## Estándares de calidad de contenido

### Conteo mínimo de palabras
| Tipo de página | Palabras mín. |
|-----------|-----------|
| Homepage | 500 |
| Producto/Servicio | 800 |
| Post de blog | 1.500 |
| Página "Acerca de" | 400 |
| Landing page | 600 |

### Esenciales de E-E-A-T
1. **Experiencia**: Comparte ejemplos reales y casos de estudio
2. **Pericia**: Muestra credenciales y cualificaciones
3. **Autoridad**: Gana menciones y citas
4. **Confiabilidad**: Información de contacto completa, políticas visibles

## Fundamentos técnicos

### Imprescindibles
- [ ] HTTPS habilitado
- [ ] Diseño responsivo para móviles
- [ ] robots.txt configurado
- [ ] Sitemap XML enviado
- [ ] Google Search Console verificado
- [ ] Core Web Vitals aprobando (LCP <2.5s, INP <200ms, CLS <0.1)

### Recomendables
- [ ] Datos estructurados en páginas clave
- [ ] Estrategia de enlazado interno
- [ ] Página de error 404 optimizada
- [ ] Cadenas de redirección eliminadas
- [ ] Optimización de imágenes (WebP, lazy loading)

## Prioridades de contenido

### Fase 1: Cimientos (semanas 1-4)
1. Optimización de homepage
2. Páginas principales de producto/servicio
3. Páginas "Acerca de" y contacto
4. Implementación básica de schema

### Fase 2: Expansión (semanas 5-12)
1. Lanzamiento del blog (2-4 posts/mes)
2. Página de FAQ
3. Páginas adicionales de producto/servicio
4. Auditoría de enlazado interno

### Fase 3: Crecimiento (semanas 13-24)
1. Publicación de contenido consistente
2. Outreach de link building
3. Optimización GEO
4. Optimización de rendimiento

### Fase 4: Autoridad (meses 7-12)
1. Contenido de liderazgo de pensamiento (thought leadership)
2. Investigación original
3. PR y menciones en medios
4. Schema avanzado

## Métricas clave a monitorear

- Tráfico orgánico (general y por sección)
- Rankings de keywords (de marca y sin marca)
- Tasa de conversión desde orgánico
- Páginas indexadas
- Puntuaciones de Core Web Vitals
- Backlinks adquiridos

## Puntos de personalización

Ajusta esta plantilla según:

1. **Modelo de negocio**: B2B vs B2C vs D2C
2. **Alcance geográfico**: Local, nacional o internacional
3. **Tipo de contenido**: Enfocado en producto vs intensivo en contenido
4. **Nivel de competencia**: Nicho vs mercado competitivo
5. **Recursos**: Presupuesto y capacidad del equipo

## Checklist de Generative Engine Optimization (GEO)

- [ ] Incluir hechos y estadísticas claros y citables que los sistemas de IA puedan extraer y citar
- [ ] Usar datos estructurados (Schema.org) para ayudar a los sistemas de IA a entender el contenido
- [ ] Construir autoridad temática mediante clusters de contenido exhaustivos
- [ ] Aportar datos, investigación o perspectivas únicas que la IA no pueda encontrar en otro lugar
- [ ] Mantener información de entidad consistente (marca, personas, productos) en toda la web
- [ ] Estructurar el contenido con encabezados claros, definiciones y formatos paso a paso
- [ ] Considerar agregar un archivo `llms.txt` en la raíz del sitio (convención emergente para crawlers de IA — Google lo trata como un archivo de texto normal)
- [ ] Monitorear las citas de IA en Google AI Overviews, ChatGPT, Perplexity y Bing Copilot
