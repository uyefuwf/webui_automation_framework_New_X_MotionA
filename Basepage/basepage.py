class BasePage:

    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator, timeout=10000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def select_option(self, locator, value):
        self.page.locator(locator).select_option(value)

    def get_all_texts(self, locator):
        return self.page.locator(locator).all_text_contents()

    def get_title(self):
        return self.page.title()