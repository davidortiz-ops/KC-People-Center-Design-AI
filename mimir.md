# Mimir — Catálogo de Skills · Chapter Research

Fuente: repositorio `KC-People-Center-Design-AI`, carpeta `research/`
Commit de referencia: `387f7ef` (2026-07-29)
Fecha de extracción: 2026-08-20
Total de skills: **7**

> **Nota de fidelidad de datos.** Los campos `name`, `description`, `license`,
> `compatibility`, `allowed-tools` y `metadata` están transcritos literalmente del
> frontmatter YAML de cada `SKILL.md`. El campo `allowed-tools` fue derivado del
> contenido de cada skill y escrito de vuelta al repositorio el 2026-08-20.
> El campo **`tags`** *sigue sin existir* en el repositorio: es una propuesta de
> este documento, marcada como `(derivado)`, y debe validarse antes de tratarla
> como contrato.

---

## Índice

| # | Skill (`name`) | Título | Categoría | Versión | Allowed-tools |
| --- | --- | --- | --- | --- | --- |
| 1 | `analizar-contenido-tematico` | Análisis de Contenido Temático | research | 1.0.0 | Base + Ask |
| 2 | `analizar-tendencias-mercado` | Análisis de Tendencias de Mercado | market-research | 1.0.0 | Base + Ask + Web |
| 3 | `crear-personas-ux` | Creación de Personas UX | ux-research | 1.0.0 | Base + Ask |
| 4 | `diagnosticar-barreras-conductuales` | Diagnóstico de Barreras Conductuales | behavioral-research | 1.0.0 | Base |
| 5 | `extraer-vacantes-software` | Extracción de Vacantes de Software | research-data-extraction | 1.0.0 | Base |
| 6 | `mapear-journey-conductual` | Behavioral Customer Journey Map | ux-research | 1.0.0 | Base + Ask |
| 7 | `simular-usuarios-banca-premium` | Usuarios Sintéticos de Banca Premium | synthetic-user-research | 1.0.0 | Base + Ask |

Donde **Base** = `Read`, `Write`, `Edit`, `Grep`, `Glob` · **Ask** = `AskUserQuestion` · **Web** = `WebFetch`, `WebSearch`.

---

## 1. Análisis de Contenido Temático

- **Título:** Análisis de Contenido Temático
- **Nombre técnico (`name`):** `analizar-contenido-tematico`
- **Tipo:** Agent Skill
- **Descripción:** Analiza entrevistas, respuestas abiertas, documentos, notas y transcripciones mediante codificación temática inductiva, deductiva o híbrida. Úsalo para crear códigos y categorías, comparar segmentos, construir diccionarios de códigos y sintetizar hallazgos cualitativos con trazabilidad hasta la evidencia.
- **Descripción corta:** Codifica y sintetiza evidencia cualitativa.
- **Tags (derivado):** `investigacion-cualitativa`, `codificacion-tematica`, `analisis-de-contenido`, `entrevistas`, `transcripciones`, `diccionario-de-codigos`, `trazabilidad`, `sintesis-de-hallazgos`
- **Categorías:** `research` · investigación cualitativa · análisis de datos
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura al corpus cualitativo. No requiere herramientas externas.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: research
  - `language`: es
  - `source_prompt`: analisis-contenido-tematico.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
    - AskUserQuestion
  ```

  *Sin red: declara "no requiere herramientas externas". `AskUserQuestion` porque la regla de evidencia obliga a solicitar el dato faltante cuando es bloqueante. `Edit` para refinar el diccionario de códigos en pasadas sucesivas.*
- **Prompt de invocación:** `Usa $analizar-contenido-tematico para codificar este corpus con trazabilidad de fuentes.`
- **Estructura de salida:** Alcance y método → Categorías → Diccionario de códigos → Patrones y contrastes → Insights → Vacíos y limitaciones → Comprobación final
- **Ruta:** `research/analizar-contenido-tematico/`

---

## 2. Análisis de Tendencias de Mercado

- **Título:** Análisis de Tendencias de Mercado
- **Nombre técnico (`name`):** `analizar-tendencias-mercado`
- **Tipo:** Agent Skill
- **Descripción:** Analiza fuentes actuales de mercado para distinguir hechos, tendencias, señales débiles e incertidumbres; evalúa madurez e impacto y construye escenarios prospectivos trazables. Úsalo para inteligencia de mercado, vigilancia estratégica, análisis PESTEL, oportunidades, riesgos y recomendaciones por horizonte temporal.
- **Descripción corta:** Detecta tendencias y construye escenarios.
- **Tags (derivado):** `inteligencia-de-mercado`, `vigilancia-estrategica`, `pestel`, `tendencias`, `senales-debiles`, `escenarios-prospectivos`, `analisis-de-riesgos`, `horizontes-temporales`
- **Categorías:** `market-research` · estrategia · prospectiva
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Puede requerir navegación web para información actual y acceso de lectura a las fuentes aportadas.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: market-research
  - `language`: es
  - `source_prompt`: analisis-tendencias-mercado.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
    - AskUserQuestion
    - WebFetch
    - WebSearch
  ```

  *Única skill del set con acceso a red (`compatibility` menciona navegación web para información actual). `AskUserQuestion` porque el contrato de entrada exige mercado, geografía, fecha de corte y horizontes antes de analizar.*
