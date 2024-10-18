import time

from pageObjects.Add_new_Calls import AddNewCalls
from pageObjects.Login_Page import Login

class TestAddNewCalls:
    def test_add_new_call(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.ANC = AddNewCalls(self.driver)
        self.ANC.hover_and_click_add_new_deals()
        self.ANC.select_call_time()
        self.ANC.select_type()
        # self.ANC.enter_callscript('Hey need to attend this call')
        self.ANC.enter_duration('60')
        self.ANC.select_start_time()
        self.ANC.select_flag()
        self.ANC.enter_tag('business')
        self.ANC.enter_description('This is testing of description')
        self.ANC.scroll_down()
        self.ANC.enter_participants('Rajesh')
        self.ANC.enter_deal('Testing')
        self.ANC.enter_case('Case Testing')
        self.ANC.enter_task('Team meeting')
        self.ANC.select_country()
        self.ANC.enter_phone_number('7820062006')
        self.ANC.enter_type_phone('Work')
        self.ANC.enter_identifier('This is a testing of identifier')
        self.ANC.save_task()
        self.ANC.verify_new_deal_created()
        time.sleep(1000)






















