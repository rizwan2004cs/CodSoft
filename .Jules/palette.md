## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2026-05-19 - Timeline Image Accessibility
**Learning:** Timeline illustrations accompanied by descriptive titles cause redundant screen reader announcements and distraction if not treated as purely decorative.
**Action:** Set `alt=""` and `aria-hidden="true"` on timeline images to treat them as purely decorative.
