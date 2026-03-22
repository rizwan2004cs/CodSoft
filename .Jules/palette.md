## 2024-03-20 - Mobile Native Keyboard Overlap on Custom UIs
**Learning:** When building a custom virtual keyboard (like a calculator app), a standard `<input type="text">` will trigger the native mobile keyboard on touch, blocking the custom UI.
**Action:** Always add the `readonly` attribute to input fields that are populated entirely by custom on-screen buttons to prevent native keyboard popups while maintaining value display. Also include an `aria-label` so screen readers understand the input's purpose since it acts as a display.
