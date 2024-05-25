from pages.ApparelShoesPage import ApparelShoesPage

class Teste6:

    def test_visualizar_itens_numa_lista(self, setup):
        home_page = setup
        home_page.open_home_page()
        assert home_page.is_url_home_page(), 'URL da HomePage está incorreta!'

        apparel_shoes_page = ApparelShoesPage(home_page.driver)
        apparel_shoes_page.clicar_apparel_shoes_menu()

        assert apparel_shoes_page.is_apparel_shoes_page(), 'URL de Apparel & Shoes incorreta'
        assert apparel_shoes_page.titulo_pagina_apparel_shoes(), 'Titulo da pagina Apparel & Shoes incorreto'

        apparel_shoes_page.selecionar_modo_lista()
        assert apparel_shoes_page.verificar_modo_lista(), 'Modo Lista não foi selecionado'
