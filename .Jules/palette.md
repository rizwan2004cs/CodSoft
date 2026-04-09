## 2024-05-15 - Calculator Input Accessibility
**Learning:** Custom calculators that maintain their own state via JS variables and buttons shouldn't allow manual typing in their display inputs, as it causes unwanted mobile keyboards to pop up. Additionally, the display needs an aria-label to explain its purpose since it lacks a visible label.
**Action:** Always add `readonly` and an appropriate `aria-label` to custom calculator display inputs.
