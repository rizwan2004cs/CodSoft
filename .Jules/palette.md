## 2025-05-18 - Calculator Accessibility
**Learning:** Common pattern in beginner calculators: multiple elements sharing the same `id` for styling (e.g., `id="ora"`), and inputs lacking `readonly` despite logic only handling button clicks.
**Action:** Always replace duplicate IDs with classes for styling. Make calculator inputs `readonly` unless manual typing is explicitly supported, to prevent misleading user experience.
