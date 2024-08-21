import time
from pageObjects.Add_new_Company import AddNewCompany
from pageObjects.Login_Page import Login


class TestNewCompany:
    def test_add_company(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.ANC = AddNewCompany(self.driver)
        self.ANC.hover_and_click_add_new_company()
        self.ANC.enter_name("NextPoint")
        self.ANC.enter_website("http://www.nextpoint-solutions.com/")
        self.ANC.enter_street_address("123 Innovation Lane")
        self.ANC.enter_city_address("Pune")
        self.ANC.enter_state_address("Maharashtra")
        self.ANC.enter_post_code("411057")
        self.ANC.enter_country_address("India") #
        self.ANC.enter_phone_country("India")
        self.ANC.enter_phone_number("8888446392")
        self.ANC.enter_phone_type("Mobile")
        self.ANC.enter_email("info@nextpoint-tech.com")
        self.ANC.enter_email_type("Business")
        #self.ANCT.enter_tag("technology")#Technology,Software Development,India,Innovation
        self.ANC.enter_description("NextPoint delivers innovative software solutions and IT consulting services. Based in Maharashtra, we help businesses thrive with cutting-edge technology")
        self.ANC.enter_social_channel() #linkedin
        self.ANC.enter_sc_link("linkedin.com/company/nextpoint-tech")##
        self.ANC.scroll_down()
        self.ANC.enter_industry("Technology")
        self.ANC.enter_no_employees("500")
        self.ANC.enter_stock_symbol("NPT")
        self.ANC.enter_annual_revenue("2,075,000,000")
        self.ANC.enter_priority() #low
        self.ANC.enter_status() #new
        self.ANC.enter_source() #internet
        self.ANC.enter_category() #partner
        self.ANC.enter_vat_number("MH12345678901234")
        self.ANC.enter_identifier("NP-2024-001")
        self.ANC.upload_image("C:/Users/gaurav/Downloads/indian_flag.png")
        self.ANC.save_profile()
        time.sleep(20)
        self.ANC.verify_company_created()




