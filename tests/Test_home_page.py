class TestHomePage:

    def test_home_page(self, setup):
        home_page = setup

        home_page.open_home_page()

        assert home_page.is_url_home_page(), 'URL da HomePage está incorreta!'

