## 2024-05-20 - Calculator Input Accessibility and Mobile UX
**Learning:** Using a standard text input for a custom calculator display causes mobile keyboards to pop up unnecessarily and lacks context for screen readers.
**Action:** Use `readonly` attribute to prevent keyboard popup on mobile while keeping it focusable, and add an explicit `aria-label` to provide context for screen readers.
