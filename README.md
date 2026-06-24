# PromptsOps — Knowledge Center de People Center Design (Pragma)

Biblioteca de **skills, prompts y artefactos** del **Knowledge Center de People Center
Design** de **Pragma**. Reúne agentes y prompts reutilizables que cubren el ciclo de un
proyecto digital: **descubrimiento de negocio**, **diseño de soluciones**,
**investigación** y **SEO**.

La biblioteca se organiza en **chapters**. Cada chapter es una carpeta con sus artefactos
y su propia documentación (`README.md`).

En total: **43 artefactos** en **4 chapters**.

## Visor

Abre [`index.html`](index.html) en el navegador para explorar todos los artefactos en una
interfaz de tarjetas: agrupa por chapter, permite ver el contenido completo de cada archivo
y copiarlo al portapapeles. El visor lee los archivos directamente de las carpetas.

## Chapters

| Chapter | Carpeta | Artefactos | Enfoque |
|---------|---------|:----------:|---------|
| **Business Discovery** | [`Business Discovery/`](Business%20Discovery/README.md) | 10 | Diagnóstico de problemas, suposiciones, alcance, métricas y compliance. |
| **Diseño de Soluciones** | [`diseno-de-soluciones/`](diseno-de-soluciones/README.md) | 5 | UX, accesibilidad (WCAG) y madurez de design systems. |
| **Research** | [`research/`](research/README.md) | 7 | Investigación cualitativa y de mercado: personas, journey maps, tendencias. |
| **SEO** | [`seo/`](seo/README.md) | 21 | Auditoría, SEO técnico, contenido/E-E-A-T, datos de Google, local, GEO y estrategia. |

Cada chapter tiene su propio `README.md` con el catálogo detallado de sus artefactos.

## Tipos de artefacto

Los artefactos se clasifican según su forma de uso predominante (en el visor, cada tarjeta
muestra una puntuación 0-10 como **Prompt**, **Skill** y **Agente**):

- **Prompt** — Un system prompt autónomo que define un rol e instrucciones; se pega en el
  chat y opera en un solo turno guiado.
- **Skill** — Un paquete con framework, fases y (a veces) recursos/scripts, en formato de
  Claude Code: una carpeta con `SKILL.md` y frontmatter `name` + `description`.
- **Agente** — Artefacto orientado a operar de forma autónoma en múltiples pasos.
- **Referencia** — Material de contexto (p. ej. una proto-persona), no un agente ejecutable.

## Estructura

```
PromptsOps/
├── README.md                  ← este archivo (índice del Knowledge Center)
├── index.html                 ← visor de la biblioteca
├── Business Discovery/        ← chapter (10 artefactos + README)
├── diseno-de-soluciones/      ← chapter (5 artefactos + README)
├── research/                  ← chapter (7 artefactos + README)
└── seo/                       ← chapter (21 skills + scripts, references, hooks + README)
```
