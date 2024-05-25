from pages.jewerlyPage import JewerlyPage


class Test007:

    def test_click_on_jewelry(self, setup):
        home_page = setup
        home_page.open_home_page()
        jewerly_page = JewerlyPage(home_page.driver)
        home_page.click_on_jewelry()
        jewerly_page.click_on_filter()
