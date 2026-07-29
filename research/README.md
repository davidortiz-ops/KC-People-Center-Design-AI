# Research

> Chapter de **People Center Design - Pragma**.

Skills para **investigación de usuario y de mercado**. Cada skill define un flujo
operativo, controles de evidencia, formato de salida, compatibilidad y licencia de
uso interno exclusivo de Pragma.

Los prompts Markdown originales se conservan en [`backup/`](backup/) como material
legado para facilitar la comparación, auditoría y migración.

## Catálogo de skills

| Skill | Nombre | Qué hace |
|---|---|---|
| `analizar-contenido-tematico/` | Análisis de Contenido Temático | Codifica corpus cualitativos y genera categorías, diccionario e insights trazables. |
| `analizar-tendencias-mercado/` | Análisis de Tendencias de Mercado | Distingue tendencias y señales, evalúa evidencia y construye escenarios. |
| `extraer-vacantes-software/` | Extracción de Vacantes de Software | Extrae y normaliza datos auditables de anuncios de empleo. |
| `mapear-journey-conductual/` | Behavioral Customer Journey Map | Reconstruye journeys por actor y escenario con evidencia y confianza. |
| `crear-personas-ux/` | Creación de Personas UX | Crea segmentos conductuales sin demografía inventada ni estereotipos. |
| `diagnosticar-barreras-conductuales/` | Diagnóstico de Barreras Conductuales | Formula hipótesis causales y diseña intervenciones evaluables y éticas. |
| `simular-usuarios-banca-premium/` | Usuarios Sintéticos de Banca Premium | Opera perfiles sintéticos dentro de un sobre de evidencia explícito. |

## Estructura

Cada skill sigue la estructura recomendada por Anthropic:

```text
nombre-del-skill/
├── SKILL.md
├── LICENSE.txt
├── agents/
│   └── openai.yaml
└── evals/
    └── evals.json
```

- `SKILL.md`: frontmatter, activadores, compatibilidad, metadata e instrucciones.
- `LICENSE.txt`: licencia propietaria para uso interno exclusivo de Pragma.
- `agents/openai.yaml`: metadata de interfaz para Codex.
- `evals/evals.json`: casos realistas para verificar el comportamiento del skill.

No se incluyen `scripts/`, `references/` ni `assets` porque estos flujos no los
necesitan actualmente.

## Uso

Invoca el skill por nombre y proporciona los insumos de evidencia:

```text
Usa $analizar-contenido-tematico para codificar estas entrevistas.
Usa $analizar-tendencias-mercado para analizar estas fuentes.
Usa $extraer-vacantes-software para estructurar estas vacantes.
Usa $mapear-journey-conductual para mapear este recorrido.
Usa $crear-personas-ux para segmentar este corpus.
Usa $diagnosticar-barreras-conductuales para evaluar este abandono.
Usa $simular-usuarios-banca-premium para auditar este perfil.
```

## Prompts heredados

| Archivo en `backup/` | Skill sucesor |
|---|---|
| `analisis-contenido-tematico.md` | `analizar-contenido-tematico/` |
| `analisis-tendencias-mercado.md` | `analizar-tendencias-mercado/` |
| `analisis-vacantes-empleo.md` | `extraer-vacantes-software/` |
| `behavioral-customer-journey-map.md` | `mapear-journey-conductual/` |
| `creacion-user-persona.md` | `crear-personas-ux/` |
| `sesgos-cognitivos-intervenciones.md` | `diagnosticar-barreras-conductuales/` |
| `usuarios-sinteticos.md` | `simular-usuarios-banca-premium/` |

## Notas

- Estos skills esperan **insumos de evidencia** (entrevistas, transcripciones, documentos,
  datos) y producen artefactos accionables: personas, journey maps, codificaciones temáticas,
  escenarios de mercado o extracciones estructuradas.
- Encadenan bien con **Business Discovery**: los detonantes y personas que producen aquí
  alimentan el diagnóstico (Anubis/Némesis) y la definición de alcance.
- **Usuarios Sintéticos** y las **User Personas** sirven como sujetos/contexto para las
  evaluaciones de **Diseño de Soluciones**.
- Los usuarios sintéticos generan hipótesis; no sustituyen investigación con personas
  reales ni validan demanda o prevalencia.
