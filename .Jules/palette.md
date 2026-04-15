## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-20 - Calculator Operator Button Accessibility
**Learning:** Standalone mathematical symbols (like `+`, `-`, `*`, `/`, `%`) and abbreviations (`C`, `AC`) on calculator buttons can be ambiguous or mispronounced by screen readers, leading to poor accessibility for visually impaired users.
**Action:** Always add explicit, descriptive `aria-label` attributes (e.g., "Add", "Subtract", "Clear", "All Clear") to symbol and abbreviation buttons so that their functionality is clearly announced.
