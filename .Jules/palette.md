## 2024-05-24 - Calculator Display Accessibility
**Learning:** Using standard text inputs for custom calculator displays triggers mobile keyboards and lacks screen reader context.
**Action:** Always add `readonly` to prevent mobile keyboards and `aria-label` to provide screen reader context for custom input-based displays.
