---
name: crear-personas-ux
description: Crea personas UX conductuales y accionables a partir de entrevistas, encuestas, observaciones y otras fuentes de investigación. Úsalo para segmentar usuarios por objetivos, comportamientos, contexto, barreras y criterios de decisión, manteniendo trazabilidad y evitando estereotipos o atributos inventados.
license: "Propietaria de Pragma; uso interno exclusivo. Ver LICENSE.txt."
compatibility: "Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura a evidencia de investigación de usuarios."
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
metadata:
  author: "Pragma"
  version: "1.0.0"
  category: "ux-research"
  language: "es"
  source_prompt: "creacion-user-persona.md"
---

# Crear personas UX

## Licencia

Uso interno y exclusivo de Pragma conforme a `LICENSE.txt`. No copiar, distribuir, adaptar ni usar fuera de Pragma sin autorización previa y escrita.

## Compatibilidad

- Codex y agentes compatibles con `SKILL.md`.
- Entradas de investigación accesibles como texto o archivos.
- Salida Markdown; JSON opcional.
- Sin scripts, referencias ni assets.

## Flujo

1. Definir pregunta de investigación, producto, mercado y decisión que apoyarán las personas.
2. Asignar IDs a fuentes y participantes.
3. Extraer objetivos, tareas, conductas, contexto, barreras, necesidades y criterios de decisión.
4. Proponer segmentos solo cuando existan diferencias conductuales sustentadas.
5. Buscar evidencia que contradiga cada segmento.
6. Construir el mínimo número de personas que explique variaciones relevantes.
7. Documentar cobertura, variación interna, límites y vacíos.
8. Validar que cada atributo sea útil para decisiones de producto, diseño o negocio.

## Reglas

- Priorizar variables conductuales sobre demográficas.
- Incluir demografía solo si es explícita, relevante y no sensible.
- No inferir raza, etnia, salud, orientación, religión, ideología, patrimonio ni otros atributos sensibles.
- No crear una persona cuando el corpus no soporte una segmentación; entregar patrones provisionales.
- No inventar nombres, biografías ni citas para dar realismo.
- Usar un nombre funcional del segmento; añadir un nombre ficticio solo si el usuario lo exige y marcarlo como recurso editorial.
- Usar verbatims literales con fuente. Si se resume una voz, etiquetarla como `Paráfrasis` y no usar comillas.
- Distinguir `Observado`, `Inferido` y `No determinado`.

## Salida

### Base de segmentación

Explicar variables, evidencia, tamaño o cobertura disponible y limitaciones.

### Persona: [nombre funcional]

- Descripción conductual.
- Situaciones y contexto de uso.
- Objetivos y tareas.
- Motivaciones y criterios de decisión.
- Estrategias y comportamientos actuales.
- Barreras, frustraciones y necesidades.
- Autonomía digital, familiaridad y soporte requerido.
- Verbatims con fuentes.
- Variaciones internas.
- Límites: qué casos no representa.
- Supuestos y confianza.

### Matriz de evidencia

| Atributo | Evidencia | Fuente/participantes | Tipo | Confianza |
|---|---|---|---|---|

### Diferencias entre personas

### Implicaciones y preguntas pendientes

Formular implicaciones sin convertirlas automáticamente en soluciones.

## Comprobación final

- Verificar evidencia para cada atributo.
- Verificar que las personas sean mutuamente distinguibles.
- Eliminar estereotipos y demografía decorativa.
- Verificar que ninguna paráfrasis parezca una cita.
- Indicar si la muestra no permite estimar prevalencia.
