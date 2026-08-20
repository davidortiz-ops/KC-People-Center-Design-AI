# PromptsOps — People Centered Design - Pragma

Biblioteca de **skills, prompts y artefactos** de **People Centered Design - Pragma**.
Reúne agentes y prompts reutilizables que cubren el ciclo de un proyecto digital:
**descubrimiento de negocio**, **diseño de soluciones**, **investigación** y **SEO**.

La biblioteca se organiza en **chapters**. Cada chapter es una carpeta con sus artefactos
y su propia documentación (`README.md`).

En total: **43 artefactos** en **4 chapters**.

## Cómo descargar y usar (sin conocimientos de Git)

> Este repositorio es **privado**. Para acceder necesitas estar **invitado** e **iniciar
> sesión** en GitHub con tu cuenta.

### Opción A — Leer directamente en GitHub (lo más simple)
1. Abre el repositorio en el navegador: `https://github.com/davidortiz-ops/KC-People-Center-Design-AI`
2. Entra a la carpeta del chapter que te interese y haz clic en cualquier archivo `.md`.
3. GitHub lo muestra formateado. Usa el botón **"Copy raw file"** (icono de copiar) para
   copiar el contenido y pegarlo donde lo necesites (por ejemplo, en el chat de la IA).

### Opción B — Descargar todo en un ZIP
1. En la página principal del repositorio, haz clic en el botón verde **`<> Code`**.
2. Elige **"Download ZIP"**.
3. Descomprime el archivo en tu computador (clic derecho → *Extraer todo*).
4. Abre cualquier archivo `.md` con un editor de texto, Bloc de notas o Visual Studio Code,
   o léelo desde el visor (ver abajo).

### Usar el visor `index.html`
El visor es un catálogo visual de todos los artefactos. Para que cargue el contenido de los
archivos, el navegador necesita "servir" la carpeta (al abrir el `index.html` con doble clic
puede que no cargue los textos por seguridad del navegador). La forma gratuita más sencilla:

1. Abre una terminal **dentro de la carpeta descargada**.
2. Ejecuta (requiere [Python](https://www.python.org/downloads/) instalado):
   ```
   python -m http.server 8000
   ```
3. Abre en el navegador: `http://localhost:8000/index.html`

> Si no tienes Python o prefieres algo más directo, usa la **Opción A** (leer en GitHub) o
> abre los archivos `.md` uno por uno desde la carpeta descargada.

## Visor

Abre [`index.html`](index.html) en el navegador para explorar todos los artefactos en una
interfaz de tarjetas: agrupa por chapter, permite ver el contenido completo de cada archivo
y copiarlo al portapapeles. El visor lee los archivos directamente de las carpetas.

## Chapters

| Chapter | Carpeta | Artefactos | Enfoque |
|---------|---------|:----------:|---------|
| **Business Discovery** | [`business-discovery/`](business-discovery/README.md) | 10 | Diagnóstico de problemas, suposiciones, alcance, métricas y compliance. |
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
├── README.md                  ← este archivo (índice de la biblioteca)
├── index.html                 ← visor de la biblioteca
├── business-discovery/        ← chapter (10 artefactos + README)
├── diseno-de-soluciones/      ← chapter (5 artefactos + README)
├── research/                  ← chapter (7 artefactos + README)
└── seo/                       ← chapter (21 skills + scripts, references, hooks + README)
```
