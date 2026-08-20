<!-- Actualizado: 2026-02-07 -->
# Referencia rápida de SEO de Google (febrero 2026)

Guía de referencia concisa para subagentes. Resume conceptos clave de Google Search,
requisitos y mejores prácticas. No es una reproducción de la documentación de Google —
consulta los enlaces a la documentación oficial al final para todos los detalles.

---

## Cómo funciona Google Search

Google Search opera en tres etapas: **Rastreo** (Googlebot descubre páginas siguiendo enlaces y leyendo sitemaps), **Indexación** (Google procesa y almacena el contenido, los metadatos y las señales de la página en su índice de búsqueda) y **Servicio** (cuando un usuario busca, los algoritmos de Google clasifican las páginas indexadas por relevancia, calidad y usabilidad para devolver los resultados más útiles). Las páginas deben ser rastreables e indexables para aparecer en los resultados de búsqueda.

---

## Google Search Essentials

Antes conocidas como "Directrices para webmasters". Requisitos clave:

### Requisitos técnicos
- Las páginas deben ser accesibles para Googlebot (no bloqueadas por robots.txt ni noindex)
- Las páginas deben devolver estado HTTP 200 para el contenido indexable
- El contenido debe estar en un formato que Google pueda procesar (HTML preferido; el contenido renderizado con JS es compatible pero más lento)
- Las páginas deben servirse sobre HTTPS

### Políticas de spam
- Sin cloaking (mostrar contenido distinto a Googlebot vs usuarios)
- Sin doorway pages (páginas creadas solo para rankear ante consultas específicas)
- Sin texto o enlaces ocultos
- Sin relleno de keywords
- Sin link spam (comprar enlaces, intercambios excesivos de enlaces)
- Sin contenido copiado o autogenerado sin valor agregado
- Sin redirecciones engañosas
- Sin páginas de afiliados thin

### Mejores prácticas clave
- Crea contenido para usuarios, no para motores de búsqueda
- Haz tu sitio fácil de navegar con una jerarquía clara
- Usa títulos y meta descriptions descriptivos y únicos por página
- Usa etiquetas de encabezado (H1-H6) para estructurar el contenido lógicamente
- Optimiza imágenes con alt text y tamaños de archivo apropiados
- Asegura un diseño responsivo apto para móviles
- Mejora la velocidad de carga (Core Web Vitals)
- Envía un sitemap XML a Google Search Console
- Usa datos estructurados (JSON-LD) para ayudar a Google a entender el contenido

---

## Señales de calidad de contenido

Google evalúa la calidad del contenido mediante el framework E-E-A-T:

- **Experiencia**: ¿El creador del contenido tiene experiencia de primera mano con el tema? (Fotos originales, historias personales, uso demostrado)
- **Pericia**: ¿El creador tiene conocimiento o credenciales relevantes? (Trayectoria profesional, profundidad técnica, fuentes precisas)
- **Autoridad**: ¿El creador o el sitio es reconocido como fuente de referencia? (Citas de la industria, menciones de marca, reconocimiento como experto)
- **Confiabilidad**: ¿El contenido y el sitio son fiables y transparentes? (Información de contacto, sitio seguro, estándares editoriales, afirmaciones precisas)

> **Nota YMYL**: Los temas "Your Money or Your Life" (salud, finanzas, seguridad, legal) se someten a los estándares E-E-A-T más altos. El contenido YMYL inexacto puede causar daño real, por lo que Google aplica umbrales de calidad más estrictos.

> **Actualización de diciembre 2025**: La evaluación E-E-A-T ahora se extiende a TODAS las consultas competitivas, no solo a los temas YMYL. Toda página que compita por ranking se evalúa según estas señales.

---

## Core Web Vitals

Medidos en el percentil 75 de datos de usuarios reales (datos de campo).

| Métrica | Bueno | Mejorable | Deficiente |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s – 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms – 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 – 0.25 | > 0.25 |

**Datos clave:**
- INP reemplazó a FID (First Input Delay) el 12 de marzo de 2024. FID se eliminó por completo de todas las herramientas de Chrome (CrUX API, PageSpeed Insights, Lighthouse) el 9 de septiembre de 2024. NO hagas referencia a FID.
- Core Web Vitals es una señal de ranking confirmada (desde junio de 2021)
- Los datos de campo (CrUX) se prefieren sobre los de laboratorio (Lighthouse) para la evaluación
- El objetivo es aprobar las tres métricas en "Bueno"

