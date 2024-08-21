import time
from pageObjects.Add_new_Contact import AddNewContact
from pageObjects.Login_Page import Login

class TestNewContact:
    def test_add_contact(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.ANCT = AddNewContact(self.driver)
        self.ANCT.hover_and_click_add_new_contact()
        self.ANCT.enter_first_name("Rajesh")
        self.ANCT.enter_last_name("Deshmukh")
        self.ANCT.enter_middle_name("Kumar")
        self.ANCT.enter_company("NextPoint")
        self.ANCT.enter_email("rajesh.deshmukh@nextpoint.com")
        self.ANCT.enter_type_email("Business")
        self.ANCT.enter_category()
        self.ANCT.enter_status()
        self.ANCT.enter_description("Senior executive with a focus on driving business growth and innovation at NextPoint.")
        self.ANCT.enter_social_channel()
        self.ANCT.scroll_down()
        self.ANCT.enter_sc_link("https://www.linkedin.com/in/rajesh-deshmukh-nextpoint")#
        #self.ANCT.enter_timezone()
        self.ANCT.enter_street_address("1234 Business Avenue")
        self.ANCT.enter_city_address("Pune")
        self.ANCT.enter_state_address("Maharashtra")
        self.ANCT.enter_post_code("411001")
        self.ANCT.enter_country_address("India")
        self.ANCT.enter_phone_country("India")
        self.ANCT.enter_phone_number("9872305641")
        self.ANCT.scroll_down()
        self.ANCT.enter_phone_type("Work")
        self.ANCT.enter_position("Senior Business Analyst")
        self.ANCT.enter_department("Strategy & Planning")
        self.ANCT.enter_supervisor("HR Manager")
        self.ANCT.enter_assistant("Support Staff")
        self.ANCT.scroll_down()
        self.ANCT.enter_referred_by("Friend")
        self.ANCT.enter_source()


