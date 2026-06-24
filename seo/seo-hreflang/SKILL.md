---
name: seo-hreflang
description: >
  Reglas completas para sitios web multilingües y multirregionales: implementación
  de hreflang (HTML, cabeceras HTTP o sitemap), geotargeting, páginas adaptativas por
  ubicación, validación de códigos idioma/región y errores comunes. Úsala cuando el
  usuario diga "hreflang", "SEO internacional", "i18n", "multilenguaje",
  "multirregional", "geotargeting", "x-default", "language tags", o cuando agregue
  variantes de idioma/región a páginas existentes.
version: 2.0.0
---

# SEO: Internacional y Multilenguaje

## Cuándo usarlo
Usa esta skill cuando:
- Construyas un sitio web multilingüe (contenido en varios idiomas).
- Construyas un sitio web multirregional (mismo idioma, diferentes países — ej., inglés de EE. UU. vs. Reino Unido).
- Agregues variantes de idioma/región a páginas existentes.
- Implementes etiquetas `hreflang` mediante HTML, cabeceras HTTP o sitemaps.
- Manejes páginas adaptativas por ubicación que cambian el contenido según la ubicación del usuario.
- Configures geotargeting para países específicos.
- Gestiones contenido duplicado entre dominios (ej., `example.de` y `example.com/de/`).

## Entradas requeridas
- Idiomas y regiones objetivo (ej., `en-US`, `es-ES`, `fr-FR`, `zh-Hans`).
- Estrategia de URL: subdirectorios (`/en/`), subdominios (`en.example.com`) o dominios separados (`example.de`).
- Si el contenido está completamente traducido, parcialmente localizado o generado por usuarios (ej., foros).
- Si el sitio sirve contenido diferente según la IP del usuario o la cabecera `Accept-Language`.

## Procedimiento

### 1. Entender Multilingüe vs Multirregional
Son conceptos distintos según Google:
- **Multilingüe**: Contenido en varios idiomas (ej., sitio en inglés + francés para Canadá).
- **Multirregional**: Mismo idioma dirigido a diferentes países (ej., `en-US` vs `en-GB`).
- Un sitio puede ser **ambos** (ej., un sitio canadiense con contenido en inglés y francés dirigido específicamente a Canadá).

### 2. Usa URLs Diferentes para Cada Versión de Idioma
Google recomienda firmemente **URLs separadas** para cada versión de idioma — nunca cambies el contenido basándote solo en cookies o configuración del navegador.

> **Crítico:** Googlebot rastrea desde EE. UU. y NO envía una cabecera `Accept-Language`. Si sirves contenido diferente según la IP o las cabeceras, Googlebot solo verá la versión en inglés de EE. UU.

```html
<!-- ✅ CORRECTO: URLs separadas por idioma -->
https://example.com/en/about
https://example.com/es/about
https://example.com/fr/about

<!-- ❌ INCORRECTO: Misma URL, contenido cambia según cookie/IP -->
https://example.com/about  (muestra inglés o español según la ubicación)
```

### 3. Estrategia de URL

| Estrategia | Ejemplo | Mejor para |
|---|---|---|
| Subdirectorios | `example.com/en/`, `example.com/es/` | La mayoría de sitios — autoridad de dominio única, más simple |
| Subdominios | `en.example.com`, `es.example.com` | Equipos grandes con infraestructura separada |
| ccTLDs | `example.com`, `example.de`, `example.es` | Marca local fuerte o geotargeting por país |

- Usa **codificación UTF-8** para palabras localizadas en las URLs (ej., `example.com/über-uns/`).
- Los nombres de dominio internacionalizados (IDN) están bien, pero escapa las URLs correctamente al enlazar.

### 4. Etiquetas Hreflang — Tres Métodos

Google admite tres formas de declarar variantes de idioma. **Usa solo un método por página** (no los mezcles):

#### Método A: Etiquetas HTML `<link>` (más común)
```html
<head>
  <!-- Autorreferencia + todas las versiones alternativas -->
  <link rel="alternate" hreflang="en" href="https://example.com/en/about" />
  <link rel="alternate" hreflang="es" href="https://example.com/es/about" />
  <link rel="alternate" hreflang="fr" href="https://example.com/fr/about" />
  <link rel="alternate" hreflang="de-CH" href="https://example.com/de-ch/about" />
  <link rel="alternate" hreflang="x-default" href="https://example.com/en/about" />
</head>
```

