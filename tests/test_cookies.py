import pytest
from pages.main_page import MainPage
from common.utils import Utils
import json

screenshot_dir = "screenshots"
@pytest.mark.parametrize("browser_context", ["chromium", "firefox", "webkit"], indirect=True)
def test_cookies(browser_context, request):
    page = browser_context.new_page()
    main = MainPage(page)

    main.goto()
    current_url = main.get_url()

    request.node._nodeid = f"test_cookies_in_{browser_context._browser_type_name}"

    assert MainPage.ING_DOMAIN in current_url
    assert current_url.startswith(MainPage.HTTPS_PREFIX)
    cookies_pre = main.get_cookies()
    for cookie in cookies_pre:
        print(f"Cookies before accept for {browser_context._browser_type_name}: {cookie['name']} = {cookie['value']}")

    page.click(main.customize_button_selector)

    if not main.is_analytical_cookie_selected():
        page.click(main.analytical_switch_selector)

    if main.is_marketing_cookie_selected():
        page.click(main.marketing_switch_selector)

    page.click(main.accept_selected_button_selector)
    cookies_post = main.get_cookies()
    for cookie in cookies_post:
        print(f"Cookies after accept for {browser_context._browser_type_name}: {cookie['name']} = {cookie['value']}")
    new_cookies = [cookie for cookie in cookies_post if cookie not in cookies_pre]

    for cookie in new_cookies:
        print(f"{cookie['name']} = {cookie['value']}")

    # assert expected cookies are set
    cookie_names = [cookie['name'] for cookie in cookies_post]
    assert MainPage.COOKIE_GDPR in cookie_names, f"{MainPage.COOKIE_GDPR} not found in cookies"
    assert MainPage.COOKIE_GDPR_DETAILS in cookie_names, f"{MainPage.COOKIE_GDPR_DETAILS} not found in cookies"
    assert MainPage.COOKIE_INCPS in cookie_names, f"{MainPage.COOKIE_INCPS} not found in cookies"

    # 4 for both selected, 3 for analytical + technical , 2 for  marketing + technical , 1 for technical only

    # Assert cookiePolicyGDPR value is 3 - for only analytical
    gdpr_cookie = next(cookie for cookie in cookies_post if cookie['name'] == MainPage.COOKIE_GDPR)
    assert gdpr_cookie['value'] == MainPage.GDPR_EXPECTED_VALUE_ANALYTICAL_ONLY, \
        f"{MainPage.COOKIE_GDPR} value is {gdpr_cookie['value']} instead of {MainPage.GDPR_EXPECTED_VALUE_ANALYTICAL_ONLY}"

    # Assert cookiePolicyGDPR__details contains text "cookieCreateTimestamp"
    gdpr_details_cookie = next(cookie for cookie in cookies_post if cookie['name'] == MainPage.COOKIE_GDPR_DETAILS)
    details_value = json.loads(gdpr_details_cookie['value'])
    assert MainPage.GDPR_DETAILS_TIMESTAMP_KEY in details_value, \
        f"{MainPage.GDPR_DETAILS_TIMESTAMP_KEY} not found in {MainPage.COOKIE_GDPR_DETAILS}"

    # Assert cookiePolicyINCPS value is true 
    incps_cookie = next(cookie for cookie in cookies_post if cookie['name'] == MainPage.COOKIE_INCPS)
    assert incps_cookie['value'] == MainPage.INCPS_EXPECTED_VALUE, \
        f"{MainPage.COOKIE_INCPS} value is {incps_cookie['value']} instead of {MainPage.INCPS_EXPECTED_VALUE}"
    
    # Get the screenshot
    screenshot_path = f"{screenshot_dir}/cookies_{browser_context._browser_type_name}_{Utils.get_actual_timestamp()}.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved as: {screenshot_path}")
    page.close()