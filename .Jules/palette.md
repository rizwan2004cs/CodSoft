## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-18 - Timeline Image Accessibility
**Learning:** Timeline illustrations (like student, graduate icons) that are immediately followed by descriptive text (e.g., "School Student (2010 - 2020)") create redundant and noisy screen reader announcements when they contain `alt` text.
**Action:** Treat such accompanying illustrations as purely decorative by setting `alt=""` and `aria-hidden="true"` to streamline the screen reader experience.
