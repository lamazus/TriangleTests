from pages.base_page import BasePage
from pages.locators import TrianglePageLocators
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class TrianglePage(BasePage):

    def check_triangle(self, a, b, c):
        field_a = self.browser.find_element(*TrianglePageLocators.FIELD_A)
        field_b = self.browser.find_element(*TrianglePageLocators.FIELD_B)
        field_c = self.browser.find_element(*TrianglePageLocators.FIELD_C)
        field_a.send_keys(a)
        field_b.send_keys(b)
        field_c.send_keys(c)
        self.browser.find_element(*TrianglePageLocators.SUBMIT_BUTTON).click()
        msg = self.browser.find_element(*TrianglePageLocators.INFO_MESSAGE)
        Wait(self.browser,5).until_not(EC.invisibility_of_element((msg)))
        field_a.clear()
        field_b.clear()
        field_c.clear()
        return msg
        
    def is_info_message_error(self,msg:WebElement):
        if msg.get_attribute("class").find("error") == -1:
            return False
        return True