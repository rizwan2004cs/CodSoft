## 2024-10-24 - Prevent Mobile Keyboard & Sync State on Calculator Display
**Learning:** In simple JS calculators where state is maintained entirely in JS variables, allowing user input desyncs the visual state from internal state. On mobile, this also unhelpfully triggers the system keyboard when tapping the display. Making the input `readonly` solves both issues smoothly without complex state-sync logic.
**Action:** Always apply `readonly` and an `aria-label` to calculator or virtual keypad displays that are updated strictly via on-screen buttons.
