from playwright.sync_api import Page

class MainPage:
    COOKIE_GDPR = "cookiePolicyGDPR"
    COOKIE_GDPR_DETAILS = "cookiePolicyGDPR__details"
    COOKIE_INCPS = "cookiePolicyINCPS"
    GDPR_EXPECTED_VALUE_ALL_CHECKED = "4"
    GDPR_EXPECTED_VALUE_ANALYTICAL_ONLY = "3"
    GDPR_EXPECTED_VALUE_MARKETING_ONLY = "2"
    GDPR_EXPECTED_VALUE_TECHNICAL_ONLY = "1"
    INCPS_EXPECTED_VALUE = "true"
    GDPR_DETAILS_TIMESTAMP_KEY = "cookieCreateTimestamp"
    ING_DOMAIN = "ing.pl"
    HTTPS_PREFIX = "https://"
    
    def __init__(self, page: Page):
        self.page = page
        self.customize_button_selector = "button.js-cookie-policy-main-settings-button"
        self.accept_button_selector = "button.js-cookie-policy-main-accept-button"
        self.reject_button_selector = "button.js-cookie-policy-main-reject-button"
        self.technical_switch_selector = 'div.cookie-policy-toggle-button[name="CpmTechnicalOption"]' #disabled
        self.analytical_switch_selector = 'div.cookie-policy-toggle-button[name="CpmAnalyticalOption"]'
        self.marketing_switch_selector = 'div.cookie-policy-toggle-button[name="CpmMarketingOption"]'
        self.decline_all_button_selector = "button.js-cookie-policy-settings-decline-all-button"
        self.accept_selected_button_selector = "button.js-cookie-policy-settings-decline-button"

    def goto(self):
        self.page.goto("https://www.ing.pl/")

    def get_url(self):
        return self.page.url
    
    def get_cookies(self):
        return self.page.context.cookies()

    def is_technical_cookie_selected(self):
        element = self.page.query_selector(self.technical_switch_selector)
        return element.get_attribute("aria-checked") == "true" if element else False

    def is_analytical_cookie_selected(self):
        element = self.page.query_selector(self.analytical_switch_selector)
        return element.get_attribute("aria-checked") == "true" if element else False

    def is_marketing_cookie_selected(self):
        element = self.page.query_selector(self.marketing_switch_selector)
        return element.get_attribute("aria-checked") == "true" if element else False