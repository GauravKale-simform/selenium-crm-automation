import time
from pageObjects.Add_new_Deals import AddNewDeals
from pageObjects.Login_Page import Login


class TestAddNewDeals ():
    def test_add_new_deals(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.AND = AddNewDeals(self.driver)
        self.AND.hover_and_click_add_new_deals()
        self.AND.enter_title('We are creating a new deal')
        self.AND.select_assigned_to()
        self.AND.select_company('NextPoint')
        self.AND.enter_products('Product A')
        self.AND.enter_contact('Rajesh Kumar')
        self.AND.select_close_date()
        self.AND.select_tag('business')
        self.AND.enter_description('This is the testing of description entering into the deal')
        self.AND.enter_probability('65')
        self.AND.scroll_down()
        self.AND.enter_amount('15000')
        self.AND.enter_commission('3500')
        self.AND.select_stage()
        self.AND.select_status()
        self.AND.enter_next_step('This is testing of next step in deal')
        self.AND.select_type()
        self.AND.select_source()
        self.AND.enter_identifier('This is testing of identifier')
        self.AND.save_deal()
        self.AND.verify_new_deal_created()
        time.sleep(2)




