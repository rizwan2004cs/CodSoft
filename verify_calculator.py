from playwright.sync_api import sync_playwright

def verify_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the calculator page directly from the file system
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/calculator/index.html")

        # Verify 1: Check if input is readonly
        input_element = page.locator("input[type='text']")
        is_readonly = input_element.get_attribute("readonly")
        print(f"Input readonly attribute: {is_readonly}")
        if is_readonly is not None:
            print("✅ Input is readonly")
        else:
            print("❌ Input is NOT readonly")

        # Verify 2: Check aria-label
        aria_label = input_element.get_attribute("aria-label")
        print(f"Input aria-label: {aria_label}")
        if aria_label == "Calculator Result":
             print("✅ Input has correct aria-label")
        else:
             print("❌ Input missing or incorrect aria-label")

        # Verify 3: Check focus styles (visual check via screenshot)
        # Tab to a button
        page.keyboard.press("Tab")
        page.keyboard.press("Tab") # Focus on first button
        page.screenshot(path="calculator_focus.png")
        print("✅ Screenshot taken: calculator_focus.png")

        # Verify 4: Check keyboard support
        # Press '1', '+', '2', '='
        page.keyboard.press("1")
        page.keyboard.press("+")
        page.keyboard.press("2")
        page.keyboard.press("Enter")

        # Check result
        result = input_element.input_value()
        print(f"Calculation result (1+2): {result}")

        if result == "3":
            print("✅ Keyboard support working")
        else:
            print(f"❌ Keyboard support failed, got {result}")

        page.screenshot(path="calculator_result.png")

        browser.close()

if __name__ == "__main__":
    verify_calculator()
