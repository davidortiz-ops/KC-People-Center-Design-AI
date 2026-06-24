---
name: seo-geo
description: >
  Optimizar contenido para AI Overviews (anteriormente SGE), búsqueda web de
  ChatGPT, Perplexity y otras experiencias de búsqueda impulsadas por IA.
  Análisis de Generative Engine Optimization (GEO) incluyendo señales de
  menciones de marca, accesibilidad de crawlers de IA, cumplimiento de
  llms.txt, puntuación de citabilidad a nivel de pasaje y optimización
  por plataforma. Usar cuando el usuario diga "AI Overviews", "SGE",
  "GEO", "AI search", "LLM optimization", "Perplexity", "AI citations",
  "ChatGPT search" o "AI visibility".
---

# Optimización para Búsqueda IA / GEO (Febrero 2026)

## Estadísticas Clave

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Alcance de AI Overviews | 1500 millones de usuarios/mes en 200+ países | Google |
| Cobertura de consultas en AI Overviews | 50%+ de todas las consultas | Datos de la industria |
| Crecimiento de sesiones referidas por IA | 527% (Enero-Mayo 2025) | SparkToro |
| Usuarios activos semanales de ChatGPT | 900 millones | OpenAI |
| Consultas mensuales de Perplexity | 500+ millones | Perplexity |

## Insight Crítico: Menciones de Marca > Backlinks

**Las menciones de marca se correlacionan 3× más fuerte con la visibilidad en IA que los backlinks.**
(Estudio de Ahrefs diciembre 2025 sobre 75,000 marcas)

| Señal | Correlación con Citas en IA |
|-------|-----------------------------|
| Menciones en YouTube | ~0.737 (más fuerte) |
| Menciones en Reddit | Alta |
| Presencia en Wikipedia | Alta |
| Presencia en LinkedIn | Moderada |
| Domain Rating (backlinks) | ~0.266 (débil) |

**Solo el 11% de los dominios** son citados tanto por ChatGPT como por Google AI Overviews para la misma consulta — la optimización por plataforma es esencial.

---

## Criterios de Análisis GEO (Actualizados)

### 1. Puntuación de Citabilidad (25%)

**Longitud óptima de pasaje: 134-167 palabras** para citación en IA.

**Señales fuertes:**
- Oraciones claras y citables con datos o estadísticas específicas
- Bloques de respuesta autocontenidos (pueden extraerse sin contexto)
- Respuesta directa en las primeras 40-60 palabras de la sección
- Afirmaciones atribuidas con fuentes específicas
- Definiciones que siguen patrones "X es..." o "X se refiere a..."
- Puntos de datos únicos no encontrados en otros lugares

**Señales débiles:**
- Declaraciones vagas y generales
- Opinión sin evidencia
- Conclusiones enterradas
- Sin puntos de datos específicos

### 2. Legibilidad Estructural (20%)

**El 92% de las citas de AI Overviews provienen de páginas en el top 10**, pero el 47% proviene de páginas que rankean por debajo de la posición 5 — lo que demuestra una lógica de selección diferente.

**Señales fuertes:**
- Jerarquía limpia de encabezados H1→H2→H3
- Encabezados basados en preguntas (coincide con patrones de consulta)
- Párrafos cortos (2-4 oraciones)
- Tablas para datos comparativos
- Listas ordenadas/no ordenadas para contenido paso a paso o multi-elemento
- Secciones FAQ con formato claro de Q&A

**Señales débiles:**
- Muro de texto sin estructura
- Jerarquía de encabezados inconsistente
- Sin listas ni tablas
- Información enterrada en párrafos

### 3. Contenido Multi-Modal (15%)

El contenido con elementos multi-modales tiene **tasas de selección 156% más altas**.

**Verificar:**
- Texto + imágenes relevantes
- Contenido en video (incrustado o enlazado)
- Infografías y gráficos
- Elementos interactivos (calculadoras, herramientas)
- Datos estructurados que respalden el contenido multimedia

### 4. Señales de Autoridad y Marca (20%)

**Señales fuertes:**
- Firma de autor con credenciales
- Fecha de publicación y última actualización
- Citas a fuentes primarias (estudios, documentos oficiales, datos)
- Credenciales y afiliaciones de la organización
- Citas de expertos con atribución
- Presencia de entidad en Wikipedia, Wikidata
- Menciones en Reddit, YouTube, LinkedIn

**Señales débiles:**
- Autoría anónima
- Sin fechas
- Sin fuentes citadas
- Sin presencia de marca en las plataformas

### 5. Accesibilidad Técnica (20%)

**Los crawlers de IA NO ejecutan JavaScript** — el renderizado del lado del servidor es crítico.

