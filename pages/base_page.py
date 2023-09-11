from selenium.webdriver.remote.webdriver import WebDriver

class BasePage():
    def __init__(self, browser:WebDriver, url:str, timeout:int = 4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