#### Método B: Cabeceras HTTP (para PDFs y archivos no HTML)
```http
Link: <https://example.com/file.pdf>; rel="alternate"; hreflang="en",
      <https://de.example.com/file.pdf>; rel="alternate"; hreflang="de",
      <https://de-ch.example.com/file.pdf>; rel="alternate"; hreflang="de-ch"
```

#### Método C: Sitemap XML
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/en/about</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/about" />
    <xhtml:link rel="alternate" hreflang="es" href="https://example.com/es/about" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/about" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/en/about" />
  </url>
  <url>
    <loc>https://example.com/es/about</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/about" />
    <xhtml:link rel="alternate" hreflang="es" href="https://example.com/es/about" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/about" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/en/about" />
  </url>
</urlset>
```

### 5. Reglas de Hreflang (según Google)
Estas reglas aplican a los TRES métodos:

1. **El enlace bidireccional es OBLIGATORIO.** Si la página A referencia a la página B, la página B DEBE referenciar a la página A. Si no, las etiquetas hreflang se ignoran.
2. **La autorreferencia es obligatoria.** Cada página debe incluir su propia URL en el conjunto hreflang.
3. **Usa URLs completamente calificadas.** Siempre `https://example.com/page`, nunca `//example.com/page` o `/page`.
4. **Incluye siempre `x-default`.** Apunta a la página de respaldo para usuarios cuyo idioma/región no coincide con ninguna variante.
5. **Usa código de idioma ISO 639-1 + región opcional ISO 3166-1 Alpha-2.** El código de idioma DEBE ir primero.

```
✅ Códigos correctos:  en, en-US, en-GB, de, de-CH, zh-Hans, zh-Hant, pt-BR
❌ Códigos inválidos:  be (bielorruso, no Bélgica), eu (no es una región válida), uk (no es GB), es-419 (no soportado)
```

> **Trampa de Bélgica:** Bélgica tiene 3 idiomas. Usa `fr-BE`, `nl-BE`, `de-BE` — nunca solo `be` (ese es el código del idioma bielorruso).

### 6. Detección de Idioma — Cómo lo Determina Realmente Google
Google determina el idioma de la página a partir del **contenido visible**, NO de:
- El atributo `<html lang="">`
- Las cabeceras HTTP
- La estructura de la URL

Establece `<html lang="">` por accesibilidad, pero debes saber que Google se basa en el contenido de texto real. No mezcles idiomas en una sola página — mantén navegación, contenido y pie de página en el mismo idioma.

### 7. Páginas Adaptativas por Ubicación
Si tu servidor devuelve contenido diferente según la IP del visitante o `Accept-Language`:

- **Problema:** Googlebot rastrea desde IPs de EE. UU. sin una cabecera `Accept-Language`, por lo que solo ve la versión en inglés estadounidense.
- **Solución:** Usa anotaciones `hreflang` para informar a Google sobre todas las versiones, Y asegúrate de que cada versión tenga su propia URL rastreable.

### 8. Contenido Duplicado entre Dominios
Si el mismo contenido existe en múltiples dominios (ej., `example.de` y `example.com/de/`):
- Elige una versión preferida.
- Usa `rel="canonical"` en la versión no preferida apuntando a la preferida.
- Usa etiquetas `hreflang` en la versión canónica para declarar todas las variantes de idioma.

```html
<!-- En example.com/de/ (no preferido) -->
<link rel="canonical" href="https://example.de/" />

<!-- En example.de/ (preferido) -->
<link rel="canonical" href="https://example.de/" />
<link rel="alternate" hreflang="de" href="https://example.de/" />
<link rel="alternate" hreflang="en" href="https://example.com/" />
```

