---
name: seo-content
description: >
  Análisis de calidad de contenido y E-E-A-T con evaluación de preparación
  para citas de IA. Usar cuando el usuario diga "content quality", "E-E-A-T",
  "content analysis", "readability check", "thin content" o "content audit".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - Bash
  - WebFetch
  - WebSearch
---

# Análisis de Calidad de Contenido y E-E-A-T

## Framework E-E-A-T (actualizado QRG Sept 2025)

Leer `seo/references/eeat-framework.md` para los criterios completos.

### Experiencia (señales de primera mano)
- Investigación original, casos de estudio, resultados antes/después
- Anécdotas personales, documentación de procesos
- Datos únicos, conocimientos propietarios
- Fotos/videos de experiencia directa

### Expertise
- Credenciales del autor, certificaciones, biografía
- Trayectoria profesional relevante al tema
- Profundidad técnica adecuada para la audiencia
- Afirmaciones precisas y bien fundamentadas

### Autoridad
- Citas externas, backlinks de fuentes autoritativas
- Menciones de marca, reconocimiento de la industria
- Publicado en medios reconocidos
- Citado por otros expertos

### Confiabilidad
- Información de contacto, dirección física
- Política de privacidad, términos de servicio
- Testimonios de clientes, reseñas
- Sellos de fecha, correcciones transparentes
- Sitio seguro (HTTPS)

## Métricas de Contenido

### Análisis de Word Count
Comparar contra los mínimos por tipo de página:
| Tipo de Página | Mínimo |
|-----------|---------|
| Homepage | 500 |
| Página de servicio | 800 |
| Blog post | 1,500 |
| Página de producto | 300+ (400+ para productos complejos) |
| Página de ubicación | 500-600 |

> **Importante:** Estos son **pisos de cobertura temática**, no objetivos. Google ha confirmado que el word count NO es un factor de ranking directo. El objetivo es una cobertura temática completa — una página de 500 palabras que responda exhaustivamente a la consulta superará a una página de 2,000 palabras que no lo haga. Úsalos como guías para una profundidad de cobertura adecuada, no como requisitos rígidos.

### Legibilidad
- Flesch Reading Ease: objetivo 60-70 para audiencia general

> **Nota:** Flesch Reading Ease es un indicador útil de accesibilidad del contenido pero NO es un factor de ranking directo de Google. John Mueller ha confirmado que Google no usa puntuaciones básicas de legibilidad para el ranking. Yoast despriorizó las puntuaciones Flesch en v19.3. Usa el análisis de legibilidad como un indicador de calidad de contenido, no como una métrica SEO para optimizar directamente.
- Nivel de grado: coincidir con la audiencia objetivo
- Longitud de oraciones: promedio 15-20 palabras
- Longitud de párrafos: 2-4 oraciones

### Optimización de Keywords
- Keyword primaria en título, H1, primeras 100 palabras
- Densidad natural (1-3%)
- Variaciones semánticas presentes
- Sin keyword stuffing

#### Palabras LSI / variaciones semánticas

Las palabras LSI (términos semánticamente relacionados) ayudan a Google a entender el
tema de la página y a cubrir la intención completa de la consulta. Identifícalas a partir
de búsquedas relacionadas, "la gente también pregunta" (PAA) y el vocabulario de los
competidores que rankean. Inclúyelas de forma natural en subtítulos y cuerpo.

**Ejemplos de palabras LSI por keyword:**

| Palabra clave | Palabras LSI |
|---------------|--------------|
| ticket de avión | próximo viaje, comprar ticket, reserva tu vuelo, aerolíneas disponibles, próximo destino, tickets baratos, pasaporte |
| mallas de seguridad | seguridad en el hogar, mallas para balcones, protección de caídas, seguridad para ventanas, protección en pisos altos de edificios |
| celulares apple | dispositivo móvil, gama alta, alta tecnología, cuánto cuesta, última versión, cuál es el mejor, dónde comprar |
| comida para perros | razas pequeñas, raza mediana, alimentación de perros adultos, alto en proteína, bajo en sodio, comida saludable, necesidades nutricionales |
| pesca en río | botes de pesca, rutas de pesca, especies de peces, barcos para pesca en río, arroyos, rápidos de la corriente, señuelos para pesca en río |

