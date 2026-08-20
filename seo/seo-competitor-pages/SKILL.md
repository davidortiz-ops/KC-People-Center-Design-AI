---
name: seo-competitor-pages
description: >
  Genera páginas de comparación y alternativas optimizadas para SEO. Cubre
  layouts "X vs Y", páginas "alternatives to X", matrices de características,
  markup de schema y optimización de conversión. Usar cuando el usuario diga
  "comparison page", "vs page", "alternatives page", "competitor comparison"
  o "X vs Y".
license: Proprietary - Pragma (uso interno y confidencial)
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
  - WebSearch
metadata:
  version: "1.0"
  author: Pragma
---

# Páginas de Comparación y Alternativas

Crear páginas de comparación y alternativas de alta conversión que apunten
a keywords de intención competitiva con contenido preciso y estructurado.

## Tipos de Página

### 1. Páginas de Comparación "X vs Y"
- Comparación directa cabeza a cabeza entre dos productos/servicios
- Análisis equilibrado característica por característica
- Veredicto claro o recomendación con justificación
- Keyword objetivo: `[Producto A] vs [Producto B]`

### 2. Páginas de "Alternativas a X"
- Lista de alternativas a un producto/servicio específico
- Cada alternativa con resumen breve, pros/contra, mejor caso de uso
- Keyword objetivo: `[Producto] alternatives`, `best alternatives to [Producto]`

### 3. Páginas de Recopilación "Mejores Herramientas de [Categoría]"
- Lista curada de las mejores herramientas/servicios en una categoría
- Criterios de ranking claramente establecidos
- Keyword objetivo: `best [categoría] tools [año]`, `top [categoría] software`

### 4. Páginas de Tabla Comparativa
- Matriz de características con múltiples productos en columnas
- Ordenable/filtrable si es interactivo
- Keyword objetivo: `[categoría] comparison`, `[categoría] comparison chart`

## Generación de Tabla Comparativa

### Layout de Matriz de Características
```
| Característica    | Tu Producto | Competidor A | Competidor B |
|------------------|:------------:|:------------:|:------------:|
| Característica 1 | ✅           | ✅           | ❌           |
| Característica 2 | ✅           | ⚠️ Parcial   | ✅           |
| Característica 3 | ✅           | ❌           | ❌           |
| Precio (desde)   | $X/mes       | $Y/mes       | $Z/mes       |
| Plan Gratuito    | ✅           | ❌           | ✅           |
```

### Requisitos de Precisión de Datos
- Todas las afirmaciones sobre características deben ser verificables desde fuentes públicas
- Los precios deben estar actualizados (incluir nota "a partir de [fecha]")
- Frecuencia de actualización: revisar trimestralmente o cuando los competidores lancen cambios importantes
- Enlazar a la fuente para cada dato del competidor cuando sea posible

## Recomendaciones de Schema Markup

### Product Schema con AggregateRating
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Nombre del Producto]",
  "description": "[Descripción del Producto]",
  "brand": {
    "@type": "Brand",
    "name": "[Nombre de la Marca]"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[Puntaje]",
    "reviewCount": "[Cantidad]",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### SoftwareApplication (para comparaciones de software)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Nombre del Software]",
  "applicationCategory": "[Categoría]",
  "operatingSystem": "[SO]",
  "offers": {
    "@type": "Offer",
    "price": "[Precio]",
    "priceCurrency": "USD"
  }
}
```

### ItemList (para páginas de recopilación)
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Mejores Herramientas de [Categoría] [Año]",
  "itemListOrder": "https://schema.org/ItemListOrderDescending",
  "numberOfItems": "[Cantidad]",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "[Nombre del Producto]",
      "url": "[URL del Producto]"
    }
  ]
}
```

## Orientación de Keywords

