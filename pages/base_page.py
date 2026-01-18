from playwright.sync_api import expect, Locator

class BasePage:
    
    def __init__(self, page):
        self.page = page

    def get_locator(self, locator):
        return self.page.locator(locator)
    
    def validate_visible(self, locator):
        expect(self.get_locator(locator)).to_be_visible()

    def validate_invisible(self, locator):
        expect(self.get_locator(locator)).to_be_hidden()

    def wait_until_visible(self, locator):
        element = self.get_locator(locator)
        element.wait_for(state="visible") 

    def wait_until_hidden(self, locator):
        element = self.get_locator(locator)
        element.wait_for(state="hidden")