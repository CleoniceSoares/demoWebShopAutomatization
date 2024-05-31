
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.SearchPage import SearchPage


class Test_Buy_Product:
    def test_efetivar_compra(self, setup):
        home_page = setup
        home_page.open_home_page()
        search_page = SearchPage(home_page.driver)
        cart_page = CartPage(home_page.driver)
        checkout_page = CheckoutPage(home_page.driver)

        home_page.realizar_pesquisa_de_produto('3rd Album')
        search_page.clicar_em_AddToCart()
        assert search_page.verificar_inclusao(), 'Nenhum produto adicionado ao carrinho!'
        search_page.acessar_carrinho()
        assert cart_page.verificar_produto_no_carrinho(), "O produto não está visível no carrinho"

        cart_page.aceitar_termo()
        cart_page.clicar_no_botao_checkout()
        cart_page.clicar_no_botao_chekcout_guest()
        assert checkout_page.is_url_checkout_page(), 'URL incorreta'

        checkout_page.preencher_campo_first_name('Jeferson')
        checkout_page.preencher_campo_last_name('Rodrigues')
        checkout_page.preencher_campo_email('teste@teste.com')
        checkout_page.preencher_campo_country('Brazil')
        checkout_page.preencher_campo_city('Brasilia')
        checkout_page.preencher_campo_address('Condominio Rio Negro casa 98')
        checkout_page.preencher_campo_postal('73093900')
        checkout_page.preencher_campo_phone('61987654321')
        checkout_page.clicar_no_botao_continuar_para_pagamento()
        checkout_page.verificar_meio_pagamento()
        checkout_page.clicar_no_botao_contunuar_para_resumo()
        assert checkout_page.verificar_resumo_produto, 'Produto diferente'
        checkout_page.clicar_no_botao_continuar_para_confirmar()
        checkout_page.clicar_no_botao_confirmar()
        assert checkout_page.verificar_mensagem_de_sucesso, 'Compra nao realizada'
