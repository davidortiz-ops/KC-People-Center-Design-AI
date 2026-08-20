# Business Discovery

> Chapter de **People Centered Design - Pragma**.

Artefactos para la fase de **descubrimiento de negocio**: diagnóstico de problemas,
validación de suposiciones, definición de alcance, métricas y guardrails regulatorios.
La mayoría están diseñados como **skills** (agentes especializados con framework propio),
nombrados con deidades mitológicas según su rol.

> Cada archivo es un prompt/skill autónomo en Markdown. Para ver y copiar su contenido
> cómodamente, abre `../index.html` (chapter **Business Discovery**).

## Catálogo

| Archivo | Nombre | Tipo | Qué hace |
|---------|--------|------|----------|
| `anubis-pdd.md` | Anubis — Problem Driven Development | Skill | Senior PM + Systems Architect que diagnostica problemas de negocio con un framework de 6 etapas, detecta sesgos cognitivos, integra inteligencia y entrega roadmaps ejecutables. |
| `argos-analisis-categoria.md` | Argos — Inteligencia Competitiva | Prompt | Análisis de categoría de ecosistemas digitales: mercado competitivo, propuestas de valor, sentimiento de usuario, capacidades tecnológicas y tendencias. |
| `atenea-roadmap.md` | Atenea — Roadmap Estratégico | Skill | Diseño de roadmaps estratégicos. Valida hipótesis, diseña roadmaps MVE→R2→R3, se adapta a metodologías y lee tableros de Miro. |
| `cassandra-suposiciones-criticas.md` | Casandra — Suposiciones Críticas | Skill | Validación brutal de suposiciones críticas y simulación de riesgos tempranos: identifica Saltos de Fe, modela escenarios Monte Carlo y diseña experimentos. |
| `hermes-funcional.md` | Hermes — Definición Funcional | Skill | Definición funcional sin zonas grises para Financial y Retail: reglas de negocio, edge cases, Gherkin, entidades e impacto en procesos. |
| `maat-alcance-solucion.md` | Maat — Alcance de Solución | Skill | Definición de alcance quirúrgico. Convierte el diagnóstico de Anubis en un alcance acotado con Boundary Maps, Dependency Radars y Constraints Canvas. |
| `mimir-nsm.md` | Mímir — North Star Metric | Skill | Arquitectura de métricas de negocio: North Star Metric, OMTM, KPI Tree, embudos de conversión y plan de instrumentación. |
| `nemesis-detonantes.md` | Némesis — Detonantes | Skill | Procesa datos no estructurados para extraer detonantes reales: ingiere insumos crudos, extrae entidades, detecta fricción, clusteriza patrones y valida hipótesis. |
| `themis-guardrails.md` | Themis — Compliance & Guardrails | Skill | Inteligencia regulatoria y guardrails de diseño: mapea regulación según país e industria y traduce compliance en criterios de aceptación. |
| `thoth-definicion-funcional.md` | Thoth — Definición Funcional | Skill | Define requerimientos sin zonas grises: reglas de negocio, edge cases, Gherkin, entidades y análisis de impacto en procesos. |

## Flujo sugerido

Un recorrido típico de descubrimiento encadena varios de estos artefactos:

1. **Anubis** — diagnostica si el problema es real y su causa raíz.
2. **Némesis** — extrae detonantes desde datos no estructurados (entrevistas, soporte, reseñas).
3. **Casandra** — valida las suposiciones críticas y simula riesgos.
4. **Maat** — acota el alcance de la solución a partir del diagnóstico.
5. **Hermes / Thoth** — define el detalle funcional sin zonas grises.
6. **Mímir** — define la métrica norte y el plan de medición.
7. **Atenea** — convierte todo en un roadmap estratégico.
8. **Themis** y **Argos** aportan, en paralelo, contexto regulatorio y competitivo.
