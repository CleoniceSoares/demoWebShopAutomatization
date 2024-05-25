from pages.SearchPage import SearchPage


class Test_Search_Products:
    def test_realizar_pesquisa_de_produto(self, setup):
        home_page = setup
        home_page.open_home_page()
        search_page = SearchPage(home_page.driver)

        home_page.realizar_pesquisa_de_produto()
        search_page.verificar_resultado_da_pesquisa()