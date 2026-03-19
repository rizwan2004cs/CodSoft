## 2024-05-24 - Calculator Input UX
**Learning:** Custom calculator inputs require `readonly` to prevent state desync and mobile keyboard popups, and an `aria-label` for accessibility.
**Action:** Always add `readonly` and `aria-label` to custom input fields that maintain state via buttons.