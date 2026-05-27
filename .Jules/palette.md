## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-19 - Redundant Timeline Illustration Descriptions
**Learning:** Timeline illustrations or icons that are directly accompanied by descriptive titles or text content cause redundant and noisy screen reader announcements if they retain their descriptive `alt` tags. Screen readers will read the image's description, and then immediately read the same information in the title.
**Action:** Always make accompanying timeline illustrations or redundant visual icons purely decorative by setting `alt=""` and adding `aria-hidden="true"` to prevent redundant screen reader announcements. Let the text content do the talking.
