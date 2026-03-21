import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            record_video_dir="/home/jules/verification/video"
        )
        page = await context.new_page()

        await page.goto("file:///app/calculator/index.html")

        # Test basic functionality by clicking buttons
        await page.click("text='1'")
        await page.click("text='+'")
        await page.click("text='2'")
        await page.click("text='='")

        # Ensure the input is readonly
        is_readonly = await page.evaluate("document.querySelector('input').hasAttribute('readonly')")
        print(f"Input is readonly: {is_readonly}")

        # Ensure the input has aria-label
        aria_label = await page.evaluate("document.querySelector('input').getAttribute('aria-label')")
        print(f"Input aria-label: {aria_label}")

        os.makedirs("/home/jules/verification", exist_ok=True)
        await page.screenshot(path="/home/jules/verification/calculator.png")

        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
