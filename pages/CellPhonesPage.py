from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CellPhonesPage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    smartPhoneButton = (By.XPATH, "//a[@href='/smartphone']")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_url_cellphone_page(self):
        return self.is_url(self.url)

    def click_on_smartphone(self):
        self.driver.find_element(*self.smartPhoneButton).click()


