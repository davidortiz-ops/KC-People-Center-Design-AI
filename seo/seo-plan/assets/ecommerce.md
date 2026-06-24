<!-- Actualizado: 2026-02-07 -->
# Plantilla de estrategia SEO para e-commerce

## Características de la industria

- Alta intención transaccional
- Comportamiento de comparación de productos
- Sensibilidad al precio
- Toma de decisiones visual primero
- Patrones de demanda estacional
- Listados competitivos en marketplaces

## Arquitectura de sitio recomendada

```
/
├── Inicio
├── /colecciones (o /categorias)
│   ├── /categoria-1
│   │   ├── /subcategoria-1
│   │   └── ...
│   ├── /categoria-2
│   └── ...
├── /productos
│   ├── /producto-1
│   ├── /producto-2
│   └── ...
├── /marcas
│   ├── /marca-1
│   └── ...
├── /ofertas
├── /novedades
├── /mas-vendidos
├── /guia-de-regalos
├── /blog
│   ├── /guias-de-compra
│   ├── /como-hacer
│   └── /tendencias
├── /acerca-de
├── /contacto
├── /envios
├── /devoluciones
└── /faq
```

## Recomendaciones de schema

| Tipo de página | Tipos de schema |
|-----------|-------------|
| Página de producto | Product, Offer, AggregateRating, Review, BreadcrumbList |
| Página de categoría | CollectionPage, ItemList, BreadcrumbList |
| Página de marca | Brand, Organization |
| Blog | Article, BlogPosting |

### Schema adicional de e-commerce (2025)

- **ProductGroup**: Úsalo para productos con variantes (talla, color). Envuelve entradas Product individuales con las propiedades `variesBy` y `hasVariant`. Ver `schema/templates.json`.
- **Certification**: Para certificaciones de producto (Energy Star, seguridad, orgánico). Reemplazó a EnergyConsumptionDetails (abril 2025). Usa `hasCertification` en Product.
- **OfferShippingDetails**: Incluye tarifa de envío, tiempo de manipulación y tiempo de tránsito. Crítico para la elegibilidad en Merchant Center.

> **Listados gratuitos de Google Merchant Center:** Los productos pueden aparecer en Google Shopping de forma gratuita. Asegúrate de que los datos estructurados Product estén en el HTML inicial renderizado por el servidor (no inyectados por JavaScript) con las propiedades requeridas: `name`, `image`, `price`, `priceCurrency`, `availability`.

> **Nota sobre renderizado JS:** Los datos estructurados de producto deben estar en el HTML inicial renderizado por el servidor — no inyectados dinámicamente vía JavaScript (según la guía de JS SEO de Google de diciembre 2025).

### Ejemplo de schema de producto
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Nombre del Producto",
  "image": ["https://example.com/product.jpg"],
  "description": "Descripción del producto",
  "sku": "SKU123",
  "brand": {
    "@type": "Brand",
    "name": "Nombre de la Marca"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/product"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "42"
  }
}
```

## Requisitos de contenido

### Páginas de producto (mín. 400 palabras)
- Descripciones de producto únicas (no el texto del fabricante)
- Aspectos destacados de funcionalidades
- Casos de uso / para quién es
- Tabla de especificaciones
- Guía de talla/ajuste (para ropa)
- Instrucciones de cuidado
- Reseñas de clientes

### Páginas de categoría (mín. 400 palabras)
- Introducción de la categoría
- Extracto de guía de compra
- Productos destacados
- Enlaces a subcategorías
- Opciones de filtro/orden

## Consideraciones técnicas

### Paginación
- Usa rel="next"/rel="prev" o "cargar más"
- Asegura que todos los productos sean rastreables
- Canonical hacia la página principal de categoría

### Navegación por facetas
- Noindex en combinaciones de filtros que creen contenido duplicado
- Usa etiquetas canonical apropiadamente
- Asegura que los filtros populares sean indexables

### Variaciones de producto
- URL única para el producto padre con variantes
- O URLs separadas con canonical hacia el padre
- Datos estructurados para todas las variantes

## Prioridades de contenido

### Alta prioridad
1. Páginas de categoría (nivel superior)
2. Páginas de productos más vendidos
3. Homepage
4. Guías de compra para categorías principales

### Prioridad media
1. Páginas de subcategoría
2. Páginas de marca
3. Contenido de comparación
4. Landing pages estacionales

### Temas de blog
- Guías de compra ("Cómo elegir...")
- Comparaciones de productos
- Reportes de tendencias
- Casos de uso e inspiración
- Guías de cuidado y mantenimiento

## Métricas clave a monitorear

- Ingresos desde búsqueda orgánica
- Rankings de páginas de producto
- Rankings de páginas de categoría
- Click-through rate (resultados enriquecidos)
- Valor promedio de pedido desde orgánico

## Generative Engine Optimization (GEO) para e-commerce

Las plataformas de búsqueda con IA responden cada vez más las consultas de producto directamente. Optimiza para la citación por IA:

- [ ] Incluir especificaciones de producto, dimensiones y materiales claros en formato estructurado
- [ ] Usar schema ProductGroup para productos con variantes
- [ ] Aportar fotografía de producto original con alt text descriptivo
- [ ] Incluir contenido genuino de reseñas de clientes (schema AggregateRating)
- [ ] Mantener datos de entidad de producto consistentes en todas las plataformas (sitio, Amazon, Merchant Center)
- [ ] Estructurar el contenido de comparación con tablas de funcionalidades claras que la IA pueda parsear
- [ ] Agregar contenido de FAQ detallado para preguntas comunes de producto
