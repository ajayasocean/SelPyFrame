# https://rahulshettyacademy.com/angularpractice/
# submit form on home page test case

from PageObjects.Homepage import HomePage
from utilities.BaseClass import BaseClass


class TestSubmitForm(BaseClass):
    def test_submit_form(self):
        print(self.driver.title)
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys("Tester")
        home_page.get_email().send_keys("qa@tester.com")
        home_page.get_password().send_keys("test@123")
        home_page.get_check().click()
        self.select_dd_option(home_page.get_gender(), "Male")
        home_page.get_radios().click()
        home_page.get_radioe().click()
        home_page.get_calender().send_keys("02/02/1993")
        home_page.get_submit().click()
        message = home_page.get_s_txt().text
        print(message)
        assert "Success!" in message
        self.driver.get_screenshot_as_file("output/screenshots/e2escreen.png")
        print("test_HomePageSubmit.py finished execution")
