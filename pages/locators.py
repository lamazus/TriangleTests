from selenium.webdriver.common.by import By 

class TrianglePageLocators():
    FIELD_A = (By.XPATH, '//input[@class="js_a"]')
    FIELD_B = (By.XPATH, '//input[@class="js_b"]')
    FIELD_C = (By.XPATH, '//input[@class="js_c"]')
    SUBMIT_BUTTON = (By.CLASS_NAME, "btn-submit")
    INFO_MESSAGE = (By.CSS_SELECTOR, "div.info")