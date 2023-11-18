from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    GOOGLE_URL = "https://www.google.com/"

    def open_google(self):
        self.driver.get(self.GOOGLE_URL)

    def search_for(self, search_term):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term)
        search_box.submit()
