# e2e test for cart app in framework
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_e2e(self):
        print(self.driver.title)

        # clicking on shop button
        self.driver.find_element_by_xpath("//a[@href='/angularpractice/shop']").click()

        # getting title of shop page.
        print(self.driver.title)

        # finding product list.
        product_list = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        # traversing through card list to get product names.
        for product in product_list:
            product_name = product.find_element_by_xpath("div/h4/a").text
            if product_name == 'Blackberry':
                print(product_name)
                # clicking on add to cart button
                product.find_element_by_xpath("div/button").click()

        # scrolling upwards on web page using java script as selenium don't have scroll method
        # driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

        # clicking on checkout button
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        # self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click
        # driver.find_element_by_partial_link_text("Checkout").click()

        # clicking on checkout button on cart page.
        # driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        time.sleep(3)
        print(self.driver.current_url)

        # handling auto suggest for country name
        self.driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.driver.find_element_by_link_text("India").click()

        # clicking on checkbox
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        # clicking on Purchase button
        self.driver.find_element_by_css_selector("[type='submit']").click()

        # validating the success text
        message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        print(message)
        assert "Success!" in message
        self.driver.get_screenshot_as_file("Selenium/screenshot/e2e.png")
        print("2e2test.py finished execution")
