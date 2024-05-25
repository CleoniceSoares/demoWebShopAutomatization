from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class WishListPage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    titleWishList = (By.CLASS_NAME, 'page-title')
    productTitle = (By.XPATH, "//*[@href='/smartphone']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_url_wishlist_page(self):
        return self.is_url(self.url)

    def validate_product(self):
        assert WishListPage.titleWishList, 'Wishlist'
        assert WishListPage.productTitle, 'Smartphone'
