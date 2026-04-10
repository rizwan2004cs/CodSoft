## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-21 - Screen Reader Ambiguity for Math Operators
**Learning:** Screen readers often misinterpret standalone mathematical symbols (like *, /, -) as punctuation or ignore them altogether, leading to a confusing experience for visually impaired users using the calculator.
**Action:** Always add explicit aria-label attributes to calculator operator buttons to ensure their mathematical function is clearly announced.
