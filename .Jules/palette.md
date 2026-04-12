## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-18 - Calculator Standalone Symbols Accessibility
**Learning:** Standalone mathematical symbols (like `*`, `/`, `+`, `-`, `=`, `.`, `C`, `AC`, `%`) used as button labels often lack clear context for screen reader users, leading to ambiguity about their specific function.
**Action:** Explicitly define `aria-label` attributes for buttons containing standalone mathematical symbols or operators (e.g., `aria-label="Multiply"` for `*`) so their function is clearly announced.
