from playwright.sync_api import sync_playwright
import os

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
OUTPUT_DIR = "outputs"

def scrape_and_screenshot(url):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=f"{OUTPUT_DIR}/chapter1.png", full_page=True)

        # Extract text from the main content
        text = page.inner_text("body")
        with open(f"{OUTPUT_DIR}/chapter1.txt", "w", encoding="utf-8") as f:
            f.write(text)

        browser.close()

if __name__ == "__main__":
    scrape_and_screenshot(URL)
