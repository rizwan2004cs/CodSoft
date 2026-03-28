## 2024-11-20 - Calculator Display Accessibility
**Learning:** Calculator display inputs should use `readonly` to prevent mobile keyboards from popping up, and an `aria-label` to ensure screen readers can announce the element's purpose properly since it lacks a visible label.
**Action:** When designing custom input interfaces like calculators where input is managed entirely via on-screen buttons, ensure the actual `<input>` element is marked `readonly` and has an appropriate `aria-label`.
