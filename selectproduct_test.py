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
    page.get_by_label("Salutation / Title").select_option("2: MRS")
    page.locator("label").filter(has_text="Female").click()
    page.locator("#bb_input_16").click()
    page.locator("#bb_input_16").fill("Marto")
    page.locator("#bb_input_17").click()
    page.locator("#bb_input_17").fill("One")
    page.get_by_test_id("day").get_by_placeholder("DD").click()
    page.get_by_test_id("day").get_by_placeholder("DD").fill("01")
    page.get_by_test_id("month").get_by_placeholder("MM").click()
    page.get_by_test_id("month").get_by_placeholder("MM").fill("01")
    page.get_by_test_id("year").get_by_placeholder("YYYY").click()
    page.get_by_test_id("year").get_by_placeholder("YYYY").fill("2000")
    page.locator("#bb_input_21").click()
    page.locator("#bb_input_21").fill("36590165")
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("marto1@mailinator.com")
    page.get_by_label("Phone Input").click()
    page.get_by_label("Phone Input").fill("487287561")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Via Email").click()
    page.get_by_role("button", name="Send OTP").click()
    page.get_by_test_id("otp-code").locator("#ds-inm-otp-verification-journey-ang-otp").click()
    page.get_by_test_id("otp-code").locator("#ds-inm-otp-verification-journey-ang-otp").fill("123456")
    page.get_by_role("button", name="Continue").click()
    page.goto("https://test-dxp.imbank.com/retail-onboarding/prospect/identity-verification")
    page.get_by_text("Your personal security is").click()
    expect(page.get_by_role("heading")).to_contain_text("Smile for the camera")
    page.get_by_role("button", name="Start verification").click()
    page.locator("[data-testid=\"jumio-mock\"]").click()
    page.frame_locator("[data-testid=\"jumio-mock\"]").get_by_role("button", name="APPROVED AFTER RETRY").click()
    page.get_by_label("Continue").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
