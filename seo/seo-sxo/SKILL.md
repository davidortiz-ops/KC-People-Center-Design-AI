---
name: seo-sxo
description: >
  Search Experience Optimization: Lee Google SERPs al revés para detectar
  page-type mismatches, deriva user stories de señales de intent de búsqueda,
  y scorea páginas desde múltiples perspectivas de persona. Identifica por qué
  páginas bien optimizadas fallan en rankear. Úsala cuando el usuario diga "SXO",
  "search experience", "page type mismatch", "análisis SERP", "user story",
  "persona scoring", "por qué mi página no rankea" o "intent mismatch".
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

# Search Experience Optimization (SXO)

SXO puentea SEO (lo que Google recompensa) con UX (lo que los usuarios necesitan).
Una página puede scorear 95/100 en SEO técnico y aún así fallar en rankear
porque es el **tipo de página incorrecto** para la keyword.

## Insight Principal

Si Google muestra 8 product pages y 2 comparison pages para tu keyword,
tu blog post nunca va a posicionarse — sin importar qué tan bien optimizado esté.

## Comandos

| Comando | Propósito |
|---------|----------|
| `/seo sxo <url>` | Análisis SXO completo (auto-detecta keyword desde la página) |
| `/seo sxo <url> <keyword>` | Análisis SXO completo para keyword específica |
| `/seo sxo personas <url>` | Scoring solo de personas |

## Pipeline de Ejecución

### Paso 1: Adquisición del Target

Obtener URL vía petición HTTP. Extraer: title, H1, meta description,
jerarquía de encabezados, recuento de palabras, schema, CTAs.

### Paso 2: Análisis Inverso de SERP

1. Buscar en Google la keyword objetivo (WebSearch)
2. Para cada resultado orgánico top 10, registrar:
   - URL y nivel de domain authority
   - Tipo de página (clasificar usando taxonomía)
   - Formato de contenido (long-form, listicle, how-to, comparison)
   - Estimación de recuento de palabras
   - Tipos de schema
3. Calcular consenso SERP:
   - Tipo de página dominante (>60% = fuerte, 40-60% = mixto, <40% = fragmentado)
   - Expectativas de profundidad de contenido
   - Expectativa de schema

### Paso 3: Detección de Page-Type Mismatch

| Tipo Target | SERP Espera | Severidad | Recomendación |
|-------------|-------------|----------|----------------|
| Blog Post | Product Pages | CRÍTICO | Crear página de producto dedicada |
| Blog Post | Comparison | ALTA | Reestructurar como comparación |
| Product | Informational | ALTA | Agregar contenido educativo |
| Landing Page | Tool/Calculator | ALTA | Construir herramienta interactiva |
| Service Page | Local Results | MEDIA | Agregar señales de ubicación |
| Coincidencia de tipo | - | ALINEADO | Enfocar en profundidad de contenido |

### Paso 4: Derivación de User Stories

De señales SERP, derivar user stories:

1. **Preguntas PAA** → brechas de conocimiento y preocupaciones
2. **Temas de anuncios** → disparadores comerciales
3. **Búsquedas relacionadas** → journey de búsqueda
4. **Formato de featured snippet** → estructura de respuesta esperada

Generar 3-5 user stories:
```
Como [persona],
quiero [objetivo de la intención de búsqueda],
porque [impulsor emocional],
pero estoy bloqueado por [barrera de PAA / búsquedas relacionadas].
```

### Paso 5: Gap Analysis — SXO Score

| Dimensión | Qué Comparar | Peso |
|-----------|----------------|--------|
| Tipo de Página | Target vs dominante SERP | 15 |
| Profundidad de Contenido | Recuento de palabras, cobertura temática | 15 |
| Señales UX | Claridad de CTA, layout mobile | 15 |
| Schema Markup | Presente vs esperado | 15 |
| Riqueza Multimedia | Imágenes, video vs norma SERP | 15 |
| Señales de Autoridad | Marcadores E-E-A-T, credenciales | 15 |
| Frescura | Última actualización, actualidad del contenido | 10 |

**Total: 0-100 SXO Score** (menor = gap más grande)

### Paso 6: Scoring Basado en Personas

Derivar 4-7 personas de señales SERP. Puntuar en 4 dimensiones (25 pts cada una):
- **Relevancia**: ¿La página aborda la necesidad de esta persona?
- **Claridad**: ¿La persona encuentra respuesta en 10 segundos?
- **Confianza**: ¿Señales de confianza adecuadas para esta persona?
- **Acción**: ¿Siguiente paso claro para esta persona?

## Salida

```
## Análisis SXO: [URL]
### Keyword objetivo: [keyword]

### 1. Panorama SERP
- Tipo de página dominante: [tipo] ([confianza]%)
- Features SERP: [lista]
- Norma de profundidad de contenido: [rango de palabras]

### 2. Alineación de Tipo de Página
- Tu tipo de página: [tipo]
- SERP espera: [tipo]
- Veredicto: [ALINEADO | DESALINEADO (severidad)]

### 3. User Stories
[3-5 user stories con señales fuente]

### 4. Gap Analysis (SXO Score: XX/100)
[Desglose de 7 dimensiones]

### 5. Puntuaciones por Persona
[4-7 tarjetas de persona]

### 6. Acciones Prioritarias
```

## Integración entre Skills

| Hallazgo | Derivar A |
|---------|-------------|
| Brechas E-E-A-T | `/seo content` |
| Schema faltante | `/seo schema` |
| Intención local detectada | `/seo local` |
| Brechas de profundidad de contenido | `/seo page` |
| Problemas técnicos | `/seo technical` |
| Brechas de imágenes/media | `/seo images` |

## Manejo de Errores

| Error | Resolución |
|-------|-----------|
| Fallo al obtener URL | Verificar accesibilidad de la URL |
| No se detectó keyword | Preguntar al usuario por keyword objetivo |
| WebSearch devuelve <5 resultados | Proceder con datos disponibles |
| Página target renderizada con JS | Notar limitación |