- **Prompt de invocación:** `Usa $analizar-tendencias-mercado para analizar estas fuentes y construir escenarios trazables.`
- **Estructura de salida:** Alcance y calidad de fuentes → Tendencias → Señales débiles → Escenarios → Oportunidades, riesgos y recomendaciones → Limitaciones → Comprobación final
- **Ruta:** `research/analizar-tendencias-mercado/`

---

## 3. Creación de Personas UX

- **Título:** Creación de Personas UX
- **Nombre técnico (`name`):** `crear-personas-ux`
- **Tipo:** Agent Skill
- **Descripción:** Crea personas UX conductuales y accionables a partir de entrevistas, encuestas, observaciones y otras fuentes de investigación. Úsalo para segmentar usuarios por objetivos, comportamientos, contexto, barreras y criterios de decisión, manteniendo trazabilidad y evitando estereotipos o atributos inventados.
- **Descripción corta:** Crea personas conductuales sustentadas.
- **Tags (derivado):** `ux-research`, `user-persona`, `segmentacion`, `investigacion-de-usuarios`, `comportamiento`, `matriz-de-evidencia`, `antiestereotipos`, `trazabilidad`
- **Categorías:** `ux-research` · diseño centrado en el usuario · investigación de usuarios
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura a evidencia de investigación de usuarios.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: ux-research
  - `language`: es
  - `source_prompt`: creacion-user-persona.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
    - AskUserQuestion
  ```

  *Sin red. `AskUserQuestion` para fijar la decisión que soportarán las personas y para casos que la skill deja en manos del usuario (p. ej. añadir nombre ficticio solo si lo exige). `Edit` para iterar personas sobre un documento existente.*
- **Prompt de invocación:** `Usa $crear-personas-ux para crear personas conductuales basadas en este corpus.`
- **Estructura de salida:** Base de segmentación → Persona → Matriz de evidencia → Diferencias entre personas → Implicaciones y preguntas pendientes → Comprobación final
- **Ruta:** `research/crear-personas-ux/`

---

## 4. Diagnóstico de Barreras Conductuales

- **Título:** Diagnóstico de Barreras Conductuales
- **Nombre técnico (`name`):** `diagnosticar-barreras-conductuales`
- **Tipo:** Agent Skill
- **Descripción:** Diagnostica barreras de capacidad, oportunidad y motivación; formula hipótesis sobre sesgos cognitivos y diseña intervenciones conductuales éticas y evaluables. Úsalo para analizar abandono, indecisión, baja adopción o incumplimiento de un comportamiento objetivo sin presentar correlaciones como causas.
- **Descripción corta:** Formula hipótesis y nudges éticos.
- **Tags (derivado):** `behavioral-design`, `com-b`, `sesgos-cognitivos`, `nudges`, `intervenciones-conductuales`, `adopcion`, `abandono`, `etica`, `plan-de-validacion`
- **Categorías:** `behavioral-research` · ciencias del comportamiento · diseño de intervenciones
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura a evidencia conductual cualitativa o cuantitativa.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: behavioral-research
  - `language`: es
  - `source_prompt`: sesgos-cognitivos-intervenciones.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
  ```

  *Sin red y **sin `AskUserQuestion`**: la skill no pregunta por datos faltantes, los declara en la columna `Dato faltante` de la tabla de diagnóstico. Añádelo solo si quieres cambiar ese comportamiento.*
