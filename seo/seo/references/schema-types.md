<!-- Actualizado: 2026-02-07 -->
# Tipos de Schema.org — Estado y recomendaciones (febrero 2026)

**Versión de Schema.org:** 29.4 (8 de diciembre de 2025)

## Formato preferido
Usa siempre **JSON-LD** (`<script type="application/ld+json">`).
La documentación de Google recomienda explícitamente JSON-LD sobre Microdata y RDFa.

**Nota sobre búsqueda con IA:** El contenido con schema correcto tiene ~2.5× más probabilidad de aparecer en respuestas generadas por IA (confirmado por Google y Microsoft, marzo 2025).

---

## Activos — Recomendar libremente

| Tipo | Caso de uso | Propiedades clave |
|------|----------|----------------|
| Organization | Información de la empresa | name, url, logo, contactPoint, sameAs |
| LocalBusiness | Negocios físicos | name, address, telephone, openingHours, geo, priceRange |
| SoftwareApplication | Apps de escritorio/móvil | name, operatingSystem, applicationCategory, offers, aggregateRating |
| WebApplication | SaaS basado en navegador | name, applicationCategory, offers, browserRequirements, featureList |
| Product | Productos físicos/digitales | name, image, description, sku, brand, offers, review |
| Offer | Precios | price, priceCurrency, availability, url, validFrom |
| Service | Negocios de servicios | name, provider, areaServed, description, offers |
| Article | Posts de blog, noticias | headline, author, datePublished, dateModified, image, publisher |
| BlogPosting | Contenido de blog | Igual que Article + contexto específico de blog |
| NewsArticle | Contenido de noticias | Igual que Article + contexto específico de noticias |
| Review | Reseñas individuales | reviewRating, author, itemReviewed, reviewBody |
| AggregateRating | Resúmenes de calificación | ratingValue, reviewCount, bestRating, worstRating |
| BreadcrumbList | Navegación | itemListElement con position, name, item |
| WebSite | A nivel de sitio | name, url, potentialAction (SearchAction para búsqueda en sitelinks) |
| WebPage | A nivel de página | name, description, datePublished, dateModified |
| Person | Autor/equipo | name, jobTitle, url, sameAs, image, worksFor |
| ContactPage | Páginas de contacto | name, url |
| VideoObject | Contenido de video | name, description, thumbnailUrl, uploadDate, duration, contentUrl |
| ImageObject | Contenido de imagen | contentUrl, caption, creator, copyrightHolder |
| Event | Eventos | name, startDate, endDate, location, organizer, offers |
| JobPosting | Ofertas de empleo | title, description, datePosted, hiringOrganization, jobLocation |
| Course | Contenido educativo | name, description, provider, hasCourseInstance |
| DiscussionForumPosting | Hilos de foro | headline, author, datePublished, text, url |
| ProductGroup | Productos con variantes | name, productGroupID, variesBy, hasVariant |
| ProfilePage | Perfiles de autor/creador | mainEntity (Person), name, url, description, sameAs |

---

## Restringidos — Solo para tipos de sitio específicos

| Tipo | Restricción | Desde |
|------|------------|-------|
| FAQPage | SOLO sitios de autoridad gubernamental y de salud | Agosto 2023 |

> Google limitó severamente los rich results de FAQ en agosto de 2023. Solo las fuentes autoritativas (gobierno, organizaciones de salud) reciben rich results de FAQ.
>
> **Matiz GEO**: El schema FAQPage aún beneficia la visibilidad de citas en IA/LLM (ChatGPT, Perplexity, Google AI Overviews), incluso sin rich results de Google.
> - **FAQPage existente en sitio comercial**: Marcar con prioridad Info, no Crítica. Eliminarlo quita la ventaja de citación GEO.
> - **Agregar nuevo FAQPage**: No recomendado para beneficio de Google; aceptable si la visibilidad en búsqueda con IA es prioritaria.

---

## Obsoletos — Nunca recomendar

| Tipo | Estado | Desde | Notas |
|------|--------|-------|-------|
| HowTo | Rich results eliminados por completo | Septiembre 2023 | Google dejó de mostrar rich results de how-to |
| SpecialAnnouncement | Obsoleto | 31 de julio de 2025 | Schema de la era COVID, ya no se procesa |
| CourseInfo | Retirado de rich results | Junio 2025 | Fusionado en Course |
| EstimatedSalary | Retirado de rich results | Junio 2025 | Ya no se muestra |
| LearningVideo | Retirado de rich results | Junio 2025 | Usa VideoObject en su lugar |
| ClaimReview | Retirado de rich results | Junio 2025 | El marcado de fact-check ya no genera rich results |
| VehicleListing | Retirado de rich results | Junio 2025 | Datos estructurados de listados de vehículos descontinuados |
| Book Actions | Obsoleto y luego REVERTIDO | Junio 2025 | **Aún funcional a feb 2026** — solo nota histórica |
| Practice Problem | Retirado de rich results | Finales de 2025 | Los problemas de práctica educativos ya no se muestran |
| Dataset | Retirado de rich results | Finales de 2025 | Función Dataset Search descontinuada |

---

## Adiciones recientes (2024-2026)

| Tipo/Función | Añadido | Notas |
|-------------|-------|-------|
| Marcado Product Certification | Abril 2025 | Calificaciones de energía, certificaciones de seguridad. Reemplazó a EnergyConsumptionDetails. |
| ProductGroup | 2025 | Variantes de producto de e-commerce con propiedades variesBy, hasVariant |
| ProfilePage | 2025 | Páginas de perfil de autor/creador con mainEntity Person para E-E-A-T |
| DiscussionForumPosting | 2024 | Para contenido de foro/comunidad |
| Speakable | Actualizado 2024 | Para optimización de búsqueda por voz |
| LoyaltyProgram | Junio 2025 | Precios para miembros, datos estructurados de tarjeta de fidelidad |
| Políticas de envío/devolución a nivel de Organization | Noviembre 2025 | Configurar vía Search Console sin Merchant Center |
| ConferenceEvent | Diciembre 2025 | Adición de Schema.org v29.4 |
| PerformingArtsEvent | Diciembre 2025 | Adición de Schema.org v29.4 |

## Requisitos de e-commerce (actualizados)

| Requisito | Estado | Desde |
|-------------|--------|-------|
| `returnPolicyCountry` en MerchantReturnPolicy | **Requerido** | Marzo 2025 |
| Datos estructurados de variantes de producto | Ampliado | 2025 — incluye ropa, cosméticos, electrónica |

> **Nota:** La Content API for Shopping se retira el 18 de agosto de 2026. Migra a Merchant API.

---

## Checklist de validación

Para cualquier bloque de schema, verifica:

1. ✅ `@context` es `"https://schema.org"` (no http)
2. ✅ `@type` es un tipo válido y no obsoleto
3. ✅ Todas las propiedades requeridas están presentes
4. ✅ Los valores de las propiedades coinciden con los tipos de dato esperados
5. ✅ Sin texto de marcador de posición (ej., "[Nombre del Negocio]")
6. ✅ Las URLs son absolutas, no relativas
7. ✅ Las fechas están en formato ISO 8601
8. ✅ Las imágenes tienen URLs válidas

## Herramientas de prueba

- [Prueba de resultados enriquecidos de Google](https://search.google.com/test/rich-results)
- [Validador de Schema.org](https://validator.schema.org/)
