from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class ApparelShoesPage(PageObject):

    url_apparel_shoes = 'https://demowebshop.tricentis.com/apparel-shoes'

    apparel_shoes_menu = (By.XPATH, "//*[@class='top-menu']//*[contains(@href, 'apparel-shoes')]")
    display_per_page_select = (By.ID, 'products-pagesize')
    display_per_page_select_four = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/apparel-shoes?pagesize=4']")
    apparel_shoes_title_element = (By.CLASS_NAME, 'page-title')
    apparel_shoes_title_text = 'Apparel & Shoes'
    product_list_container = (By.CLASS_NAME, 'product-list')
    product_item_card = (By.CLASS_NAME, 'product-item')
    select_display_mode_list = (By.ID, 'products-viewmode')
    list_items = (By.CLASS_NAME, 'list-item')
    modo_lista_value = "https://demowebshop.tricentis.com/apparel-shoes?viewmode=list"

    def __init__(self, driver):
        super(ApparelShoesPage, self).__init__(driver=driver)

    def clicar_apparel_shoes_menu(self):
        self.clicar_menu(*self.apparel_shoes_menu)

    def is_apparel_shoes_page(self):
        return self.is_url(self.url_apparel_shoes)

    def titulo_pagina_apparel_shoes(self):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.apparel_shoes_title_element, self.apparel_shoes_title_text)
        )

    def clicar_display_per_page_four(self):
        self.driver.find_element(*self.display_per_page_select_four).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_item_card)
        )
        items = self.driver.find_elements(*self.product_item_card)
        if len(items) == 4:
            return True
        else:
            return False

    def selecionar_modo_lista(self):
        select_element = self.driver.find_element(*self.select_display_mode_list)
        select = Select(select_element)
        select.select_by_value(self.modo_lista_value)

    def verificar_modo_lista(self):
        list_container = self.driver.find_element(*self.product_list_container)
        product_items = list_container.find_elements(*self.product_item_card)
        if len(product_items) > 0:
            return True
        else:
            return False
