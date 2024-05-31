from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.PageObject import PageObject

class CartPage(PageObject):
    url = 'https://demowebshop.tricentis.com/cart'
    nome_produto = (By.LINK_TEXT, '3rd Album')
    qtd_adicionada = (By.CLASS_NAME, 'qty nobr')

    def __init__(self, driver):
        self.driver = driver

    def is_url_cart_page(self):
        return self.is_url(self.url)

    def verificar_produto_no_carrinho(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.nome_produto)
        )

        verificar_nome_produto = link.is_displayed()

        return verificar_nome_produto
