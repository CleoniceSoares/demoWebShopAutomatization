import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class HomePage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    campo_search = (By.ID, 'small-searchterms')
    botao_search = (By.CSS_SELECTOR, '[type="submit"]')
    jewelryButton = (By.XPATH, "//*[@class='top-menu']//*[contains(@href, 'jewelry')]")
    cellPhonesButton = (By.CSS_SELECTOR, "ul.sublist.firstLevel a[href='/cell-phones']")

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)

    def open_home_page(self):
        self.driver.get(self.url)

    def is_url_home_page(self):
        return self.is_url(self.url)

    def realizar_pesquisa_de_produto(self):
        self.driver.find_element(*self.campo_search).send_keys('Science')
        self.driver.find_element(*self.botao_search).click()
    def click_on_jewelry(self):
        self.driver.find_element(*self.jewelryButton).click()

    def click_on_cell_phones(self):
        self.driver.find_element(*self.cellPhonesButton).click()

