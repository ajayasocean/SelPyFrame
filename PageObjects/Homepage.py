from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Always use CSS_SELECTOR with selenium.webdriver.common.by import By
    # shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def get_shop(self):
        return self.driver.find_element(*HomePage.shop)
