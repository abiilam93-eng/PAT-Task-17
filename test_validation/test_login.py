from idlelib import browser

from playwright.sync_api import sync_playwright, Page, expect

from Pages.loginpage import LoginPage


def test_tc01_login_success(page:Page):
   login_page = LoginPage(page)
   login_page.navigate_url()
   login_page.login_cred("<email.id>", "<password>")
   expect(page).to_have_url("https://www.zenclass.in/dashboard")
   page.screenshot(path="Screenshots/tc01_screenshot.png")

def test_tc02_login_fail(page:Page):
   login_page = LoginPage(page)
   login_page.navigate_url()
   login_page.login_cred("<email.id>", "<invalid password>")
   expect(page).to_have_url("https://www.zenclass.in/dashboard")
   page.screenshot(path="Screenshots/tc02_screenshot.png")

def test_tc03_validate_input(page:Page):
   login_page = LoginPage(page)
   login_page.navigate_url()
   login_page.enabled_input()

def test_tc04_submitbtn_working(page:Page):
   login_page = LoginPage(page)
   login_page.navigate_url()
   login_page.login_cred("<email.id>", "<password>")
   expect(page).to_have_url("https://www.zenclass.in/dashboard")
   page.screenshot(path="Screenshots/tc04_screenshot.png")

def test_tc05_submitbtn_fail(page:Page):
   login_page = LoginPage(page)
   login_page.navigate_url()
   login_page.login_cred("<email.id>", "<password>")
   expect(page.locator("button[type='submit']")).to_be_hidden()

def test_tc06_logout_success(page:Page):
   login_page = LoginPage(page)
   login_page.navigate_url()
   login_page.login_cred("<email.id>", "<password>")
   expect(page).to_have_url("https://www.zenclass.in/dashboard")
   page.screenshot(path="Screenshots/tc06_new1.png")
   login_page.logout()
   page.screenshot(path="Screenshots/tc06_new2.png")
   expect(page).to_have_url("https://www.zenclass.in/login")