**Verificar:**
- Renderizado del lado del servidor (SSR) vs contenido solo del cliente
- Acceso de crawlers de IA en robots.txt
- Presencia y configuración del archivo llms.txt
- Términos de licencia RSL 1.0

---

## Detección de Crawlers de IA

Verificar `robots.txt` para estos crawlers de IA:

| Crawler | Propietario | Propósito |
|---------|-------------|-----------|
| GPTBot | OpenAI | Búsqueda web de ChatGPT |
| OAI-SearchBot | OpenAI | Funciones de búsqueda de OpenAI |
| ChatGPT-User | OpenAI | Navegación de ChatGPT |
| ClaudeBot | Anthropic | Funciones web de Claude |
| PerplexityBot | Perplexity | Búsqueda IA de Perplexity |
| CCBot | Common Crawl | Datos de entrenamiento (a menudo bloqueado) |
| anthropic-ai | Anthropic | Entrenamiento de Claude |
| Bytespider | ByteDance | IA de TikTok/Douyin |
| cohere-ai | Cohere | Modelos de Cohere |

**Recomendación:** Permitir GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot para visibilidad en búsqueda IA. Bloquear CCBot y crawlers de entrenamiento si se desea.

---

## Estándar llms.txt

El emergente estándar **llms.txt** proporciona a los crawlers de IA una guía estructurada de contenido.

**Ubicación:** `/llms.txt` (raíz del dominio)

**Formato:**
```
# Título del sitio
> Breve descripción

## Secciones principales
- [Título de página](url): Descripción
- [Otra página](url): Descripción

## Opcional: Datos clave
- Dato 1
- Dato 2
```

**Verificar:**
- Presencia de `/llms.txt`
- Guía estructurada de contenido
- Destacados de páginas clave
- Información de contacto/autoridad

---

## RSL 1.0 (Really Simple Licensing)

Nuevo estándar (diciembre 2025) para términos de licencia de IA legibles por máquina.

**Respaldado por:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Verificar:** Implementación de RSL y términos de licencia apropiados.

---

## Optimización por Plataforma

| Plataforma | Fuentes Clave de Citación | Enfoque de Optimización |
|------------|---------------------------|-------------------------|
| **Google AI Overviews** | Páginas en top 10 (92%) | SEO tradicional + optimización de pasajes |
| **ChatGPT** | Wikipedia (47.9%), Reddit (11.3%) | Presencia de entidad, fuentes autoritativas |
| **Perplexity** | Reddit (46.7%), Wikipedia | Validación comunitaria, discusiones |
| **Bing Copilot** | Índice de Bing, sitios autoritativos | Bing SEO, IndexNow |

---

## Salida

Generar `GEO-ANALYSIS.md` con:

1. **Puntuación de Preparación GEO: XX/100**
2. **Desglose por plataforma** (Google AIO, ChatGPT, Perplexity scores)
3. **Estado de Acceso de Crawlers IA** (qué crawlers están permitidos/bloqueados)
4. **Estado de llms.txt** (presente, faltante, recomendaciones)
5. **Análisis de Menciones de Marca** (presencia en Wikipedia, Reddit, YouTube, LinkedIn)
6. **Citabilidad a Nivel de Pasaje** (bloques óptimos de 134-167 palabras identificados)
7. **Verificación de Renderizado del Lado del Servidor** (análisis de dependencia de JavaScript)
8. **Top 5 Cambios de Mayor Impacto**
9. **Recomendaciones de Schema** (para descubrimiento en IA)
10. **Sugerencias de Reformateo de Contenido** (pasajes específicos para reescribir)

---

## Ganancias Rápidas

1. Agregar definición "¿Qué es [tema]?" en las primeras 60 palabras
2. Crear bloques de respuesta autocontenidos de 134-167 palabras
3. Agregar encabezados H2/H3 basados en preguntas
4. Incluir estadísticas específicas con fuentes
5. Agregar fechas de publicación/actualización
6. Implementar schema Person para autores
7. Permitir crawlers clave de IA en robots.txt

## Esfuerzo Medio

1. Crear archivo `/llms.txt`
2. Agregar bio de autor con credenciales + enlaces a Wikipedia/LinkedIn
3. Asegurar renderizado del lado del servidor para contenido clave
4. Construir presencia de entidad en Reddit, YouTube
5. Agregar tablas comparativas con datos
6. Implementar secciones FAQ (estructuradas, no schema para sitios comerciales)

## Alto Impacto

1. Crear investigación/encuestas originales (citabilidad única)
2. Construir presencia en Wikipedia para la marca/personas clave
3. Establecer canal de YouTube con menciones de contenido
4. Implementar enlazado de entidades comprehensivo (sameAs entre plataformas)
5. Desarrollar herramientas o calculadoras únicas
