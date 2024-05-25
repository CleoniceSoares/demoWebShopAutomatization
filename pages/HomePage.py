from lib2to3.pgen2 import driver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class HomePage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    campo_search = (By.ID, 'small-searchterms')
    botao_search = (By.CSS_SELECTOR, '[type="submit"]')
    jewelryButton = (By.XPATH, "//*[@class='top-menu']//*[contains(@href, 'jewelry')]")
    eletronicsButton = (By.XPATH, "//a[@href='/electronics']")
    contactUsButton = (By.XPATH, "//a[@href='/contactus']")

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)

    def open_home_page(self):
        self.driver.get(self.url)

    def is_url_home_page(self):
        return self.is_url(self.url)

    def realizar_pesquisa_de_produto(self, produto):
        self.driver.find_element(*self.campo_search).send_keys(produto)
        self.driver.find_element(*self.botao_search).click()

    def click_on_jewelry(self):
        self.driver.find_element(*self.jewelryButton).click()

    def click_on_eletronics(self):
        self.driver.find_element(*self.eletronicsButton).click()

    def click_on_contactUs(self):
        self.driver.find_element(*self.contactUsButton).click()

