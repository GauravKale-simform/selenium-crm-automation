from pageObjects.Login_Page import Login
from utilities.logger import logGen

logger = logGen.logger()

class TestLogin:
    def test_login_valid(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        logger.info("Starting valid login test")
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        logger.info("Entering Email")
        self.lp.enter_password('Royal@12345')
        logger.info("Entering Password")
        self.lp.click_login_button()
        logger.info("Clicking on login button")
        self.driver.implicitly_wait(10)
        if self.lp.page_title_displayed():
            print("Login successful")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//success.png")
            assert True
        else:
            print("Fail")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//fail.png")

    def test_login_invalid_email(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gaurav.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.driver.implicitly_wait(10)
        if self.lp.invalid_error_message():
            print("Login failed as expected due to invalid email")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//invalid_email_fail.png")
            assert True
        else:
            print("Unexpected success")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//invalid_email_unexpected.png")
            assert False

    def test_login_invalid_password(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('royal@abcd')
        self.lp.click_login_button()
        self.driver.implicitly_wait(10)
        if self.lp.invalid_error_message():
            print("Login failed as expected due to invalid email")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//invalid_password_fail.png")
            assert True
        else:
            print("Unexpected success")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//invalid_email_unexpected.png")
            assert False

    def test_login_invalid_email_password(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gaurav123.sinhgad@gmail.com')
        self.lp.enter_password('royal@abcd')
        self.lp.click_login_button()
        self.driver.implicitly_wait(10)
        if self.lp.invalid_error_message():
            print("Login failed as expected due to invalid email")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//invalid_email_password_fail.png")
            assert True
        else:
            print("Unexpected success")
            self.driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//invalid_email_unexpected.png")
            assert False