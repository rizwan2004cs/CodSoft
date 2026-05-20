## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-06-25 - Redundant Screen Reader Announcements for Descriptive Timelines
**Learning:** Timeline illustrations accompanied by explicitly descriptive titles often cause redundant and annoying screen reader announcements if their `alt` text repeats the same information.
**Action:** Always treat timeline illustrations accompanied by descriptive titles as purely decorative by setting `alt=""` and `aria-hidden="true"` on the image.
