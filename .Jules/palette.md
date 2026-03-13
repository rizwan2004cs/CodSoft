## 2024-05-18 - Calculator Input Accessibility
**Learning:** Calculator display inputs often trigger unwanted mobile keyboard popups when tapped, ruining the UX, and lack semantic meaning for screen readers.
**Action:** Always add `readonly` and `aria-label="Calculator display"` to calculator input fields that are updated via custom on-screen buttons to ensure a smooth, accessible experience on all devices.
