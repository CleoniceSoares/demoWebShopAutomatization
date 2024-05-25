from pages.ApparelShoesPage import ApparelShoesPage

class Test4:

    def test_listar_quatro_itens_por_pagina(self, setup):
        home_page = setup
        home_page.open_home_page()
        assert home_page.is_url_home_page(), 'URL da HomePage está incorreta!'

        apparel_shoes_page = ApparelShoesPage(home_page.driver)
        apparel_shoes_page.clicar_apparel_shoes_menu()

        assert apparel_shoes_page.is_apparel_shoes_page(), 'URL de Apparel & Shoes incorreta'
        assert apparel_shoes_page.titulo_pagina_apparel_shoes(), 'Titulo da pagina Apparel & Shoes incorreto'

        assert apparel_shoes_page.clicar_display_per_page_four(), 'Quantidade de itens por pagina diferente de 4'

