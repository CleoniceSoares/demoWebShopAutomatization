from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject

class RegisterPage(PageObject):

    url_register = 'https://demowebshop.tricentis.com/register'
    url_home_page = 'https://demowebshop.tricentis.com/'
    register_title_element = (By.CLASS_NAME, 'page-title')
    register_title_text = 'Register'
    gender_field = (By.ID, 'gender-male')
    first_name_field = (By.ID, 'FirstName')
    last_name_field = (By.ID, 'LastName')
    email_field = (By.ID, 'Email')
    password_field = (By.ID, 'Password')
    confirm_password_field = (By.ID, 'ConfirmPassword')
    register_button = (By.ID, 'register-button')
    message_sucess_register = (By.CLASS_NAME, 'result')
    messagem_sucess_register_text = 'Your registration completed'
    continue_button = (By.CSS_SELECTOR, "input.button-1.register-continue-button")


    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver=driver)

    def clicar_link_register(self):
        self.driver.get(self.url_register)

    def titulo_pagina_register(self):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.register_title_element, self.register_title_text)
        )

    def preencher_dados_pessoais(self, first_name, last_name, email):
        gender = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.gender_field)
        )
        gender.click()
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.email_field).send_keys(email)

    def preencher_dados_senha(self, password='Teste123', password_confirm='Teste123'):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_field)
        )
        password_input.send_keys(password)
        self.driver.find_element(*self.confirm_password_field).send_keys(password_confirm)

    def clicar_botao_register(self):
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.register_button)
        )
        register_button.click()

    def tem_messagem_sucesso(self):
        message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_sucess_register)
        )
        is_message_displayed = message_element.is_displayed()
        has_message_text = message_element.text == self.messagem_sucess_register_text
        return is_message_displayed and has_message_text

    def clicar_botao_continue(self):
        continue_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()

    def is_url_home_page(self):
        return self.is_url(self.url_home_page)

    def is_url_register_page(self):
        return self.is_url(self.url_register)
