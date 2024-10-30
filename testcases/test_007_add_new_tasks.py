import time

from pageObjects.Add_New_Tasks import AddNewTask
from pageObjects.Login_Page import Login


class TestAddNewTask ():
    def test_add_new_task(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.ANT = AddNewTask(self.driver)
        self.ANT.hover_and_click_add_new_tasks()
        self.ANT.enter_title('Testing Task - 01')
        self.ANT.select_assigned_to()
        self.ANT.select_type()
        self.ANT.deu_date()
        self.ANT.enter_contact('Abhishek Radha Sen')
        self.ANT.enter_company('Testing Your Source')
        self.ANT.enter_deal('Deal - Inactive')
        self.ANT.enter_case('Case Testing - 1')
        self.ANT.close_date()
        self.ANT.enter_tags('technology')
        self.ANT.enter_description('This is nothing but the testing of description')
        self.ANT.enter_completion('75')
        self.ANT.select_priority()
        self.ANT.select_status()
        self.ANT.enter_identifier('This is testing of identifier')
        self.ANT.save_task()
        self.ANT.verify_new_deal_created()
        time.sleep(2)

