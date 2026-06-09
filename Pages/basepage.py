from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def url_link(self, path: str):
        self.page.goto(f"https://www.zenclass.in{path}")





