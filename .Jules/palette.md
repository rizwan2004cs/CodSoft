## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-19 - Glassmorphism Text Contrast Requirements
**Learning:** Hardcoding low-contrast colors (like bright orange) as inline styles over semi-transparent glassmorphism backgrounds (like `rgba(255, 255, 255, 0.4)`) severely reduces text readability and fails accessibility guidelines, especially when the underlying background is a light unified gradient (`linear-gradient(135deg, #e0f7fa, #80deea)`).
**Action:** When styling text inside glassmorphism components (like navbars), always rely on the design system's established accessible primary accent color (e.g., `#00838f`) defined in the CSS stylesheet rather than overriding it with inline styles or custom utility classes that fail contrast checks.
