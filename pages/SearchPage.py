from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject
class SearchPage(PageObject):

    url = 'https://demowebshop.tricentis.com/search?q=Science'
    imagem_produto = (By.CSS_SELECTOR, '[title="Show details for Science"]')
    titulo_produto = (By.CLASS_NAME, 'product-title')
    descricao_texto = 'Science'
    botao_AddToCart = (By.CSS_SELECTOR, '[value="Add to cart"]')
    carrinho = (By.CLASS_NAME, 'cart-qty')
    qtd_itens = '(1)'

    def __init__(self, driver):
        self.driver = driver

    def is_url_seach_page(self):
        return self.is_url(self.url)

    def verificar_resultado_da_pesquisa(self):
        produto_imagem = self.driver.find_element(*self.imagem_produto)
        produto_titulo = self.driver.find_element(*self.titulo_produto)

        visualizar_imagem_produto = produto_imagem.is_displayed()
        visualizar_descricao_produto = produto_titulo.text == self.descricao_texto

        return visualizar_descricao_produto and visualizar_imagem_produto

    def clicar_em_AddToCart(self):
        self.driver.find_element(*self.botao_AddToCart).click()

    def verificar_mensagem(self):
        carrinho_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.carrinho)
        )

        visualizar_mensagem = carrinho_element.is_displayed()
        verificar_texto = carrinho_element.text == self.qtd_itens

        return visualizar_mensagem and verificar_texto

    def acessar_carrinho(self):
        carrinho_qtd_itens = self.driver.find_element(*self.qtd_itens)