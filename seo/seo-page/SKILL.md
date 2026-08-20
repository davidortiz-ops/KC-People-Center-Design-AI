---
name: seo-page
description: >
  Análisis profundo de página individual SEO cubriendo elementos on-page, calidad de
  contenido, meta tags técnicos, schema, imágenes y rendimiento. Úsala cuando el
  usuario diga "analiza esta página", "verifica SEO de página", o proporcione una
  URL única para revisión.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
---

# Análisis de Página Individual

> **Antes del análisis, obtén datos reales de GSC + GA4** (si tu stack cuenta con un
> script para ello; ajusta la ruta a tu proyecto):
> ```bash
> python <tu-stack>/scripts/fetch_gsc_ga4.py <url> --pretty
> ```

## Qué Analizar

### SEO On-Page
- Title tag: 50-60 caracteres, incluye keyword principal, único
- Meta description: 150-160 caracteres, convincente, incluye keyword
- H1: exactamente uno, coincide con la intención de la página, incluye keyword
- H2-H6: jerarquía lógica (sin niveles saltados), descriptivos
- URL: corta, descriptiva, con guiones, sin parámetros
- Enlaces internos: suficientes, anchor text relevante, sin páginas huérfanas
- Enlaces externos: a fuentes autoritativas, cantidad razonable

### Calidad del Contenido
- Recuento de palabras vs mínimos por tipo de página (ver quality-gates.md)
- Legibilidad: puntuación Flesch Reading Ease, nivel de grado
- Densidad de keyword: natural (1-3%), variaciones semánticas presentes
- Señales E-E-A-T: biografía del autor, credenciales, marcadores de experiencia de primera mano
- Frescura del contenido: fecha de publicación, última fecha de actualización

### Elementos Técnicos
- Canonical tag: presente, auto-referenciado o correcto
- Meta robots: index/follow a menos que esté bloqueado intencionalmente
- Open Graph: og:title, og:description, og:image, og:url
- Twitter Card: twitter:card, twitter:title, twitter:description
- Hreflang: si es multi-idioma, implementación correcta

### Schema Markup
- Detectar todos los tipos (JSON-LD preferido)
- Validar propiedades requeridas
- Identificar oportunidades faltantes
- NUNCA recomendar HowTo (obsoleto) ni FAQ (restringido a gov/salud)

### Imágenes
- Texto alternativo: presente, descriptivo, incluye keywords donde sea natural
- Tamaño de archivo: marcar >200KB (advertencia), >500KB (crítico)
- Formato: recomendar WebP/AVIF sobre JPEG/PNG
- Dimensiones: width/height definidos para prevención de CLS
- Carga diferida: loading="lazy" en imágenes debajo del pliegue

### Core Web Vitals (solo referencia — no medibles desde HTML solo)
- Señalar posibles problemas de LCP (imágenes héroe enormes, recursos que bloquean renderizado)
- Señalar posibles problemas de INP (JS pesado, sin async/defer)
- Señalar posibles problemas de CLS (dimensiones de imagen faltantes, contenido inyectado)

## Salida

### Tarjeta de Puntuación de Página
```
Puntuación General: XX/100

SEO On-Page:     XX/100  ████████░░
Calidad Contenido: XX/100  ██████████
Técnico:         XX/100  ███████░░░
Schema:          XX/100  █████░░░░░
Imágenes:        XX/100  ████████░░
```

### Problemas Encontrados
Organizados por prioridad: Crítico → Alto → Medio → Bajo

### Recomendaciones
Mejoras específicas y accionables con impacto esperado

### Sugerencias de Schema
Código JSON-LD listo para usar para oportunidades detectadas

## Integración con SXO

Si la página no rankea a pesar de buena optimización, recomendar:
```bash
/seo sxo <url> <keyword>
```

Esto detecta page-type mismatch (ej: blog post cuando Google espera product pages).

## Integración entre Skills

| Hallazgo | Skill |
|---------|-------|
| La página no rankea a pesar de buen SEO | `/seo sxo <url> <keyword>` |
| Problemas de calidad de contenido | `/seo content <url>` |
| Schema faltante | `/seo schema <url>` |
| Problemas de imágenes | `/seo images <url>` |
| Problemas técnicos | `/seo technical <url>` |
| Preparación para búsqueda con IA | `/seo geo <url>` |
| Datos reales de GSC + oportunidades de keywords | `/seo google <url>` |

## Salida Bilingüe

Cuando el sitio analizado está en inglés, generar dos versiones:
- `PAGE-ANALYSIS.md` (inglés)
- `PAGE-ANALYSIS-ES.md` (español)
