from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Login:
    Email_xpath = (By.XPATH,"//input[@placeholder='Email']")
    Password_xpath = (By.XPATH,"//input[@placeholder='Password']")
    Login_Button_xpath = (By.XPATH,"//div[@class='ui fluid large blue submit button']")
    Cogmento_xpath = (By.XPATH,"//div[@class='header item']")
    Error_message = (By.XPATH,"//div[@class='header']")

    def __init__(self,driver):
        self.driver = driver

    def enter_email(self,email):
        self.driver.find_element(*Login.Email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*Login.Password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Login.Login_Button_xpath).click()

    def page_title_displayed(self):
        try:
            self.driver.find_element(*Login.Cogmento_xpath).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def invalid_error_message(self):
        try:
            self.driver.find_element(*Login.Error_message).is_displayed()
            return True
        except NoSuchElementException:
            return False

