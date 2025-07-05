#import os
import shutil
import pytest
from playwright.sync_api import sync_playwright
from tests.test_cookies import MainPage

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright_instance:
        yield playwright_instance

@pytest.fixture
def browser_context(playwright, request):
    browser_type_name = request.param
    browser_type = getattr(playwright, browser_type_name)
    browser = browser_type.launch(headless=True)  # headless=False 
    context = browser.new_context()
    context._browser_type_name = browser_type_name  
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="session", autouse=True)
def clean_cookies_screenshots():
    screenshot_dir  = "screenshots"
    shutil.rmtree(screenshot_dir, ignore_errors=True)