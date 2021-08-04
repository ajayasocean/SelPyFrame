import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:
    def verify_link_text(self, l_text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, l_text)))

    def select_dd_option(self, locator, text):
        gender_dropdown = Select(locator)
        gender_dropdown.select_by_visible_text(text)
        gender_dropdown.select_by_index(0)



