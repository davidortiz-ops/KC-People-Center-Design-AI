---
name: seo-ecommerce
description: >
  Análisis SEO para e-commerce: validación de schema de producto, visibilidad en
  Google Shopping, brechas de keywords en marketplaces, optimización de páginas
  de producto, inteligencia de precios. Usar cuando el usuario diga "ecommerce
  SEO", "product SEO", "Google Shopping", "product schema", "Amazon SEO",
  "product listings", "shopping ads", "merchant SEO".
---

# Análisis SEO para E-commerce

## Referencia Rápida

| Comando | Propósito |
|---------|-----------|
| `/seo ecommerce <url>` | Análisis SEO completo de e-commerce del producto/tienda |
| `/seo ecommerce schema <url>` | Validación de schema de producto |

## 1. Análisis de Página de Producto

### Checklist SEO de Producto

#### Título (Title Tag)
- [ ] Contiene la keyword principal del producto
- [ ] Incluye el nombre de la marca
- [ ] Menos de 60 caracteres
- [ ] Formato: `[Nombre del Producto] - [Característica Clave] | [Marca]`

#### Meta Description
- [ ] Contiene keyword del producto + beneficio
- [ ] Incluye precio o "desde $XX" (activa el rich snippet)
- [ ] CTA presente (Compra ahora, Comprar, Envío gratis)
- [ ] Menos de 155 caracteres

#### Estructura de Encabezados
- [ ] Un solo H1 que coincida con el nombre del producto
- [ ] H2: Características, Especificaciones, Reseñas, Relacionados
- [ ] Sin H1 duplicados entre variantes

#### Imágenes del Producto
- [ ] Alt text incluye nombre del producto + característica
- [ ] Nombres de archivo descriptivos (no IMG_001.jpg)
- [ ] Formato WebP (con fallback a JPEG)
- [ ] Al menos 3 imágenes (principal, detalle, estilo de vida)
- [ ] 800px+ para elegibilidad en Google Shopping
- [ ] Lazy loading solo en imágenes debajo del pliegue

#### Enlazado Interno
- [ ] Breadcrumb: Inicio > Categoría > Subcategoría > Producto
- [ ] Productos relacionados (cross-sell / upsell)
- [ ] Enlace de vuelta a categoría con anchor rico en keywords

#### Calidad del Contenido
- [ ] Descripción única del producto (no copia del fabricante)
- [ ] 200+ palabras para el cuerpo de la descripción
- [ ] Tabla de especificaciones presente
- [ ] Reseñas de usuarios en la página (señales UGC)

### Puntuación

| Categoría | Peso |
|-----------|------|
| Completitud del schema | 25% |
| Título y meta | 15% |
| Optimización de imágenes | 20% |
| Calidad del contenido | 20% |
| Enlazado interno | 10% |
| Técnico | 10% |

## 2. Mejora del Schema de Producto

Validar y generar schema de Producto siguiendo los requerimientos de Google.

### Propiedades Requeridas

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "",
  "image": [""],
  "description": "",
  "brand": { "@type": "Brand", "name": "" },
  "offers": {
    "@type": "Offer",
    "url": "",
    "priceCurrency": "USD",
    "price": "0.00",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "" }
  }
}
```

### Propiedades Recomendadas
- sku, gtin13, gtin14, mpn
- aggregateRating (estrellas + cantidad de reseñas)
- review (individual)
- shippingDetails
- hasMerchantReturnPolicy

### Reglas de Validación

1. price = string numérico, no "$29.99"
2. availability = URL completa del enum de Schema.org
3. image = array con 1+ URLs en alta resolución
4. priceCurrency = ISO 4217
5. brand.name no vacío
6. Fechas en priceValidUntil = ISO 8601
7. aggregateRating requiere ratingValue + reviewCount

## 3. Brechas de Keywords en Marketplaces

Identificar desajustes entre visibilidad orgánica y en Shopping.

| Tipo de Brecha | Significado | Acción |
|----------------|-------------|--------|
| Solo Orgánico | Rankings pero sin anuncios Shopping | Crear feed en Merchant Center, pujar por keywords |
| Solo Shopping | Visibilidad en Shopping pero orgánico débil | Crear contenido (guías de compra, páginas comparativas) |
| Ambos Presentes | Visible en ambos | Optimizar: asegurar consistencia de precios, mejorar schema |

## Salida

```
## Reporte SEO de E-commerce: [URL]

### Puntuación General: XX/100

### SEO de Página de Producto
- Completitud del Schema: XX/100
- Título y Meta: XX/100
- Optimización de Imágenes: XX/100
- Calidad del Contenido: XX/100
- Enlazado Interno: XX/100

### Schema de Producto
- Campos requeridos: ✅/❌
- Campos recomendados: X/7
- Errores de validación: X

### Recomendaciones Principales
1. [Crítico] ...
2. [Alto] ...
3. [Medio] ...
```

## Integración entre Skills

| Skill | Punto de Integración |
|-------|----------------------|
| **seo-schema** | Generación y validación de schema de producto |
| **seo-images** | Optimización de imágenes de producto |
| **seo-content** | Análisis E-E-A-T de descripciones de producto |
| **seo-technical** | Core Web Vitals para páginas de producto |
