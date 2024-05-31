from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.PageObject import PageObject


class SearchPage(PageObject):
    url = 'https://demowebshop.tricentis.com/search?q=Science'
    imagem_produto = (By.CSS_SELECTOR, '[title="Show details for Science"]')
    titulo_produto = (By.CLASS_NAME, 'product-title')
    descricao_texto = 'Science'
    botao_AddToCart = (By.CSS_SELECTOR, '[value="Add to cart"]')
    carrinho = (By.CLASS_NAME, 'cart-qty')
    qtd_itens = '(1)'
    link_carrinho = (By.CLASS_NAME, 'button-1 cart-button')
    nome_carrinho = 'Shopping cart'
    link_carrinho_texto = (By.LINK_TEXT, 'Shopping cart')

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
        botao_add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.botao_AddToCart)
        )
        botao_add.click()

    def verificar_inclusao(self):
        carrinho_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.carrinho)
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: carrinho_element.text == self.qtd_itens
        )

        carrinho_atualizado = carrinho_element.is_displayed()
        qtd_produto = carrinho_element.text == self.qtd_itens

        return carrinho_atualizado and qtd_produto

    def acessar_carrinho(self):
        meu_carrinho = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.link_carrinho_texto)
        )

        meu_carrinho.click()
