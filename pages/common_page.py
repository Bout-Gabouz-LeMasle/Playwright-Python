from playwright.sync_api import expect, Locator

class CommonPage:
    
    def __init__(self, page):
        self.page = page

    def get_Locator(self, locator):
        return self.page.locator(locator)
    
    def validate_visible(self, locator):
        expect(self.get_Locator(locator)).to_be_visible()

    def validate_invisible(self, locator):
        expect(self.get_Locator(locator)).to_be_hidden()

    def wait_until_visible(self, locator):
        element = self.get_Locator(locator)
        element.wait_for(state="visible") 

    def wait_until_hidden(self, locator):
        element = self.get_Locator(locator)
        element.wait_for(state="hidden")