from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ContactUsPage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    fillName = (By.ID, "FullName")
    fillEmail = (By.ID, "Email")
    fillEnquiry = (By.ID, "Enquiry")
    submitButton = (By.CSS_SELECTOR, "input.button-1.contact-us-button[type='submit']")
    successMessageContactUS = (By.CLASS_NAME, 'page-body')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_url_contactUs_page(self):
        return self.is_url(self.url)

    def contact_us_page(self, name, email, enquiry):
        self.driver.find_element(*self.fillName).click()
        self.driver.find_element(*self.fillName).send_keys(name)
        self.driver.find_element(*self.fillEmail).click()
        self.driver.find_element(*self.fillEmail).send_keys(email)
        self.driver.find_element(*self.fillEnquiry).click()
        self.driver.find_element(*self.fillEnquiry).send_keys(enquiry)
        self.driver.find_element(*self.submitButton).click()
        assert ContactUsPage.successMessageContactUS, 'Your enquiry has been successfully sent to the store owner.'


