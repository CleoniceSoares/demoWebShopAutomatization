from pages.ContactUsPage import ContactUsPage
from pages.WishListPage import WishListPage


class Test009:

    def test_add_product_to_wishlist(self, setup):
        home_page = setup
        home_page.open_home_page()
        contactus_page = ContactUsPage(home_page.driver)
        home_page.click_on_contactUs()
        contactus_page.contact_us_page("Lidiane", "lidiane@teste.com", "Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
