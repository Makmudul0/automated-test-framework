# tests/e2e_tests/test_login.py
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in the background
        page = browser.new_page()

        # Navigate to the login page
        page.goto("https://www.saucedemo.com/")

        # Fill in the username and password
        page.fill("#user-name", "standard_user")  # Correct selector for username field
        page.fill("#password", "secret_sauce")    # Correct selector for password field

        # Click the login button
        page.click("#login-button")

        # Verify login success
        assert "Products" in page.inner_text(".title")  # Verify the page title after login

        # Close the browser
        browser.close()