##################### Reading the data from the xlsheet stored locally #########################
#
# from pageObjects.Add_new_Company import AddNewCompany
# from pageObjects.Login_Page import Login
# from utilities.excel_reader import ExcelReader
#
# class TestNewCompany:
#     def test_add_company(self, setup):
#         self.driver = setup
#         self.lp = Login(self.driver)
#         row = 2
#         excel = ExcelReader('C://Users//gaurav//Desktop//Automation//CRM_Project//CRM_testdata.xlsx')
#         fields = [
#             ('email', 'Email'), ('password', 'Password'), ('company', 'Company'), ('website', 'Website'),
#             ('street', 'Street'), ('city', 'City'), ('state', 'State'), ('post', 'PostCode'),
#             ('country', 'Country'), ('phone_country', 'Ph-Country'), ('phone_number', 'Ph-Number'),
#             ('phone_type', 'Ph-Type'), ('email_type', 'Email-Type'), ('tag', 'Tag'),
#             ('description', 'Description'), ('social_channel', 'Social-Channel'), ('industry', 'Industry'),
#             ('no_employees', 'No-Employee'), ('stock_symbol', 'Stock-Symbol'), ('annual_revenue', 'Annual-Revenue'),
#             ('vat_number', 'Vat-Number'), ('identifier', 'Identifier')
#         ]
#         company_data = {key: excel.get_data("Sheet1", row, header) for key, header in fields}
#         self.lp.enter_email(company_data['email'])
#         self.lp.enter_password(company_data['password'])
#         self.lp.click_login_button()
#         self.ANC = AddNewCompany(self.driver)
#         self.ANC.hover_and_click_add_new_company()
#         self.ANC.enter_name(company_data['company'])
#         self.ANC.enter_website(company_data['website'])
#         self.ANC.enter_street_address(company_data['street'])
#         self.ANC.enter_city_address(company_data['city'])
#         self.ANC.enter_state_address(company_data['state'])
#         self.ANC.enter_post_code(company_data['post'])
#         self.ANC.enter_country_address(company_data['country'])
#         self.ANC.enter_phone_country(company_data['phone_country'])
#         self.ANC.enter_phone_number(company_data['phone_number'])
#         self.ANC.enter_phone_type(company_data['phone_type'])
#         self.ANC.enter_email(company_data['email'])
#         self.ANC.enter_email_type(company_data['email_type'])
#         self.ANC.enter_tag(company_data['tag'])
#         self.ANC.enter_description(company_data['description'])
#         self.ANC.enter_social_channel()
#         self.ANC.enter_sc_link(company_data['social_channel'])
#         self.ANC.scroll_down()
#         self.ANC.enter_industry(company_data['industry'])
#         self.ANC.enter_no_employees(company_data['no_employees'])
#         self.ANC.enter_stock_symbol(company_data['stock_symbol'])
#         self.ANC.enter_annual_revenue(company_data['annual_revenue'])
#         self.ANC.enter_priority()
#         self.ANC.enter_status()
#         self.ANC.enter_source()
#         self.ANC.enter_category()
#         self.ANC.enter_vat_number(company_data['vat_number'])
#         self.ANC.enter_identifier(company_data['identifier'])
#         self.ANC.save_profile()
#         self.ANC.verify_company_created()

######################### Reading the data from Google Sheet ##################################

from pageObjects.Add_new_Company import AddNewCompany
from pageObjects.Login_Page import Login
from utilities.googlesheet import GoogleSheetReader

