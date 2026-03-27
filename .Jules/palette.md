## 2024-03-27 - Calculator Input Accessibility & UX
**Learning:** Calculator display inputs that rely entirely on JavaScript buttons for state management cause unwanted mobile keyboard popups when focused, disrupting the UI. Furthermore, lacking an `aria-label` deprives screen reader users of context for the current display value.
**Action:** Always add `readonly` to input fields that are strictly display-only, and provide an `aria-label` (e.g., "Calculator display") to maintain state synchronization and improve accessibility.
