from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
    checkout_confirm = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def get_checkout_confirm(self):
        return self.driver.find_element(*ConfirmPage.checkout_confirm)

    # self.driver.find_element_by_id("country").send_keys("ind")
    input_cntry = (By.ID, "country")

    def get_input_cntry(self):
        return self.driver.find_element(*ConfirmPage.input_cntry)

    # self.driver.find_element_by_link_text("India").click()
    country_name = (By.LINK_TEXT, "India")

    def get_country_name(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    confirm_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.confirm_checkbox)

    # self.driver.find_element_by_css_selector("[type='submit']").click()
    submit_btn = (By.CSS_SELECTOR, "[type='submit']")

    def get_submit(self):
        return self.driver.find_element(*ConfirmPage.submit_btn)

    # message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
    success_txt = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def get_success_txt(self):
        return self.driver.find_element(*ConfirmPage.success_txt)
