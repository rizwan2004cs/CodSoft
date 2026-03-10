from playwright.sync_api import sync_playwright

def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('file:///app/calculator/index.html')

        # Verify the input has the 'readonly' attribute
        input_el = page.locator('input')
        assert input_el.get_attribute('readonly') is not None, "Input is not readonly!"

        # Verify the input has the 'aria-label' attribute
        assert input_el.get_attribute('aria-label') == 'Calculator display', "aria-label is incorrect!"

        print("Test passed! Input element has readonly and aria-label attributes.")

        browser.close()

if __name__ == "__main__":
    test_calculator()