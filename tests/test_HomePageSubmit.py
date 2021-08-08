# https://rahulshettyacademy.com/angularpractice/
# submit form on home page test case
import logging

import pytest

from PageObjects.Homepage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomeData import HomeData


class TestSubmitForm(BaseClass):
    def test_submit_form(self, get_data):
        log = self.get_logger()
        # print(self.driver.title)
        log.info(self.driver.title)
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data['name'])
        home_page.get_email().send_keys(get_data['email'])
        home_page.get_password().send_keys(get_data['password'])
        home_page.get_check().click()
        self.select_dd_option(home_page.get_gender(), get_data['gender'])
        home_page.get_radios().click()
        home_page.get_radioe().click()
        home_page.get_calender().send_keys('02/02/1993')
        home_page.get_submit().click()
        message = home_page.get_s_txt().text
        # print(message)
        log.info(message)
        assert "Success!" in message
        self.driver.get_screenshot_as_file("output/screenshots/submitscreen.png")
        # print("test_HomePageSubmit.py finished execution")
        log.info("test_HomePageSubmit.py finished execution")
        self.driver.refresh()

    # @pytest.fixture(params=[('Tester', 'qa@tester.com', 'test@123', 'Male', '02/02/1993'), ('qa', 'test@qa.com', 'test@1234', 'Female', '03/02/1993')])
    @pytest.fixture(params=HomeData.get_test_data('TC1'))
    def get_data(self, request):
        return request.param
