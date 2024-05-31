from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from pages.PageObject import PageObject


class CheckoutPage(PageObject):
    url = 'https://demowebshop.tricentis.com/onepagecheckout'

    campo_First_name = (By.ID, 'BillingNewAddress_FirstName')
    campo_Last_name = (By.ID, 'BillingNewAddress_LastName')
    campo_Email = (By.ID, 'BillingNewAddress_Email')
    campo_Country = (By.ID, 'BillingNewAddress_CountryId')
    campo_City = (By.ID, 'BillingNewAddress_City')
    campo_Address = (By.ID, 'BillingNewAddress_Address1')
    campo_Zip_postal = (By.ID, 'BillingNewAddress_ZipPostalCode')
    campo_Phone = (By.ID, 'BillingNewAddress_PhoneNumber')

    botao_continuar_Address = (By.CSS_SELECTOR, '[class="button-1 new-address-next-step-button"]')
    meio_pagamento = (By.CSS_SELECTOR, '[checked="checked"]')
    botao_continuar_Payment = (By.CSS_SELECTOR, '[class="button-1 payment-method-next-step-button"]')
    resumo = (By.XPATH, "//p[text()='You will pay by COD']")
    texto_resumo = 'You will pay by COD'
    botao_continuar_para_confirmar = (By.CSS_SELECTOR, '[class="button-1 payment-info-next-step-button"]')
    botao_confirmar = (By.CSS_SELECTOR, '[value="Confirm"]')
    mensagem_sucesso = (By.XPATH, "//strong[text()='Your order has been successfully processed!']")
    texto_mensagem = 'Your order has been successfully processed!'

    def __init__(self, driver):
        self.driver = driver

    def is_url_checkout_page(self):
        return self.is_url(self.url)

    def preencher_campo_first_name(self, nome):
        first_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_First_name)
        )

        first_name.send_keys(nome)

    def preencher_campo_last_name(self, sobrenome):
        last_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_Last_name)
        )

        last_name.send_keys(sobrenome)

    def preencher_campo_email(self, email):
        email_guest = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_Email)
        )

        email_guest.send_keys(email)

    def preencher_campo_country(self, pais):
        country = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_Country)
        )

        Select(country).select_by_visible_text(pais)

    def preencher_campo_city(self, cidade):
        city = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_City)
        )

        city.send_keys(cidade)

    def preencher_campo_address(self, endereco):
        address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_Address)
        )

        address.send_keys(endereco)

    def preencher_campo_postal(self, cep):
        zip_code = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_Zip_postal)
        )

        zip_code.send_keys(cep)

    def preencher_campo_phone(self, telefone):
        phone = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_Phone)
        )

        phone.send_keys(telefone)

    def clicar_no_botao_continuar_para_pagamento(self):
        continuar = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.botao_continuar_Address)
        )

        continuar.click()

    def verificar_meio_pagamento(self):
        pagamento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.meio_pagamento)
        )

        pagamento_marcado = pagamento.is_selected()

        return pagamento_marcado

    def clicar_no_botao_contunuar_para_resumo(self):
        confirmar_pagamento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.botao_continuar_Payment)
        )

        confirmar_pagamento.click()

    def verificar_resumo_produto(self):
        nome_produto = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.resumo)
        )

        verificar_nome_produto = nome_produto.text = self.texto_resumo

        return verificar_nome_produto

    def clicar_no_botao_continuar_para_confirmar(self):
        Continuar_confirmar_compra = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.botao_continuar_para_confirmar)
        )

        Continuar_confirmar_compra.click()

    def clicar_no_botao_confirmar(self):
        confirmar = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.botao_confirmar)
        )

        confirmar.click()

    def verificar_mensagem_de_sucesso(self):
        mensagem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.mensagem_sucesso)
        )

        visualizar_mensagem = mensagem.text = self.texto_mensagem

        return visualizar_mensagem
