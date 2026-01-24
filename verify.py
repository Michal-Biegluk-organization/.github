
import asyncio
from playwright.async_api import async_playwright
import markdown
import os

async def main():
    with open("profile/README.mdx", "r") as f:
        mdx_content = f.read()

    html_content = markdown.markdown(mdx_content)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)

        # Expand the details section to make the stats visible
        summary_element = await page.query_selector("summary")
        if summary_element:
            await summary_element.click()
            # Wait for the image inside the details section to be loaded and visible
            await page.wait_for_selector('details[open] img', state='visible')


        # Ensure the screenshot directory exists
        os.makedirs("screenshots", exist_ok=True)

        await page.screenshot(path="screenshots/verification.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
