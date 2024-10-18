import time

from pageObjects.Add_new_Cases import AddNewCases
from pageObjects.Login_Page import Login


class TestAddNewTask ():
    def test_add_new_task(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.ANC = AddNewCases(self.driver)
        self.ANC.hover_and_click_add_new_tasks()
        self.ANC.enter_title('Testing Cases - 01')
        self.ANC.select_assigned_to()
        self.ANC.enter_contact('Rajesh Kumar Deshmukh')
        self.ANC.enter_company('Next')
        self.ANC.enter_deal('Testing Deal 02')
        self.ANC.select_type()
        self.ANC.select_deadline()
        self.ANC.select_close_date()
        self.ANC.enter_tag('business')
        self.ANC.enter_description('This is nothing but the testing of description')
        self.ANC.select_priority()
        self.ANC.select_status()
        self.ANC.enter_identifier('This is testing of identifier')
        self.ANC.save_task()
        self.ANC.verify_new_deal_created()
        time.sleep(2)