### 9. Mejores Prácticas de Contenido y UX
- **Nunca redirijas automáticamente** según la IP o ubicación sin consentimiento del usuario. Usa un banner/aviso en su lugar.
- **Proporciona un selector de idioma visible** en todas las páginas.
- **Traduce todo** — títulos, meta descripciones, navegación, pies de página. No solo el contenido del cuerpo.
- **Usa un comodín.** Si tienes `en-IE`, `en-CA`, `en-AU`, también proporciona un `en` genérico para todas las demás ubicaciones de habla inglesa.

```html
<!-- ✅ Ejemplo de selector de idioma -->
<nav aria-label="Selector de idioma">
  <a href="/en/about" hreflang="en" lang="en">English</a>
  <a href="/es/about" hreflang="es" lang="es">Español</a>
  <a href="/fr/about" hreflang="fr" lang="fr">Français</a>
</nav>
```

### 10. Implementación en Frameworks

```jsx
// Next.js App Router (exportación de metadata)
export const metadata = {
  alternates: {
    canonical: 'https://example.com/en/about',
    languages: {
      'en': 'https://example.com/en/about',
      'es': 'https://example.com/es/about',
      'fr': 'https://example.com/fr/about',
      'x-default': 'https://example.com/en/about',
    },
  },
};
```

## Verificación
- **Validación de hreflang:** Usa el [Generador de Hreflang de Aleyda Solis](https://www.aleydasolis.com/english/international-seo-tools/hreflang-tags-generator/) para validar etiquetas.
- **Verificación bidireccional:** Por cada hreflang en la página A que apunte a la página B, confirma que la página B apunte de vuelta a la página A.
- **Search Console:** Revisa el informe de Segmentación Internacional para errores de hreflang y cobertura.
- **Verificación de sitemap:** Confirma que los sitemaps multilingües incluyan elementos `xhtml:link` para cada idioma por URL.
- **Verificación de HTML lang:** Confirma que `<html lang="...">` coincida con el idioma del contenido visible de la página.
- **Prueba de páginas adaptativas por ubicación:** Rastrea tu sitio desde una IP de EE. UU. — ¿aparece la versión predeterminada correcta? Luego prueba con una VPN desde otro país.
- **Consistencia canonical + hreflang:** Asegúrate de que las etiquetas canonical no entren en conflicto con hreflang (canonical debe apuntar a la misma URL que hreflang declara para ese idioma).

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| Versión de idioma incorrecta posicionada | Etiquetas hreflang faltantes o incorrectas | Agrega etiquetas hreflang bidireccionales para todos los pares de idiomas |
| "Contenido duplicado" entre idiomas | Falta hreflang `x-default` | Agrega hreflang `x-default` apuntando a la versión principal/de respaldo |
| Usuarios forzados a la ubicación incorrecta | Redirección automática basada en IP | Usa un banner/aviso en lugar de redirección forzada |
| Traducciones faltantes en SERPs | Meta título/descripción no traducidos | Traduce todas las etiquetas `<title>` y `<meta description>` |
| Etiquetas hreflang ignoradas silenciosamente | Enlaces de retorno (bidireccionales) faltantes | Cada página en un conjunto hreflang debe enlazar a todas las demás, incluyéndose a sí misma |
| Códigos de idioma inválidos | Usar `uk` en lugar de `en-GB`, o `eu` | Usa solo códigos ISO 639-1 de idioma + ISO 3166-1 Alpha-2 de región |
| Googlebot solo ve la versión en inglés | Página adaptativa por ubicación sin URLs separadas | Crea URLs separadas por idioma y usa anotaciones hreflang |
| Mismo contenido alemán en `example.de` + `.com/de/` | Contenido duplicado entre dominios sin canonical | Establece `rel="canonical"` en la versión no preferida |

## Escalamiento
- Si el sitio requiere diferencias de precios regionales, moneda o contenido legal, consulta a un especialista en localización.
- Si surgen conflictos de hreflang por plugins del CMS, escala al administrador del CMS.
- Para sitios con más de 50 variantes de idioma, considera usar exclusivamente el método de sitemap (más fácil de mantener a escala).

### Referencias
- [Google: Cómo gestionar sitios multirregionales y multilingües](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- [Google: Informa a Google sobre las versiones localizadas de tu página](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google: Cómo rastrea Google las páginas adaptativas por ubicación](https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages)
