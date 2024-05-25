from pages.CellPhonesPage import CellPhonesPage
from pages.EletronicsPage import EletronicsPage
from pages.SmartPhonePage import SmartPhonePage
from pages.WishListPage import WishListPage


class Test008:

    def test_add_product_to_wishlist(self, setup):
        home_page = setup
        home_page.open_home_page()
        eletronics_page = EletronicsPage(home_page.driver)
        cellphones_page = CellPhonesPage(home_page.driver)
        smartphone_page = SmartPhonePage(home_page.driver)
        wishlist_page = WishListPage(home_page.driver)
        home_page.click_on_eletronics()
        eletronics_page.click_on_cell_phone()
        cellphones_page.click_on_smartphone()
        smartphone_page.add_to_wishlist()
        wishlist_page.validate_product()