**Herramientas de medición:**
- Google PageSpeed Insights (datos de campo + laboratorio)
- Chrome User Experience Report (CrUX) — datos de campo
- Lighthouse (solo datos de laboratorio)
- Reporte de Core Web Vitals de Google Search Console

---

## Mejores prácticas de datos estructurados

- **JSON-LD es el formato preferido de Google** (sobre Microdata y RDFa)
- Coloca el JSON-LD en etiquetas `<script type="application/ld+json">` en el `<head>` o `<body>`
- Incluye siempre las propiedades `@context` y `@type`
- Las **propiedades requeridas** deben estar presentes para ser elegible a resultados enriquecidos
- Las **propiedades recomendadas** mejoran la calidad de los resultados enriquecidos pero no son obligatorias
- Marca únicamente contenido que sea visible en la página
- Usa la Prueba de resultados enriquecidos de Google para validar antes de desplegar
- No marques contenido engañoso u oculto a los usuarios
- Mantén el schema actualizado — actualízalo cuando cambie el contenido de la página

### Tipos obsoletos/restringidos (a feb 2026)
- **HowTo**: Rich results eliminados (septiembre 2023)
- **FAQ**: Restringido a sitios de autoridad gubernamental y de salud (agosto 2023)
- **SpecialAnnouncement**: Obsoleto (31 de julio de 2025)
- **CourseInfo, EstimatedSalary, LearningVideo**: Retirados (junio 2025)
- **ClaimReview**: Retirado (junio 2025)
- **VehicleListing**: Retirado (junio 2025)

---

## Penalizaciones comunes y cómo evitarlas

### Acciones manuales
Notificaciones de Google Search Console por infracciones. Causas comunes:
- **Enlaces no naturales** (compra/venta de enlaces): Desautorizar (disavow) enlaces malos, solicitar reconsideración
- **Contenido thin**: Agregar valor único sustancial a las páginas afectadas
- **Cloaking/redirecciones engañosas**: Eliminar el servicio engañoso, solicitar reconsideración
- **Spam generado por usuarios**: Moderar comentarios/foros, agregar nofollow a enlaces de usuarios
- **Problemas de datos estructurados**: Corregir marcado engañoso o spam

### Degradaciones algorítmicas
Sin notificación manual — se detectan por caídas de ranking. Causas comunes:
- **Sistema de contenido útil (Helpful Content System)**: Fusionado en el ranking core de Google en marzo de 2024 — ya no es un sistema independiente. Las señales de utilidad ahora se evalúan dentro de cada actualización core. El contenido de bajo valor, generado por IA o poco útil a escala sigue provocando degradaciones vía actualizaciones core.
- **Actualizaciones core**: Reevaluación amplia de calidad en todas las señales
- **Actualizaciones de spam**: Detección automatizada de patrones de spam
- **Actualizaciones de link spam**: Devaluación de patrones de enlaces manipuladores

### Pasos de recuperación
1. Identificar el problema (Search Console, análisis de la línea temporal de rankings)
2. Corregir la causa raíz (eliminar spam, mejorar contenido, limpiar enlaces)
3. Para acciones manuales: enviar solicitud de reconsideración vía Search Console
4. Para algorítmicas: mejorar la calidad, esperar la reevaluación de la próxima actualización core
5. Monitorear la recuperación en los reportes de rendimiento de Search Console

---

## Enlaces a la documentación oficial

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Cómo funciona Google Search](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Visión general de datos estructurados](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Prueba de resultados enriquecidos](https://search.google.com/test/rich-results)
- [Reporte de Core Web Vitals](https://support.google.com/webmasters/answer/9205520)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Ayuda de Search Console](https://support.google.com/webmasters)
- [Reporte de acciones manuales](https://support.google.com/webmasters/answer/9044175)
- [Panel de estado de Google Search](https://status.search.google.com/)
- [Blog de Google Search Central](https://developers.google.com/search/blog)
- [Políticas de spam](https://developers.google.com/search/docs/essentials/spam-policies)
- [E-E-A-T y Quality Rater Guidelines](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

> La **indexación mobile-first** está 100% completa desde el 5 de julio de 2024. Google ahora rastrea e indexa TODOS los sitios web exclusivamente con el user-agent móvil de Googlebot.
