## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-18 - Calculator Operator Accessibility
**Learning:** Mathematical symbol buttons (like `*`, `/`, `-`) are often read out literally (e.g., "asterisk", "slash", "dash") by screen readers, making calculator apps confusing for visually impaired users.
**Action:** Always add descriptive `aria-label` attributes (e.g., "Multiply", "Divide", "Subtract") to non-numeric operator buttons to clearly communicate their function.
