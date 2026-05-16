## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-24 - Hiding Redundant Timeline Images
**Learning:** Images inside timeline components that are accompanied by full descriptive titles (e.g., 'School Student (2010 - 2020)') create repetitive announcements for screen readers if they have alt text.
**Action:** Use `alt=""` and `aria-hidden="true"` on these decorative icons to streamline the screen reader experience without losing contextual meaning.
