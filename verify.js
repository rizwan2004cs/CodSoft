const { chromium } = require('playwright');
const fs = require('fs');
const assert = require('assert');

(async () => {
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await page.goto('file:///app/calculator/index.html');

        const input = await page.$('input[type="text"]');
        assert(input, 'Input element not found');

        const isReadonly = await input.getAttribute('readonly');
        assert.strictEqual(isReadonly, '', 'Input should be readonly');

        const ariaLabel = await input.getAttribute('aria-label');
        assert.strictEqual(ariaLabel, 'Calculator display', 'aria-label is incorrect');

        console.log('Verification passed: Input has readonly and aria-label attributes.');
    } catch (e) {
        console.error('Verification failed:', e.message);
        process.exitCode = 1;
    } finally {
        await browser.close();
    }
})();
