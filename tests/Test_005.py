import time

from pages.SearchPage import SearchPage


class Test_Add_to_Cart:
    def test_incluir_produto_no_carrinho(self, setup):
        home_page = setup
        home_page.open_home_page()
        search_page = SearchPage(home_page.driver)

        home_page.realizar_pesquisa_de_produto('Fiction')
        search_page.clicar_em_AddToCart()
        search_page.verificar_mensagem()
        #search_page.acessar_carrinho()
        time.sleep(10)

