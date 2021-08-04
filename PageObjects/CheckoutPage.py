from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_xpath("//div[@class='card h-100']")
    products = (By.XPATH, "//div[@class='card h-100']")

    def get_product_list(self):
        return self.driver.find_elements(*CheckoutPage.products)

    # product_name = product.find_element_by_xpath("div/h4/a").text
    product = (By.XPATH, "//div[@class='card h-100']/div/h4/a")

    def get_product_name(self):
        return self.driver.find_element(*CheckoutPage.product)

    # product.find_element_by_xpath("div/button").click()
    product_button = (By.XPATH, "//div[@class='card h-100']/div/button")

    def click_product(self):
        return self.driver.find_element(*CheckoutPage.product_button)

    # self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
    checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def get_checkout_button(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
