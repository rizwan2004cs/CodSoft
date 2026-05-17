## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-18 - Timeline Images Accessibility
**Learning:** Decorative timeline illustrations accompanied by descriptive titles (like "School Student" or "Developer") cause redundant and noisy announcements for screen reader users when they contain duplicate or generic alt text.
**Action:** When an image serves purely as visual flair alongside descriptive text in a timeline or list, set `alt=""` and add `aria-hidden="true"` to explicitly hide it from assistive technologies.
