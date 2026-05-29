## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2026-05-29 - Timeline Illustrations Accessibility
**Learning:** Timeline illustrations that are accompanied by descriptive titles and text can cause redundant and annoying screen reader announcements if they have descriptive `alt` text.
**Action:** Treat timeline illustrations as purely decorative by setting `alt=""` and `aria-hidden="true"` on the image when they are accompanied by text that conveys the same information.
