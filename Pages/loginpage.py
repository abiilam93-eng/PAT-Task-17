from playwright.sync_api import Page, sync_playwright

from Pages.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_ID = page.locator("input[placeholder='Enter your mail']")
        self.Password_button = page.locator("input[placeholder='Enter your password ']")
        self.Sign_in_button = page.locator("button[type='submit']")
        self.profile = page.locator("div[class = 'user-name-div']")
        self.logout_button = page.locator("//div[text()='Log out']")
        self.pop_up = page.locator("button[class='custom-close-button']")


    def navigate_url(self):
        self.url_link("/login")

    def __wait__(self):
        self.navigate_url()

    def login_cred(self, username: str, password: str):
        self.email_ID.fill(username)
        self.Password_button.fill(password)
        self.Sign_in_button.click()

    def enabled_input(self):
        self.email_ID.is_enabled()
        self.Password_button.is_enabled()

    def logout(self):
        self.pop_up.is_visible(timeout=5000)
        self.pop_up.click()
        self.profile.click()
        self.logout_button.is_visible(timeout=5000)
        self.logout_button.click()