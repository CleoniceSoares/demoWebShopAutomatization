class Test008:

    def test_add_product_to_wishlist(self, setup):
        home_page = setup
        home_page.open_home_page()
        home_page.click_on_cell_phones()