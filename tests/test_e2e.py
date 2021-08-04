# e2e test for cart app in framework
import time

from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.Homepage import HomePage
from utilities.BaseClass import BaseClass
from PageObjects.CheckoutPage import CheckoutPage


class TestE2E(BaseClass):
    def test_e2e(self):
        print(self.driver.title)

        # clicking on shop button in class itself  and creating next page object
        home_page = HomePage(self.driver)
        checkout_page = home_page.get_shop()
        # self.driver.find_element_by_xpath("//a[@href='/angularpractice/shop']").click()

        # getting title of shop page.
        # print(self.driver.title)

        # finding product list.
        # product_list = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        product_list = checkout_page.get_product_list()

        # traversing through card list to get product names.
        for product in product_list:
            # product_name = product.find_element_by_xpath("div/h4/a").text
            product_name = checkout_page.get_product_name().text

            if product_name == 'Blackberry':
                print(product_name)
                # clicking on add to cart button
                # product.find_element_by_xpath("div/button").click()
                checkout_page.click_product().click()

        # scrolling upwards on web page using java script as selenium don't have scroll method
        # driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

        # clicking on checkout button
        # self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        # self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click
        # driver.find_element_by_partial_link_text("Checkout").click()
        # checkout_page.get_checkout_button().click()

        # clicking on checkout button on cart page.
        # driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        # self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        # confirm_page = ConfirmPage(self.driver)
        confirm_page = checkout_page.get_checkout_button()
        confirm_page.get_checkout_confirm().click()
        time.sleep(1)

        # handling auto suggest for country name
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirm_page.get_input_cntry().send_keys("ind")

        # wait for country name to appear
        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.verify_link_text('India')

        # self.driver.find_element_by_link_text("India").click()
        confirm_page.get_country_name().click()

        # clicking on checkbox
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirm_page.get_checkbox().click()

        # clicking on Purchase button
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        confirm_page.get_submit().click()

        # validating the success text
        # message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        message = confirm_page.get_success_txt().text
        print(message)
        assert "Success!" in message
        self.driver.get_screenshot_as_file("output/screenshots/e2escreen.png")
        print("2e2test.py finished execution")
