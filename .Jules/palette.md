## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.
## 2024-05-19 - Timeline Redundant Screen Reader Announcements
**Learning:** Timeline illustrations or icons that are immediately followed by identical descriptive text (e.g., `<img alt="School Student"> <div>School Student</div>`) cause screen readers to announce the same content twice ("School Student, image. School Student").
**Action:** Treat such illustrations as purely decorative by explicitly setting `alt=""` and adding `aria-hidden="true"` to the `<img>` tags to streamline screen reader navigation and prevent redundancy.
