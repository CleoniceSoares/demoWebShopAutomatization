from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.PageObject import PageObject

class CartPage(PageObject):
    url = 'https://demowebshop.tricentis.com/cart'
    nome_produto = (By.LINK_TEXT, '3rd Album')
    termo_de_aceite = (By.ID, 'termsofservice')
    button_checkout = (By.ID, 'checkout')
    button_checkout_guest = (By.CSS_SELECTOR, '[value="Checkout as Guest"]')

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

    def aceitar_termo(self):
        termo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.termo_de_aceite)
        )

        termo.click()

    def clicar_no_botao_checkout(self):
        checkout = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.button_checkout)
        )

        checkout.click()

    def clicar_no_botao_chekcout_guest(self):
        guest = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.button_checkout_guest)
        )

        guest.click()
