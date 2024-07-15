from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        page.screenshot(path="example.png")
        assert page.title() == "Example Domain"
        browser.close()

if __name__ == "__main__":
    test_example()