- **Prompt de invocación:** `Usa $diagnosticar-barreras-conductuales para diagnosticar barreras y proponer pruebas éticas.`
- **Estructura de salida:** Comportamiento y línea base → Diagnóstico → Hipótesis conductuales → Intervenciones → Plan de validación → Revisión ética → Priorización → Comprobación final
- **Ruta:** `research/diagnosticar-barreras-conductuales/`

---

## 5. Extracción de Vacantes de Software

- **Título:** Extracción de Vacantes de Software
- **Nombre técnico (`name`):** `extraer-vacantes-software`
- **Tipo:** Agent Skill
- **Descripción:** Extrae y normaliza información estructurada de una o varias vacantes de desarrollo de software, incluyendo empresa, sector, cargo, seniority, ubicación, modalidad, contrato, stack, experiencia y salario. Úsalo para convertir anuncios no estructurados en tablas o JSON auditables sin inventar datos.
- **Descripción corta:** Estructura datos de vacantes de software.
- **Tags (derivado):** `extraccion-de-datos`, `normalizacion`, `vacantes`, `talento-tech`, `seniority`, `stack-tecnologico`, `json`, `datos-auditables`
- **Categorías:** `research-data-extraction` · datos estructurados · talento y mercado laboral
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura a textos o archivos de vacantes; no requiere herramientas externas.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: research-data-extraction
  - `language`: es
  - `source_prompt`: analisis-vacantes-empleo.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
  ```

  *Sin red (`compatibility` lo dice explícitamente) y **sin `AskUserQuestion`**: reporta los campos ausentes en la salida en lugar de preguntar. `Edit` para acumular vacantes en una tabla existente por lotes.*
- **Prompt de invocación:** `Usa $extraer-vacantes-software para extraer y normalizar estas vacantes.`
- **Estructura de salida:** Flujo → Reglas → Salida predeterminada (tabla o JSON) → Comprobación final
- **Ruta:** `research/extraer-vacantes-software/`

---

## 6. Behavioral Customer Journey Map

- **Título:** Behavioral Customer Journey Map
- **Nombre técnico (`name`):** `mapear-journey-conductual`
- **Tipo:** Agent Skill
- **Descripción:** Construye Behavioral Customer Journey Maps a partir de entrevistas, observaciones, analytics y evidencia de producto. Úsalo para mapear etapas, acciones, decisiones, emociones, motivaciones, fricciones, canales, transiciones y momentos de verdad para un actor y escenario concretos.
- **Descripción corta:** Mapea journeys conductuales con evidencia.
- **Tags (derivado):** `customer-journey-map`, `journey-conductual`, `ux-research`, `momentos-de-verdad`, `fricciones`, `emociones`, `canales`, `analytics`, `service-design`
- **Categorías:** `ux-research` · service design · investigación de usuarios
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura a evidencia cualitativa o cuantitativa del journey.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: ux-research
  - `language`: es
  - `source_prompt`: behavioral-customer-journey-map.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
    - AskUserQuestion
  ```

  *Sin red. `AskUserQuestion` porque el contrato de entrada exige definir actor, escenario, inicio y final del recorrido, y journey actual vs. deseado antes de mapear.*
- **Prompt de invocación:** `Usa $mapear-journey-conductual para construir un journey basado en esta evidencia.`
- **Estructura de salida:** Contexto → Journey → Transiciones y rupturas → Momentos de verdad → Oportunidades → Vacíos de investigación → Comprobación final
- **Ruta:** `research/mapear-journey-conductual/`

---

## 7. Usuarios Sintéticos de Banca Premium

- **Título:** Usuarios Sintéticos de Banca Premium
- **Nombre técnico (`name`):** `simular-usuarios-banca-premium`
- **Tipo:** Agent Skill
- **Descripción:** Construye, audita y opera perfiles sintéticos de clientes de banca premium basados en investigación identificable. Úsalo para explorar expectativas, criterios de confianza, fricciones y reacciones hipotéticas dentro de un perfil documentado, sin sustituir investigación real, validar demanda ni inventar comportamientos.
- **Descripción corta:** Simula perfiles premium con límites.
- **Tags (derivado):** `usuarios-sinteticos`, `banca-premium`, `simulacion`, `perfiles-documentados`, `auditoria-de-perfil`, `limites-de-uso`, `servicios-financieros`, `confianza`
- **Categorías:** `synthetic-user-research` · investigación simulada · servicios financieros
- **Licencia:** Propietaria de Pragma; uso interno exclusivo. Ver `LICENSE.txt`.
- **Compatibilidad:** Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere investigación base o un perfil documentado accesible como texto o archivo.
- **Metadata:**
  - `author`: Pragma
  - `version`: 1.0.0
  - `category`: synthetic-user-research
  - `language`: es
  - `source_prompt`: usuarios-sinteticos.md