> No fuerces estos términos: úsalos donde aporten contexto real. La meta es cobertura
> temática y satisfacción de la intención, no densidad de coincidencia exacta.

### Estructura del Contenido
- Jerarquía lógica de encabezados (H1 → H2 → H3)
- Secciones escaneables con encabezados descriptivos
- Listas con viñetas/numeradas donde corresponda
- Tabla de contenido para contenido de formato largo

### Multimedia
- Imágenes relevantes con alt text adecuado
- Videos cuando corresponda
- Infografías para datos complejos
- Gráficos/diagramas para estadísticas

### Internal Linking
- 3-5 enlaces internos relevantes por cada 1000 palabras
- Anchor text descriptivo
- Enlaces a contenido relacionado
- Sin páginas huérfanas

### External Linking
- Citar fuentes autoritativas
- Abrir en nueva pestaña para experiencia de usuario
- Cantidad razonable (no excesiva)

## Evaluación de Contenido IA (adición QRG Sept 2025)

Los evaluadores de Google ahora evalúan formalmente si el contenido parece generado por IA.

### Contenido IA Aceptable
- Demuestra E-E-A-T genuino
- Proporciona valor único
- Tiene supervisión y edición humana
- Contiene conocimientos originales

### Marcadores de Contenido IA de Baja Calidad
- Frases genéricas, falta de especificidad
- Sin conocimiento original
- Estructura repetitiva entre páginas
- Sin atribución de autor
- Imprecisiones fácticas

### Detección de Patrones de Escritura IA

Al auditar, escanear activamente estos 24 patrones documentados en [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing):

**Señales de vocabulario:** "destacar", "crucial", "robusto", "tapestry", "landscape" (abstracto), "testament", "pivotal", "underscore", "vibrant", "moreover", "additionally", "showcase"

**Señales de estructura:** uso excesivo de em dash, listas inline-header (`**Concepto:** texto`), regla del tres forzada, title case en todos los encabezados, decoraciones con emoji, paralelismos negativos ("No es solo X, es Y")

**Señales de voz:** atribuciones vagas ("los expertos señalan"), conclusiones genéricas ("el futuro es prometedor"), evitación de cópula ("sirve como" en lugar de "es"), acumulación de frases en -ing (highlighting... ensuring... reflecting...)

**Si se encuentran 3+ patrones:** marcar como "Riesgo de Escritura IA" y recomendar ejecutar `/humanizer` en las secciones afectadas antes de publicar.

> **Helpful Content System (Marzo 2024):** El Helpful Content System se fusionó en el algoritmo central de ranking de Google durante la core update de marzo 2024. Ya no opera como un clasificador independiente. Las señales de utilidad ahora se ponderan dentro de cada core update — los mismos principios aplican (contenido people-first, demostrar E-E-A-T, satisfacer la intención del usuario), pero la aplicación es continua en lugar de mediante actualizaciones HCU separadas.

## Preparación para Citas de IA (señales GEO)

Optimizar para motores de búsqueda de IA (ChatGPT, Perplexity, Google AI Overviews):

- Declaraciones claras y citables con estadísticas/hechos
- Datos estructurados (especialmente para puntos de datos)
- Jerarquía de encabezados sólida (flujo H1→H2→H3)
- Formato answer-first para preguntas clave
- Tablas y listas para datos comparativos
- Atribución clara y citas de fuentes

### Visibilidad en Búsqueda IA y GEO (2025-2026)

**Google AI Mode** se lanzó públicamente en mayo de 2025 como una pestaña separada en Google Search, disponible en más de 180 países. A diferencia de AI Overviews (que aparecen sobre los resultados orgánicos), AI Mode proporciona una experiencia de búsqueda completamente conversacional con **cero blue links orgánicos** — haciendo que la citación por IA sea el único mecanismo de visibilidad.