### Patrones de Intención de Comparación
| Patrón | Ejemplo | Señal de Volumen de Búsqueda |
|---------|---------|---------------------|
| `[A] vs [B]` | "Slack vs Teams" | Alto |
| `[A] alternative` | "Figma alternatives" | Alto |
| `[A] alternatives [año]` | "Notion alternatives 2026" | Alto |
| `best [categoría] tools` | "best project management tools" | Alto |
| `[A] vs [B] for [caso de uso]` | "AWS vs Azure for startups" | Medio |
| `[A] review [año]` | "Monday.com review 2026" | Medio |
| `[A] vs [B] pricing` | "HubSpot vs Salesforce pricing" | Medio |
| `is [A] better than [B]` | "is Notion better than Confluence" | Medio |

### Fórmulas para Title Tag
- X vs Y: `[A] vs [B]: [Diferenciador Clave] ([Año])`
- Alternativas: `[N] Mejores Alternativas a [A] en [Año] (Gratis y de Pago)`
- Recopilación: `[N] Mejores Herramientas de [Categoría] en [Año] — Comparadas y Clasificadas`

### Patrones de H1
- Coincidir con la intención del title tag
- Incluir keyword primaria de forma natural
- Mantener por debajo de 70 caracteres

## Layouts Optimizados para Conversión

### Ubicación de CTA
- **Above fold**: Resumen breve de comparación con CTA principal
- **Después de la tabla comparativa**: CTA "Prueba [Tu Producto] gratis"
- **Final de la página**: Recomendación final con CTA
- Evitar CTAs agresivos en secciones de descripción del competidor (reduce confianza)

### Secciones de Prueba Social
- Testimonios de clientes relevantes a los criterios de comparación
- Calificaciones de G2/Capterra/TrustPilot (con enlaces a la fuente)
- Casos de estudio que muestren migración desde el competidor
- Historias de "Cambié desde [Competidor]"

### Destacados de Precios
- Tabla comparativa de precios clara
- Destacar ventajas de valor (no solo el precio más bajo)
- Incluir costos ocultos (tarifas de configuración, precio por usuario, cargos por excedente)
- Enlazar a la página de precios completa

### Señales de Confianza
- Marca de tiempo "Última actualización [fecha]"
- Autor con experiencia relevante
- Divulgación de metodología (cómo se realizaron las comparaciones)
- Divulgación de afiliación con producto propio

## Pautas de Equidad

- **Precisión**: Toda la información del competidor debe ser verificable desde fuentes públicas
- **Sin difamación**: Nunca hacer afirmaciones falsas o engañosas sobre competidores
- **Citar fuentes**: Enlazar a sitios web de competidores, sitios de reseñas o documentación
- **Actualizaciones oportunas**: Revisar y actualizar cuando los competidores lancen cambios importantes
- **Divulgar afiliación**: Indicar claramente cuál es tu producto
- **Presentación equilibrada**: Reconocer honestamente las fortalezas del competidor
- **Precisión de precios**: Incluir exenciones de responsabilidad "a partir de [fecha]" en todos los datos de precios
- **Verificación de características**: Probar las características del competidor cuando sea posible, citar documentación en caso contrario

## Internal Linking

- Enlazar a las páginas de tu propio producto/servicio desde las secciones de comparación
- Enlazar cruzadamente entre páginas de comparación relacionadas (ej. "A vs B" enlaza a "A vs C")
- Enlazar a páginas de características específicas al discutir características individuales
- Breadcrumb: Inicio > Comparaciones > [Esta Página]
- Sección de comparaciones relacionadas al final de la página
- Enlazar a casos de estudio y testimonios mencionados en la comparación

## Salida

### Template de Página de Comparación
- `COMPARISON-PAGE.md` — Estructura de página lista para implementar con secciones
- Tabla de matriz de características
- Esquema de contenido con objetivos de word count (mínimo 1,500 palabras)

### Schema Markup
- `comparison-schema.json` — Product/SoftwareApplication/ItemList JSON-LD

### Estrategia de Keywords
- Keywords primarias y secundarias
- Oportunidades long-tail relacionadas
- Brechas de contenido vs páginas de competidores existentes

### Recomendaciones
- Mejoras de contenido para páginas de comparación existentes
- Oportunidades de nuevas páginas de comparación
- Adiciones de schema markup
- Sugerencias de optimización de conversión
