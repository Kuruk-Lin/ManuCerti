from playwright.sync_api import Playwright, sync_playwright
import re


def website_sh(target_url):
    try:
        with sync_playwright() as playwright:
            # file_name = re.findall('http[s]?://www\.(\w+)\.com', target_url)
            file_name = target_url[target_url.find('.') + 1:target_url.rfind('.com')]
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(f"{target_url}")
            page.screenshot(path=f"{file_name}.png", full_page=True)
            browser.close()
            return True
    except Exception as er:
        print(f"{er}")
        return False
