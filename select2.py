import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://test-dxp.imbank.com/retail-onboarding/prospect/select-products")
    page.goto("https://test-dxp.imbank.com/retail-onboarding/prospect/init")
    page.goto("https://test-dxp.imbank.com/retail-onboarding/prospect/select-products")
    page.locator("[id=\"product-selection-journey--Club\\ Account\"] div").filter(has_text="Club Account This account is").nth(1).click()
    page.locator("[id=\"product-selection-journey--PayGo\\ Account\"] div").filter(has_text="PayGo Account This account").nth(1).click()
    page.get_by_role("button", name="Continue (2)").click()
    page.get_by_test_id("next").click()
    page.locator("Agree to terms and conditions").check()
    page.get_by_role("button", name="Get Started").click()
    page.get_by_label("Salutation / Title").select_option("2: MRS")
    page.locator("label").filter(has_text="Female").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
