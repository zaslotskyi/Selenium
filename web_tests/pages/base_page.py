from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_element_located(locator))

    def look_for_element(self, locator):
        return self.driver.find_element(locator)
