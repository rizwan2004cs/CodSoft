## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.
## 2024-05-18 - Timeline Image Accessibility
**Learning:** Screen readers announce both image alt text and adjacent descriptive titles, leading to redundant and annoying duplicated reading when illustrations mirror the title text (e.g., an image with `alt="School Student"` next to a title "School Student").
**Action:** When an image serves purely as a visual illustration for a directly adjacent, self-explanatory title (like in a timeline), always treat it as decorative by explicitly setting `alt=""` and `aria-hidden="true"` to prevent redundant screen reader announcements.