- **Allowed-tools:**

  ```yaml
  allowed-tools:
    - Read
    - Write
    - Edit
    - Grep
    - Glob
    - AskUserQuestion
  ```

  *Sin red. `AskUserQuestion` es el caso más fuerte del set: el contrato exige el modo solicitado (construir / auditar / simular) y la skill ordena explícitamente solicitar evidencia cuando la investigación base es insuficiente, en lugar de inventar un contexto. `Edit` para el modo auditar sobre un perfil ya documentado.*
- **Prompt de invocación:** `Usa $simular-usuarios-banca-premium para construir y operar un perfil sintético trazable.`
- **Modos de operación:** Construir perfil · Auditar perfil · Simular respuesta
- **Estructura de salida:** Límites de uso → Contrato de entrada → Perfil operativo → Formato de simulación (hipótesis sintética) → Comprobación final
- **Ruta:** `research/simular-usuarios-banca-premium/`

---

## Datos comunes a todo el chapter

- **Tipo:** Agent Skill (formato Agent Skills, `SKILL.md` con frontmatter YAML)
- **Autor:** Pragma
- **Versión:** 1.0.0 (todas)
- **Idioma:** `es`
- **Licencia:** Propietaria de Pragma — uso interno exclusivo. `LICENSE.txt` idéntico en las 7 skills (misma suma MD5).
- **Texto de licencia:** Copyright (c) 2026 Pragma. Todos los derechos reservados. Propiedad confidencial; uso autorizado solo a personal y colaboradores de Pragma para fines internos. Prohibido copiar, modificar, publicar, distribuir, sublicenciar o usar con fines externos o comerciales sin autorización escrita. Material "TAL CUAL", sin garantías.
- **Estructura de carpeta por skill:**

  ```
  <nombre-skill>/
    SKILL.md              # instrucciones + frontmatter
    LICENSE.txt           # licencia propietaria
    agents/openai.yaml    # display_name, short_description, default_prompt
    evals/evals.json      # casos de evaluación
  ```

- **Carpeta `research/backup/`:** contiene los 7 prompts originales en Markdown plano, previos a su conversión a Agent Skills (referenciados en `metadata.source_prompt`).

### Pendientes de decisión al cargar en el sistema de skills

1. **`tags`** — no existen en el repo. Los de este documento son propuestos; si tu sistema los usa para búsqueda, conviene fijarlos y luego escribirlos de vuelta al frontmatter.
2. **`allowed-tools`** — ya declarados en el frontmatter de las 7 skills. Usan el vocabulario acordado (`Read`, `Write`, `Edit`, `Grep`, `Glob`, `AskUserQuestion`, `WebFetch`, `WebSearch`) y se derivan de lo que cada skill declara:
   - **Red (`WebFetch` + `WebSearch`): solo `analizar-tendencias-mercado`.** Es la única cuya `compatibility` menciona navegación web. Las otras seis operan sobre evidencia local; darles red contradice su contrato de trazabilidad.
   - **`AskUserQuestion`: 5 de 7.** Justificado donde la skill tiene contrato de entrada que debe completarse antes de producir (`analizar-tendencias-mercado`, `mapear-journey-conductual`, `simular-usuarios-banca-premium`) o una regla explícita de solicitar datos faltantes (`analizar-contenido-tematico`) o decisiones que delega al usuario (`crear-personas-ux`).
   - **Excluido en `diagnosticar-barreras-conductuales` y `extraer-vacantes-software`** de forma deliberada: ambas declaran los huecos en la salida (`Dato faltante`, `Campos ausentes relevantes`) en vez de preguntar. Añadirlo cambiaría su comportamiento de diseño.
   - **`Edit`** en las 7: todas producen entregables que se refinan en pasadas sucesivas (diccionarios de códigos, personas, journeys, tablas de vacantes por lotes).
3. **`Write` y `Edit`** — ninguna skill los exige de forma explícita; se incluyen porque todas producen un entregable documental. Recórtalos a solo `Read`/`Grep`/`Glob` si tu sistema prefiere salida por conversación sin escritura en disco.
