from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class SmartPhonePage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    addToWishListButton = (By.ID, 'add-to-wishlist-button-43')
    successMessage = (By.LINK_TEXT, "wishlist")
    wishlistButton = (By.XPATH, "//*[@class='cart-label' and text()='Wishlist']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_url_smartphone_page(self):
        return self.is_url(self.url)

    def add_to_wishlist(self):
        self.driver.find_element(*self.addToWishListButton).click()
        assert SmartPhonePage.successMessage, 'The product has been added to your '
        self.driver.find_element(*self.wishlistButton).click()
