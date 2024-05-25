from pages.ContactUsPage import ContactUsPage
from pages.WishListPage import WishListPage


class Test009:

    def submit_forms_on_contact_us(self, setup):
        home_page = setup
        home_page.open_home_page()
        contactus_page = ContactUsPage(home_page.driver)
        home_page.click_on_contactUs()
        contactus_page.contact_us_page("Lidiane", "lidiane@teste.com", "Lorem Ipsum is simply dummy text of the printing and typesetting industry.")

