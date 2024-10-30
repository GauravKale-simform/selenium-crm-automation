import time
from pageObjects.Add_new_Contact import AddNewContact
from pageObjects.Login_Page import Login
from utilities.googlesheet import GoogleSheetReader


class TestNewContact:
    def test_add_contact(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        test004 = GoogleSheetReader('C://Users//gaurav//Desktop//Automation//CRM_Project//utilities//credentials.json','CRM_testdata', 'test004')
        contact_data = test004.get_all_records()
        if len(contact_data) < 1:
            raise ValueError("Not enough data in the Google Sheet. At least one row of data is needed.")

        row_data = contact_data[0]

        self.lp.enter_email(row_data['Registered Email'])
        self.lp.enter_password(row_data['Password'])
        self.lp.click_login_button()
        self.ANCT = AddNewContact(self.driver)
        self.ANCT.hover_and_click_add_new_contact()
        self.ANCT.enter_first_name(row_data['First Name'])
        self.ANCT.enter_last_name(row_data['Last Name'])
        self.ANCT.enter_middle_name(row_data['Middle Name'])
        self.ANCT.enter_company(row_data['Company'])
        self.ANCT.enter_tag(row_data['Tag'])
        self.ANCT.enter_email(row_data['Email'])
        self.ANCT.enter_type_email(row_data['Email Type'])
        self.ANCT.enter_category()
        self.ANCT.enter_status()
        self.ANCT.enter_description(row_data['Description'])
        self.ANCT.enter_social_channel()
        self.ANCT.scroll_down()
        self.ANCT.enter_sc_link(row_data['Social Link'])
        self.ANCT.enter_street_address(row_data['Street Address'])
        self.ANCT.enter_city_address(row_data['CITY'])
        self.ANCT.enter_state_address(row_data['State'])
        self.ANCT.enter_post_code(row_data['Postal Code'])
        self.ANCT.enter_country_address(row_data['Country'])
        self.ANCT.enter_phone_country(row_data['Phone Country'])
        self.ANCT.enter_phone_number(row_data['Phone Number'])
        self.ANCT.enter_phone_type(row_data['Phone Type'])
        self.ANCT.enter_position(row_data['POSITION'])
        self.ANCT.enter_department(row_data['Department'])
        self.ANCT.enter_supervisor(row_data['Supervisor'])
        self.ANCT.enter_assistant(row_data['ASSISTANCE'])
        self.ANCT.enter_referred_by(row_data['Referred By'])
        self.ANCT.enter_source()
        self.ANCT.toggle_do_not_call(state=True)
        self.ANCT.enter_birthday_day(row_data['Birthday Day'])
        self.ANCT.enter_birthday_month()
        self.ANCT.enter_birthday_year(row_data['Birthday Year'])
        self.ANCT.enter_identifier(row_data['Identifier'])
        self.ANCT.upload_image("C:/Users/gaurav/Downloads/indian_flag.png")
        self.ANCT.save_profile()
        time.sleep(5)
        self.ANCT.verify_contact_created()


# import time
# from pageObjects.Add_new_Contact import AddNewContact
# from pageObjects.Login_Page import Login
#
# class TestNewContact:
#     def test_add_contact(self,setup):
#         self.driver = setup
#         self.lp = Login(self.driver)
#         self.lp.enter_email('gauravkale.sinhgad@gmail.com')
#         self.lp.enter_password('Royal@12345')
#         self.lp.click_login_button()
#         self.ANCT = AddNewContact(self.driver)
#         self.ANCT.hover_and_click_add_new_contact()
#         self.ANCT.enter_first_name("Abhishek")
#         self.ANCT.enter_last_name("Sen")
#         self.ANCT.enter_middle_name("Radha")
#         self.ANCT.enter_company("NextPoint")
#         self.ANCT.enter_tag("Automation")
#         self.ANCT.enter_email("abhisheck.sen@fractal.com")
#         self.ANCT.enter_type_email("Business")
#         self.ANCT.enter_category()
#         self.ANCT.enter_status()
#         self.ANCT.enter_description("Senior executive with a focus on driving business growth and innovation at NextPoint.")
#         self.ANCT.enter_social_channel()
#         self.ANCT.scroll_down()
#         self.ANCT.enter_sc_link("https://www.linkedin.com/in/abhisheks")#
#         # self.ANCT.select_timezone('Asia/Kolkata')
#         self.ANCT.enter_street_address("1234 Business Avenue")
#         self.ANCT.enter_city_address("Pune")
#         self.ANCT.enter_state_address("Maharashtra")
#         self.ANCT.enter_post_code("411001")
#         self.ANCT.enter_country_address("India")
#         self.ANCT.enter_phone_country("India")
#         self.ANCT.enter_phone_number("9872305641")
#         self.ANCT.scroll_down()
#         self.ANCT.enter_phone_type("Work")
#         self.ANCT.enter_position("Senior Business Analyst")
#         self.ANCT.enter_department("Strategy & Planning")
#         self.ANCT.enter_supervisor("Sr Manager")
#         self.ANCT.enter_assistant("L2 Lead")
#         self.ANCT.scroll_down()
#         self.ANCT.enter_referred_by("Social Media")
#         self.ANCT.enter_source()
#         self.ANCT.toggle_do_not_call(state=True)
#         self.ANCT.enter_birthday_day("20")
#         self.ANCT.enter_birthday_month()
#         self.ANCT.enter_birthday_year("1998")
#         self.ANCT.enter_identifier("QA Engineer")
#         self.ANCT.upload_image("C:/Users/gaurav/Downloads/indian_flag.png")
#         self.ANCT.save_profile()
#         time.sleep(5)
#         self.ANCT.verify_contact_created()






