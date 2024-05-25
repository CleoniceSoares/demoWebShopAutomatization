from faker import Faker

from pages.RegisterPage import RegisterPage

class Teste1:

    def test_registrar_usuario(self, setup):
        home_page = setup
        home_page.open_home_page()
        assert home_page.is_url_home_page(), 'URL da HomePage está incorreta!'

        register_page = RegisterPage(home_page.driver)
        register_page.clicar_link_register()
        assert register_page.is_url_register_page(), 'URL de Register está incorreta'
        assert register_page.titulo_pagina_register(), 'Titulo da pagina Register incorreto'

        fake = Faker()
        nome = fake.name()
        sobrenome = fake.last_name()
        email = fake.email()
        senha = fake.password()

        register_page.preencher_dados_pessoais(nome, sobrenome, email)
        register_page.preencher_dados_senha(senha, senha)
        register_page.clicar_botao_register()
        assert register_page.tem_messagem_sucesso(), 'Mensagem de sucesso nao encontrada'

        register_page.clicar_botao_continue()
        assert register_page.is_url_home_page(), 'URL da HomePage está incorreta!'



