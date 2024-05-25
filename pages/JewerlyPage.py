from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class JewerlyPage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    filterByPriceButton = (By.XPATH, "//span[@class='PriceRange' and text()='0.00']")
    diamondBraceletTxt = (By.LINK_TEXT, "Diamond Tennis Bracelet")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_url_jewelry_page(self):
        return self.is_url(self.url)

    def click_on_filter(self):
        self.driver.find_element(*self.filterByPriceButton).click()
        assert JewerlyPage.diamondBraceletTxt, 'Diamond Tennis Bracelet'
