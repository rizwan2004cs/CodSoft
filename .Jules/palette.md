## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.
## 2024-05-18 - Redundant Image Alt Text in Timelines
**Learning:** Timeline illustrations or icons that are immediately followed by descriptive text headings create redundant and annoying screen reader announcements if their `alt` text simply mirrors the heading text.
**Action:** To prevent redundant screen reader announcements, treat timeline illustrations accompanied by descriptive titles as purely decorative by setting `alt=""` and `aria-hidden="true"` on the image element.
