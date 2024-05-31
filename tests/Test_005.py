from pages.CartPage import CartPage
from pages.SearchPage import SearchPage


class Test_Add_to_Cart:
    def test_incluir_produto_no_carrinho(self, setup):
        home_page = setup
        home_page.open_home_page()
        search_page = SearchPage(home_page.driver)
        cart_page = CartPage(home_page.driver)

        home_page.realizar_pesquisa_de_produto('3rd Album')
        search_page.clicar_em_AddToCart()
        assert search_page.verificar_inclusao(), 'Nenhum produto adicionado ao carrinho!'
        search_page.acessar_carrinho()
        assert cart_page.is_url_cart_page(), 'URL incorreta'
        assert cart_page.verificar_produto_no_carrinho(), "O produto não está visível no carrinho"
