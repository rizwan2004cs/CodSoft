import asyncio
from playwright.async_api import async_playwright
import sys

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto("file:///app/calculator/index.html")

            input_el = await page.query_selector("input[type='text']")
            assert input_el is not None, "Input element not found"

            is_readonly = await input_el.get_attribute("readonly")
            assert is_readonly == "", "Input should be readonly"

            aria_label = await input_el.get_attribute("aria-label")
            assert aria_label == "Calculator display", "aria-label is incorrect"

            print("Verification passed: Input has readonly and aria-label attributes.")
        except Exception as e:
            print("Verification failed:", str(e))
            sys.exit(1)
        finally:
            await browser.close()

asyncio.run(main())
