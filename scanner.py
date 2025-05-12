import asyncio
from playwright.async_api import async_playwright
from triggers import load_blacklist, is_triggered

LOG_FILE = "trigger_comments_log.txt"

async def scan_comments(video_url: str, blacklist: list):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(video_url)
        await page.wait_for_selector("ytd-comments", timeout=15000)
        await asyncio.sleep(3)

        for _ in range(30):
            await page.mouse.wheel(0, -500)
            await asyncio.sleep(0.05)

        for _ in range(200):
            await page.mouse.wheel(0, 120)
            await asyncio.sleep(0.2)

        comment_elements = await page.query_selector_all("ytd-comment-thread-renderer")

        found_count = 0
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            for elem in comment_elements:
                author_elem = await elem.query_selector("#author-text span")
                content_elem = await elem.query_selector("#content-text")

                if author_elem and content_elem:
                    author = (await author_elem.inner_text()).strip()
                    content = (await content_elem.inner_text()).strip()

                    if is_triggered(content, blacklist):
                        found_count += 1
                        f.write(f"[{found_count}] {author}: {content}\n")

        await browser.close()
