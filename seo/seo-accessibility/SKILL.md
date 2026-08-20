---
name: seo-accessibility
description: >
  Roles ARIA, navegación de salto (skip links), gestión de foco en SPAs, alt text
  y prácticas de accesibilidad (WCAG 2.1 AA) que impactan directamente el SEO y la
  rastreabilidad. Úsala cuando el usuario diga "accesibilidad", "ARIA", "WCAG",
  "skip link", "navegación de salto", "lector de pantalla", "gestión de foco",
  "accessibility", "a11y", o cuando construya navegación, formularios, modales o
  componentes interactivos que deban ser accesibles e indexables.
version: 2.0.0
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
---

# SEO: Accesibilidad

## Cuándo usarlo
Usa esta skill cuando:
- Construyas navegación, formularios, modales o componentes interactivos.
- Implementes navegación de salto o gestión de foco.
- Agregues atributos ARIA a contenido dinámico.
- Necesites garantizar compatibilidad con lectores de pantalla (lo que también beneficia la comprensión de los motores de búsqueda).

## Entradas requeridas
- El tipo de componente interactivo que se está construyendo (nav, modal, tabs, accordion, etc.).
- Si la página tiene actualizaciones de contenido dinámico (SPAs, carga AJAX).
- Nivel objetivo de cumplimiento WCAG (generalmente 2.1 AA).

## Procedimiento

### 1. Roles ARIA Landmark
- Usa primero elementos semánticos HTML (`<nav>`, `<main>`, `<aside>`, etc.).
- Solo agrega roles ARIA cuando el HTML semántico no sea suficiente.

```html
<!-- ✅ HTML semántico (preferido) -->
<nav aria-label="Navegación principal">
  <ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about">Acerca de</a></li>
  </ul>
</nav>

<main>
  <article>Contenido...</article>
</main>

<!-- Agrega ARIA solo cuando sea necesario -->
<div role="search">
  <form>
    <label for="search-input">Buscar</label>
    <input type="search" id="search-input" name="q" />
  </form>
</div>
```

### 2. Navegación de Salto
- Cada página DEBE tener un enlace de salto al contenido como primer elemento enfocable.
- Esto ayuda a los lectores de pantalla Y mejora la rastreabilidad al definir el área de contenido principal.

```html
<body>
  <a href="#main-content" class="skip-link">Saltar al contenido principal</a>
  <header>...</header>
  <nav>...</nav>
  <main id="main-content">
    <!-- Contenido principal -->
  </main>
</body>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px 16px;
  background: #000;
  color: #fff;
  z-index: 100;
  transition: top 0.2s;
}

.skip-link:focus {
  top: 0;
}
```

### 3. Gestión de Foco en SPAs
- Después de la navegación del lado del cliente, mueve el foco al `<h1>` de la nueva página o al área de contenido principal.
- Anuncia los cambios de ruta a los lectores de pantalla.

```jsx
// Ejemplo con React Router
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

function RouteAnnouncer() {
  const location = useLocation();

  useEffect(() => {
    const heading = document.querySelector('h1');
    if (heading) {
      heading.setAttribute('tabindex', '-1');
      heading.focus();
    }
  }, [location.pathname]);

  return (
    <div aria-live="polite" aria-atomic="true" className="sr-only">
      Navegado a {document.title}
    </div>
  );
}
```

### 4. Accesibilidad en Imágenes y Multimedia
- Todas las imágenes deben tener atributos `alt` (con `alt=""` vacío para imágenes puramente decorativas).
- Los videos deben tener subtítulos o transcripciones.
- Usa `aria-describedby` para imágenes complejas como gráficos.

```html
<!-- Imagen informativa -->
<img src="/chart.png" alt="Las ventas crecieron un 45% en el tercer trimestre de 2025" />

<!-- Imagen decorativa -->
<img src="/divider.svg" alt="" role="presentation" />

<!-- Imagen compleja -->
<figure>
  <img src="/infographic.png" alt="Proceso de auditoría SEO" aria-describedby="infographic-desc" />
  <figcaption id="infographic-desc">
    Proceso paso a paso de auditoría SEO: análisis de rastreo, auditoría de contenido, revisión técnica y plan de acción.
  </figcaption>
</figure>
```

## Verificación
- **Auditoría de accesibilidad Lighthouse:** Puntaje ≥ 90.
- **Prueba con lector de pantalla:** Navega con VoiceOver (Mac) o NVDA (Windows) para verificar el orden del contenido.
- **Navegación por teclado:** Presiona Tab a lo largo de toda la página — cada elemento interactivo debe ser alcanzable.
- **axe DevTools:** Ejecuta la [extensión de navegador axe](https://www.deque.com/axe/) para verificaciones automatizadas.

## Modos de falla / depuración
| Problema | Causa | Solución |
|---|---|---|
| Los lectores de pantalla se saltan el contenido principal | Falta el enlace de navegación de salto | Agrega `<a href="#main-content">` como primer elemento enfocable |
| El foco se pierde después de navegación SPA | Sin gestión de foco tras cambio de ruta | Mueve el foco al `<h1>` o contenido principal después de navegar |
| El uso excesivo de ARIA genera ruido | Roles ARIA duplicando elementos semánticos | Elimina ARIA redundante; usa HTML semántico en su lugar |
| Imágenes decorativas son leídas en voz alta | Falta `alt=""` en imágenes decorativas | Agrega `alt=""` vacío y `role="presentation"` |

## Escalamiento
- Si el cumplimiento de WCAG requiere un rediseño significativo de la interfaz, consulta a un especialista en accesibilidad.
- Si componentes de terceros (selectores de fecha, carruseles) carecen de accesibilidad, escala al proveedor del componente o considera alternativas accesibles.
