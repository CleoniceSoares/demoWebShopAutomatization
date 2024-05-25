
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
class SearchPage(PageObject):

    url = 'https://demowebshop.tricentis.com/search?q=Science'
    imagem_produto = (By.CSS_SELECTOR, '[title="Show details for Science"]')
    titulo_produto = (By.CLASS_NAME, 'product-title')
    descricao_texto = 'Science'
    botao_AddToCart = (By.CSS_SELECTOR, '[value="Add to cart"]')
    mensagem = (By.CSS_SELECTOR, 'p.content')
    texto_mensagem = 'The product has been added to your'
    qtd_itens = (By.CLASS_NAME, 'cart-qty')
    texto_menu = (By.XPATH, "//a[@href='/cart']")

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
        #mensagem_element =\
        self.driver.find_element(By.ID, 'bar-notification').is_displayed()

        #visualizar_mensagem = mensagem_element.is_displayed()
        #validar_mensagem = mensagem_element.text == self.texto_mensagem

        #return visualizar_mensagem and validar_mensagem
    def acessar_carrinho(self):
        carrinho_qtd_itens = self.driver.find_element(*self.qtd_itens)