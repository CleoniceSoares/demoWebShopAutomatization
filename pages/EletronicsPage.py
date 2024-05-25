from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class EletronicsPage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    cellPhoneButton = (By.CSS_SELECTOR, ".sub-category-item a[href='/cell-phones']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_url_eletronics_page(self):
        return self.is_url(self.url)

    def click_on_cell_phone(self):
        self.driver.find_element(*self.cellPhoneButton).click()