**Estrategias clave de optimización para citación IA:**
- **Respuestas estructuradas:** Formatos claros de pregunta-respuesta, patrones de definición e instrucciones paso a paso que los sistemas de IA puedan extraer y citar
- **Datos propios:** Investigación original, estadísticas, casos de estudio y conjuntos de datos únicos son altamente citados por sistemas de IA
- **Schema markup:** Article, FAQ (para plataformas de IA que no son de Google) y esquemas de contenido estructurado ayudan a los sistemas de IA a analizar y atribuir contenido
- **Autoridad temática:** Los sistemas de IA prefieren citar fuentes que demuestren experiencia profunda — construye clusters de contenido, no páginas aisladas
- **Claridad de entidades:** Asegurar que la marca, los autores y los conceptos clave estén claramente definidos con datos estructurados (Organization, Person schema)
- **Seguimiento multiplataforma:** Monitorear la visibilidad en Google AI Overviews, AI Mode, ChatGPT, Perplexity y Bing Copilot — no solo rankings tradicionales. Tratar la citación IA como un KPI independiente junto con los rankings orgánicos y el tráfico.

**Generative Engine Optimization (GEO):**
GEO es la disciplina emergente de optimizar contenido específicamente para respuestas generadas por IA. Las señales GEO clave incluyen: citabilidad (hechos extractables claros y concisos), atribución (citas a fuentes dentro de tu contenido), estructura (jerarquía de encabezados bien organizada) y frescura (datos actualizados regularmente). Consulta el skill `seo-geo` para flujos de trabajo GEO detallados.

## Frescura del Contenido

- Fecha de publicación visible
- Fecha de última actualización si el contenido ha sido revisado
- Marcar contenido con más de 12 meses sin actualizar para temas de cambio rápido

## Puntuación de Brecha con Competidores

Puntuar top 5 competidores SERP en 4 dimensiones (1-10 cada una):

| Dimensión | Descripción |
|-----------|-------------|
| Depth | Cobertura del tema, word count, exhaustividad |
| Formatting | Estructura de encabezados, legibilidad, uso de multimedia |
| SEO | Título, meta, schema, internal linking |
| UX | Claridad del CTA, layout móvil, diseño above-fold |

Calcular prioridad de brecha: `Impacto x Ventaja Competitiva / Esfuerzo`

## Generación de Content Brief

Como parte del análisis de contenido, puedes generar un brief detallado. Si tu stack
incluye un script para ello, úsalo (ajusta la ruta a tu proyecto):
```bash
python <tu-stack>/scripts/content_brief.py --site <s> --keyword "KW"
```

Un brief completo incluye:
- Tabla de análisis de competidores
- Conteo de palabras por sección
- Reglas de colocación de keywords
- Requisitos E-E-A-T
- Oportunidades de enlazado interno

### Guía de Keywords por Sección

Para cada sección del outline, especificar:
- Qué keyword (primaria o secundaria) va en el heading
- Si el body debe incluir la keyword primaria o una variación
- Distribución pareja — no concentrar al inicio ni agrupar en una sección

### Especificación de Information Gain

Todo brief debe especificar el valor único:
- Datos propietarios o investigación original
- Casos de estudio con resultados reales
- Citas de expertos o experiencia de primera mano
- NO "más detalle" o "mejor formato"

## Salida

### Puntaje de Calidad de Contenido: XX/100

### Desglose E-E-A-T
| Factor | Puntaje | Señales Clave |
|--------|-------|-------------|
| Experiencia | XX/25 | ... |
| Expertise | XX/25 | ... |
| Autoridad | XX/25 | ... |
| Confiabilidad | XX/25 | ... |

### Preparación para Citas IA: XX/100

### Riesgo de Escritura IA: [Ninguno / Bajo / Medio / Alto]
<!-- Alto = 5+ patrones encontrados. Medio = 3-4. Bajo = 1-2. Ninguno = 0 -->
<!-- Si Medio o Alto: incluir "Ejecutar /humanizer en [nombres de secciones]" en Recomendaciones -->

### Puntaje de Brecha con Competidores: XX/40
| Competidor | Depth | Formatting | SEO | UX | Total |
|------------|-------|-----------|-----|-----|-------|

### Problemas Encontrados
### Recomendaciones

## Integración entre Skills

| Necesidad | Skill |
|------|-------|
| Humanizar texto generado por IA | `/humanizer [texto]` |
| Datos reales de GSC + oportunidades de keywords | `/seo google <url>` |
| Topic clustering | `/seo cluster plan <seed-kw>` |
| Análisis de tipo de página | `/seo sxo <url> <keyword>` |
| Preparación GEO/búsqueda IA | `/seo geo <url>` |
