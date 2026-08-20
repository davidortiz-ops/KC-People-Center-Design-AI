---
name: simular-usuarios-banca-premium
description: Construye, audita y opera perfiles sintéticos de clientes de banca premium basados en investigación identificable. Úsalo para explorar expectativas, criterios de confianza, fricciones y reacciones hipotéticas dentro de un perfil documentado, sin sustituir investigación real, validar demanda ni inventar comportamientos.
license: "Propietaria de Pragma; uso interno exclusivo. Ver LICENSE.txt."
compatibility: "Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere investigación base o un perfil documentado accesible como texto o archivo."
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
  category: "synthetic-user-research"
  language: "es"
  source_prompt: "usuarios-sinteticos.md"
---

# Simular usuarios de banca premium

## Licencia

Uso interno y exclusivo de Pragma conforme a `LICENSE.txt`. No copiar, distribuir, adaptar ni usar fuera de Pragma sin autorización previa y escrita.

## Compatibilidad

- Codex y agentes compatibles con `SKILL.md`.
- Requiere investigación base accesible o un perfil proporcionado por el usuario.
- Salida Markdown.
- Sin scripts, referencias ni assets.

## Límites de uso

Usar la simulación para generar hipótesis y preguntas de investigación. No usarla para:

- Sustituir entrevistas o pruebas con personas reales.
- Validar demanda, estimar prevalencia o representar a toda Latinoamérica.
- Tomar decisiones financieras, crediticias, legales, regulatorias o de cumplimiento.
- Crear evidencia o atribuir citas a usuarios inexistentes.
- Inferir patrimonio, datos sensibles o preferencias no documentadas.

Etiquetar toda respuesta simulada como `Hipótesis sintética`.

## Modos

### Construir perfil

1. Definir segmento, país o región, objetivo, fecha y fuentes.
2. Asignar IDs a las fuentes.
3. Extraer patrones confirmados, variaciones, fricciones, expectativas, lenguaje y límites.
4. Registrar para cada atributo evidencia, geografía, fecha y confianza.
5. Separar hechos, supuestos y elementos no determinados.

### Auditar perfil

1. Detectar afirmaciones sin fuente, contradicciones, estereotipos y falsa homogeneidad regional.
2. Identificar supuestos críticos y riesgos de inconsistencia.
3. Definir qué preguntas deben validarse con usuarios reales.
4. No completar vacíos durante la auditoría.

### Simular respuesta

1. Compilar un sobre de simulación con hechos, preferencias, reglas y prohibiciones documentadas.
2. Responder únicamente dentro de ese sobre.
3. Si la pregunta excede el perfil, responder `No determinado por el perfil`.
4. Indicar variables que podrían cambiar la respuesta y evidencia necesaria.
5. Mantener consistencia con el perfil auditado.

No mezclar modos en una misma entrega sin separar claramente sus resultados.

## Contrato de entrada

- Investigación base o perfil documentado.
- Segmento y límites de exclusión.
- País o región.
- Producto, canal o situación a explorar.
- Pregunta concreta.
- Modo solicitado.

Si no existe investigación suficiente, no activar un contexto base inventado. Solicitar evidencia o construir únicamente una plantilla de investigación.

## Perfil operativo

| Atributo | Valor | Evidencia | Fuente | Geografía/fecha | Tipo | Confianza |
|---|---|---|---|---|---|---|

Incluir:

- Relación con la banca.
- Objetivos financieros.
- Uso de canales y tareas.
- Criterios de confianza y desconfianza.
- Fricciones, miedos y límites.
- Necesidad de soporte humano.
- Variaciones internas.
- Casos que no representa.
- Supuestos por validar.

## Formato de simulación

### Hipótesis sintética

- Reacción inicial.
- Elementos que generarían confianza o desconfianza.
- Criterios de comparación.
- Disposición cualitativa: rechazo, cautela, interés condicionado o aceptación.
- Condiciones necesarias para avanzar.
- Base del perfil utilizada.
- Confianza.
- No determinado y preguntas para investigación real.

Usar puntuación 0–10 solo si el usuario la exige; acompañarla con anclas, evidencia y confianza.

## Comprobación final

- Verificar que cada afirmación esté dentro del sobre de simulación.
- Verificar que no haya citas ficticias.
- Verificar que se declare la naturaleza hipotética.
- Verificar variaciones regionales y límites.
- Retirar recomendaciones que pretendan validar el mercado con usuarios sintéticos.