class TestNewCompany:
    def test_add_company(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        test003 = GoogleSheetReader('C://Users//gaurav//Desktop//Automation//CRM_Project//utilities//credentials.json', 'CRM_testdata', 'test003')
        company_data = test003.get_all_records()
        if len(company_data) < 2:
            raise ValueError("Not enough data in the Google Sheet. At least one row of data is needed.")

        row_data = company_data[1]

        self.lp.enter_email(row_data['Email'])
        self.lp.enter_password(row_data['Password'])
        self.lp.click_login_button()
        self.ANC = AddNewCompany(self.driver)
        self.ANC.hover_and_click_add_new_company()
        self.ANC.enter_name(row_data['Company'])
        self.ANC.enter_website(row_data['Website'])
        self.ANC.enter_street_address(row_data['Street'])
        self.ANC.enter_city_address(row_data['City'])
        self.ANC.enter_state_address(row_data['State'])
        self.ANC.enter_post_code(row_data['PostCode'])
        self.ANC.enter_country_address(row_data['Country'])
        self.ANC.enter_phone_country(row_data['Country01'])
        self.ANC.enter_phone_number(row_data['Phone-Number'])
        self.ANC.enter_phone_type(row_data['Phone-Type'])
        self.ANC.enter_email(row_data['Email01'])
        self.ANC.enter_email_type(row_data['Type'])
        self.ANC.enter_tag(row_data['Tag'])
        self.ANC.enter_description(row_data['Description'])
        self.ANC.enter_social_channel()
        self.ANC.enter_sc_link(row_data['Social-Channel'])
        self.ANC.scroll_down()
        self.ANC.enter_industry(row_data['Industry'])
        self.ANC.enter_no_employees(row_data['No-Employee'])
        self.ANC.enter_stock_symbol(row_data['Stock-Symbol'])
        self.ANC.enter_annual_revenue(row_data['Annual-Revenue'])
        self.ANC.enter_priority()
        self.ANC.enter_status()
        self.ANC.enter_source()
        self.ANC.enter_category()
        self.ANC.enter_vat_number(row_data['Vat-Number'])
        self.ANC.enter_identifier(row_data['Identifier'])
        self.ANC.upload_image("C:/Users/gaurav/Downloads/indian_flag.png")
        self.ANC.save_profile()
        self.ANC.verify_company_created()


# from pageObjects.Add_new_Company import AddNewCompany
# from pageObjects.Login_Page import Login
# class TestNewCompany:
#     def test_add_company(self,setup):
#         self.driver = setup
#         self.lp = Login(self.driver)
#         self.lp.enter_email('gauravkale.sinhgad@gmail.com')
#         self.lp.enter_password('Royal@12345')
#         self.lp.click_login_button()
#         self.ANC = AddNewCompany(self.driver)
#         self.ANC.hover_and_click_add_new_company()
#         self.ANC.enter_name("NextPoint")
#         self.ANC.enter_website("http://www.nextpoint-solutions.com/")
#         self.ANC.enter_street_address("123 Innovation Lane")
#         self.ANC.enter_city_address("Pune")
#         self.ANC.enter_state_address("Maharashtra")
#         self.ANC.enter_post_code("411057")
#         self.ANC.enter_country_address("India")
#         self.ANC.enter_phone_country("India")
#         self.ANC.enter_phone_number("8888446392")
#         self.ANC.enter_phone_type("Mobile")
#         self.ANC.enter_email("info@nextpoint-tech.com")
#         self.ANC.enter_email_type("Business")
#         self.ANC.enter_tag("technology") #Technology,Software Development,India,Innovation
#         self.ANC.enter_description("NextPoint delivers innovative software solutions and IT consulting services. Based in Maharashtra, we help businesses thrive with cutting-edge technology")
#         self.ANC.enter_social_channel() #linkedin
#         self.ANC.enter_sc_link("linkedin.com/company/nextpoint-tech")##
#         self.ANC.scroll_down()
#         self.ANC.enter_industry("Technology")
#         self.ANC.enter_no_employees("500")
#         self.ANC.enter_stock_symbol("NPT")
#         self.ANC.enter_annual_revenue("2,075,000,000")
#         self.ANC.enter_priority() #low
#         self.ANC.enter_status() #new
#         self.ANC.enter_source() #internet
#         self.ANC.enter_category() #partner
#         self.ANC.enter_vat_number("MH12345678901234")
#         self.ANC.enter_identifier("NP-2024-001")
#         self.ANC.upload_image("C:/Users/gaurav/Downloads/indian_flag.png")
#         self.ANC.save_profile()
#         self.ANC.verify_company_created()

