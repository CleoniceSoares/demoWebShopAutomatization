from selenium import webdriver

class PageObject:

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')

    def is_url(self, url):
        return self.driver.current_url == url

    def clicar_menu(self, by, menu):
        self.driver.find_element(by, menu).click()

    def close(self):
        self.driver.quit()
