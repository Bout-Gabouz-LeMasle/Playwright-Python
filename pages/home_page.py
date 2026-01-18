from playwright.sync_api import Page
from locators.home_locators import HomeLocators
from pages.common_page import CommonPage


class HomePage(CommonPage):

    def __init__(self, page: Page, url_conf: str):
        super().__init__(page)
        self.url = url_conf

    def navigate(self):
        self.page.goto(self.url)
        self.wait_until_visible(HomeLocators.ROOT_DIV)

        self.validate_visible(HomeLocators.ROOT_DIV)
        self.validate_visible(HomeLocators.USER_INPUT)
        self.validate_visible(HomeLocators.PASS_INPUT)
        self.validate_visible(HomeLocators.LOGIN_BUTTON)
        

    def login(self, user, password):
        self.get_Locator(HomeLocators.USER_INPUT).fill(user)
        self.get_Locator(HomeLocators.PASS_INPUT).fill(password)
        self.get_Locator(HomeLocators.LOGIN_BUTTON).click()

        self.wait_until_hidden(HomeLocators.LOGIN_BUTTON)
        self.validate_invisible(HomeLocators.LOGIN_BUTTON)
