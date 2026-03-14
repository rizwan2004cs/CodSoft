## 2024-10-24 - Calculator Input Accessibility
**Learning:** The calculator input field was accessible but allowed the mobile keyboard to pop up on focus, disrupting the layout and providing a poor mobile user experience since all interactions are meant to happen via the on-screen buttons.
**Action:** Use `readonly` attribute on input fields that are designed strictly as "displays" to prevent unwanted keyboard popups while maintaining focusability and semantic structure, alongside a descriptive `aria-label`.
