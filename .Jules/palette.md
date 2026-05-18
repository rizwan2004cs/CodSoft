## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.

## 2024-05-18 - Timeline Illustration Accessibility
**Learning:** Screen readers announce alt text for images, which can be redundant and annoying if the image is immediately followed by a descriptive text title.
**Action:** When a timeline or list item includes an illustrative image next to its textual title, set `alt=""` and `aria-hidden="true"` on the image to make it decorative and avoid double-announcing the same concept to screen reader users.
