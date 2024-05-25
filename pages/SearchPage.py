import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
class SearchPage(PageObject):

    url = 'https://demowebshop.tricentis.com/search?q=Science'
    imagem_produto = (By.CSS_SELECTOR, '[title="Show details for Science"]')
    titulo_produto = (By.CLASS_NAME, 'product-title')

    def __init__(self, driver):
        self.driver = driver

    def is_url_seach_page(self):
        return self.is_url(self.url)

    def verificar_resultado_da_pesquisa(self):
        produto_imagem = self.driver.find_element(*self.imagem_produto).is_displayed()
        produto_titulo = self.driver.find_element(*self.titulo_produto).is_displayed()


