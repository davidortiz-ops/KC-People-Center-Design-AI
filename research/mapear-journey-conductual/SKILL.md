---
name: mapear-journey-conductual
description: Construye Behavioral Customer Journey Maps a partir de entrevistas, observaciones, analytics y evidencia de producto. Úsalo para mapear etapas, acciones, decisiones, emociones, motivaciones, fricciones, canales, transiciones y momentos de verdad para un actor y escenario concretos.
license: "Propietaria de Pragma; uso interno exclusivo. Ver LICENSE.txt."
compatibility: "Compatible con Claude Code, Codex y agentes que implementen Agent Skills. Requiere acceso de lectura a evidencia cualitativa o cuantitativa del journey."
metadata:
  author: "Pragma"
  version: "1.0.0"
  category: "ux-research"
  language: "es"
  source_prompt: "behavioral-customer-journey-map.md"
---

# Mapear journey conductual

## Licencia

Uso interno y exclusivo de Pragma conforme a `LICENSE.txt`. Prohibida su distribución o uso externo sin autorización previa y escrita.

## Compatibilidad

- Codex y agentes compatibles con `SKILL.md`.
- Entradas textuales, documentos y datos accesibles.
- Salida Markdown; JSON opcional.
- Sin recursos auxiliares.

## Flujo

1. Definir actor, segmento, escenario, objetivo, evento inicial y resultado final.
2. Identificar fuentes y asignarles IDs.
3. Separar conducta observada, conducta declarada e interpretación.
4. Derivar etapas desde la evidencia; usar etapas convencionales solo como hipótesis.
5. Mapear acciones, decisiones, pensamientos, emociones, motivaciones, fricciones, touchpoints y canales.
6. Identificar transiciones, abandonos, bucles, esperas y cambios de canal.
7. Crear journeys separados cuando los segmentos o escenarios sean incompatibles.
8. Priorizar momentos de verdad según frecuencia, severidad, impacto y confianza.
9. Formular oportunidades como necesidades o problemas, sin saltar a soluciones.

## Contrato de entrada

Recopilar:

- Actor o segmento.
- Escenario y alcance temporal.
- Objetivo del usuario.
- Inicio y final del recorrido.
- Producto, servicio y canales.
- Fuentes disponibles.
- Journey actual o deseado.

Si el corpus no permite reconstruir la secuencia, presentar un mapa parcial y explicar los vacíos.

## Reglas de evidencia

- Citar fuente y ubicación como `[F#]`.
- Etiquetar elementos como `Observado`, `Declarado` o `Inferido`.
- No atribuir pensamientos o emociones sin evidencia; marcarlos como inferidos y asignar confianza.
- No rellenar etapas sin evidencia con contenido genérico.
- No mezclar touchpoint, canal y acción.

## Salida

### Contexto

### Journey

| Etapa | Acciones y decisiones | Pensamientos | Emoción e intensidad | Motivaciones | Fricciones y severidad | Touchpoints | Canal | Evidencia | Tipo/confianza |
|---|---|---|---|---|---|---|---|---|---|

### Transiciones y rupturas

### Momentos de verdad

Para cada momento indicar evidencia, impacto, frecuencia, severidad y confianza.

### Oportunidades

Expresar cada oportunidad como “¿Cómo podríamos…?” solo cuando el usuario lo solicite; de lo contrario, describir necesidad, resultado deseado y evidencia.

### Vacíos de investigación

## Comprobación final

- Verificar que el journey corresponda a un actor y escenario.
- Verificar trazabilidad de etapas y emociones.
- Verificar que no se confunda el journey actual con el deseado.
- Separar hallazgos de recomendaciones.
- Eliminar etapas o conclusiones sin soporte.
