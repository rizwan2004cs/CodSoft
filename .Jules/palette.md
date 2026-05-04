## 2024-05-18 - Calculator Input Display Accessibility
**Learning:** Input fields (`<input type="text">`) used strictly as state displays for custom interactive components (like calculators) trigger unwanted mobile keyboard popups and confuse screen readers since they appear editable but are meant to be manipulated via separate on-screen buttons.
**Action:** Always add the `readonly` attribute and an appropriate `aria-label` (e.g., "Calculation result") to input fields used as pure displays in order to improve accessibility, maintain state synchronization, and prevent mobile keyboard interference.
## 2026-05-04 - [Glassmorphism Unified Theme]
**Learning:** [Applied unified liquid glass (glassmorphism) theme with responsive container stacking on mobile]
**Action:** [Ensure navbars use 'position: relative' rather than 'fixed' on mobile views to prevent component overlapping when scrolling/resizing]
