from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # use CSS_SELECTOR with selenium.webdriver.common.by import By
    # shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def get_shop(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    # driver.find_element_by_name('name')
    name_field = (By.NAME, 'name')

    def get_name(self):
        return self.driver.find_element(*HomePage.name_field)

    email_field = (By.NAME, 'email')

    def get_email(self):
        return self.driver.find_element(*HomePage.email_field)

    password = (By.ID, "exampleInputPassword1")

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    checkbox = (By.ID, "exampleCheck1")

    def get_check(self):
        return self.driver.find_element(*HomePage.checkbox)

    gender = (By.ID, 'exampleFormControlSelect1')

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    radio_student = (By.ID, 'inlineRadio1')

    def get_radios(self):
        return self.driver.find_element(*HomePage.radio_student)

    radio_employed = (By.ID, 'inlineRadio2')

    def get_radioe(self):
        return self.driver.find_element(*HomePage.radio_employed)

    calender = (By.NAME, "bday")

    def get_calender(self):
        return self.driver.find_element(*HomePage.calender)

    sbmt_btn = (By.CSS_SELECTOR, "[type='submit']")

    def get_submit(self):
        return self.driver.find_element(*HomePage.sbmt_btn)

    s_txt = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def get_s_txt(self):
        return self.driver.find_element(*HomePage.s_txt)


