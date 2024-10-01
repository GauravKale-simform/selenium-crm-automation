from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddNewCompany:
    Hover_Companies_xpath = (By.XPATH,"//span[normalize-space()='Companies']")
    Create_Company_xpath = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/button[1]/i[1]")
    Phone_label_xpath =(By.XPATH,"//label[normalize-space()='Phone']")

    Name_xpath = (By.XPATH,"//div[@class='ui right corner labeled input']//input[@name='name']")

    WebSite_xpath = (By.XPATH,"//input[@name='url']")

    Address_Street_xpath = (By.XPATH,"//input[@placeholder='Street Address']")
    Address_City_xpath = (By.XPATH,"//input[@placeholder='City']")
    Address_State_xpath = (By.XPATH,"//input[@placeholder='State / County']")
    Address_Post_Code_xpath = (By.XPATH,"//input[@placeholder='Post Code']")
    Address_Country_xpath = (By.XPATH,"//div[@name='country']//input[@type='text']")
    Address_Country_India_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']")
    Address_Country_Australia_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Australia']")
    Address_Country_Brazil_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Brazil']")
    Address_Country_Canada_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Canada']")
    Address_Country_China_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='China']")
    Address_Country_Egypt_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Egypt']")

    Phone_Country_xpath = (By.XPATH,"//div[@name='hint']//input[@type='text']")
    Phone_India_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']")
    Phone_Australia_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Australia']")
    Phone_Brazil_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Brazil']")
    Phone_Canada_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Canada']")
    Phone_China_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='China']")
    Phone_Egypt_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Egypt']")
    Phone_Number_xpath = (By.XPATH,"//input[@placeholder='Number']")
    Type_of_Phone_Number_xpath = (By.XPATH,"//input[@placeholder='Home, Work, Mobile...']") #Home,work,mobile

    Email_xpath = (By.XPATH,"//input[@placeholder='Email address']")
    Type_of_Email_xpath = (By.XPATH,"//input[@placeholder='Personal email, Business, Alt...']") #Personal,business

    Tags_xpath = (By.XPATH,"//div[@class='ui active visible fluid multiple search selection dropdown']")
    Tag_Technology_xpath = (By.XPATH,"//span[normalize-space()='technology']")
    Tag_Software_development_xpath = (By.XPATH,"//span[normalize-space()='Software Development']")
    Tag_India_xpath = (By.XPATH,"//span[normalize-space()='India']")
    Tag_Automation_xpath = (By.XPATH,"//span[normalize-space()='Automation']")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    Social_Channel_xpath = (By.XPATH,"//div[@name='channel_type']")
    Twitter_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]")
    Facebook_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    LinkedIn_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[3]")
    TikTok_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[4]")
    Instagram_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[5]")
    Yelp_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[6]")
    Enter_Social_Channel_link = (By.XPATH,"//div[@class='ui field'][.//label[normalize-space()='Social channels']]//div[@class='ui input']//input[@name='value']")

    Industry_xpath = (By.XPATH,"//input[@name='industry']")

    No_of_Employees_xpath = (By.XPATH,"//input[@name='num_employees']")

    Stock_Symbol_xpath = (By.XPATH,"//input[@name='symbol']")

    Annual_Revenue_xpath = (By.XPATH,"//input[@name='annual_revenue']")

    Priority_xpath = (By.XPATH,"//body/div[@id='ui']/div[@class='ui fluid container']/div[@class='ui fluid container']/div[@id='main-content']/div[@class='ui fluid container ']/div[@class='ui fluid container main-content']/form[@class='ui form segment custom-form-container']/div[7]/div[2]/div[1]/div[1]")
    Priority_Low_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Priority_Medium_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[3]")
    Priority_High_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[4]")


    Status_xpath = (By.XPATH,"//div[@name='status']//i[@class='dropdown icon']")
    Status_New_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Status_Active_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[3]")
    Status_Inactive_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[4]")
    Status_On_Hold_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[5]")
    Status_Terminated_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[6]")
    Status_Hot_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[7]")

    Source_xpath = (By.XPATH,"//div[@name='source']//i[@class='dropdown icon']")
    Source_Ad_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Source_Referral_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[3]")
    Source_Customer_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[4]")
    Source_Partner_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[5]")
    Source_Event_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[6]")
    Source_Internet_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[7]")
    Source_Walk_in_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[8]")
    Source_Call_in_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[9]")
    Source_Email_Source_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[10]")
    Source_Web_service_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[11]")
    Source_Import_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[12]")

    Category_xpath = (By.XPATH,"//div[@name='category']//i[@class='dropdown icon']")
    Category_Client_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Category_Partner_Category_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[3]")
    Category_Prospect_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[4]")

    Vat_Number_xpath = (By.XPATH,"//input[@name='vat_number']")

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")

    Image_upload_xpath = (By.XPATH,"//input[@name='image']")
    file_path = "C:/Users/gaurav/Downloads/indian_flag.png"

    Save_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    Star_xpath = (By.XPATH,'//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_company(self):
        hover_on_companies_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewCompany.Hover_Companies_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_companies_element).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCompany.Create_Company_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCompany.Phone_label_xpath)).click()

    def enter_name(self,name):
        self.driver.find_element(*AddNewCompany.Name_xpath).send_keys(name)

    def enter_website(self,website):
        self.driver.find_element(*AddNewCompany.WebSite_xpath).send_keys(website)

    def enter_street_address(self,street):
        self.driver.find_element(*AddNewCompany.Address_Street_xpath).send_keys(street)

    def enter_city_address(self,city):
        self.driver.find_element(*AddNewCompany.Address_City_xpath).send_keys(city)

    def enter_state_address(self,state):
        self.driver.find_element(*AddNewCompany.Address_State_xpath).send_keys(state)

    def enter_post_code(self,postcode):
        self.driver.find_element(*AddNewCompany.Address_Post_Code_xpath).send_keys(postcode)

    def enter_country_address(self,country):
        self.driver.find_element(*AddNewCompany.Address_Country_xpath).send_keys(country)
        self.driver.find_element(*AddNewCompany.Address_Country_India_xpath).click()

    def enter_phone_country(self,country):
        self.driver.find_element(*AddNewCompany.Phone_Country_xpath).send_keys(country)
        self.driver.find_element(*AddNewCompany.Phone_India_xpath).click()

    def enter_phone_number(self,phonenum):
        self.driver.find_element(*AddNewCompany.Phone_Number_xpath).send_keys(phonenum)

    def enter_phone_type(self,phonetype):
        self.driver.find_element(*AddNewCompany.Type_of_Phone_Number_xpath).send_keys(phonetype)

    def enter_email(self,email):
        self.driver.find_element(*AddNewCompany.Email_xpath).send_keys(email)

    def enter_email_type(self,emailtype):
        self.driver.find_element(*AddNewCompany.Type_of_Email_xpath).send_keys(emailtype)

    def enter_tag(self, tag):
        self.driver.find_element(*AddNewCompany.Tags_xpath).send_keys(tag)
        # tag_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewCompany.Tags_xpath))
        # tag_input.send_keys(tag)
        tag_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCompany.Tag_Technology_xpath))
        tag_option.click()

    # def enter_tag(self,tag):
    #     self.driver.find_element(*AddNewCompany.Tags_xpath).send_keys(tag)
    #     self.driver.find_element(*AddNewCompany.Tag_Technology_xpath).click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewCompany.Description_xpath).send_keys(desc)

    def enter_social_channel(self):
        self.driver.find_element(*AddNewCompany.Social_Channel_xpath).click()
        self.driver.find_element(*AddNewCompany.LinkedIn_xpath).click()

    def enter_sc_link(self,scl):
        self.driver.find_element(*AddNewCompany.Enter_Social_Channel_link).send_keys(scl)

    def enter_industry(self,industry):
        self.driver.find_element(*AddNewCompany.Industry_xpath).send_keys(industry)

    def enter_no_employees(self,emp):
        self.driver.find_element(*AddNewCompany.No_of_Employees_xpath).send_keys(emp)

    def enter_stock_symbol(self,symbol):
        self.driver.find_element(*AddNewCompany.Stock_Symbol_xpath).send_keys(symbol)

    def enter_annual_revenue(self,revenue):
        self.driver.find_element(*AddNewCompany.Annual_Revenue_xpath).send_keys(revenue)

    def enter_priority(self):
        self.driver.find_element(*AddNewCompany.Priority_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        low_priority_element = wait.until(EC.element_to_be_clickable((AddNewCompany.Priority_Low_xpath)))
        low_priority_element.click()
        #self.driver.find_element(*AddNewCompany.Priority_Low_xpath)

    def enter_status(self):
        self.driver.find_element(*AddNewCompany.Status_xpath).click()
        self.driver.find_element(*AddNewCompany.Status_New_xpath).click()

    def enter_source(self):
        self.driver.find_element(*AddNewCompany.Source_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        internet_source_element = wait.until(EC.element_to_be_clickable((AddNewCompany.Source_Internet_xpath)))
        internet_source_element.click()
        #self.driver.find_element(*AddNewCompany.Source_Internet_xpath)

    def enter_category(self):
        self.driver.find_element(*AddNewCompany.Category_xpath).click()
        self.driver.find_element(*AddNewCompany.Category_Partner_Category_xpath).click()

    def enter_vat_number(self,vat):
        self.driver.find_element(*AddNewCompany.Vat_Number_xpath).send_keys(vat)

    def enter_identifier(self,idf):
        self.driver.find_element(*AddNewCompany.Identifier_xpath).send_keys(idf)

    def upload_image(self,file_path):
        wait = WebDriverWait(self.driver, 10)
        image_upload = wait.until(EC.presence_of_element_located(AddNewCompany.Image_upload_xpath))
        #image_upload = self.driver.find_element(*AddNewCompany.Image_upload_xpath)
        image_upload.send_keys(file_path)

    def save_profile(self):
        self.driver.find_element(*AddNewCompany.Save_xpath).click()
        WebDriverWait(self.driver, 10)

    def verify_company_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewCompany.Star_xpath)))
            print("Successfully created a new company.")
        except:
            print("Failed to create a new company.")
            assert False, "The page did not land on the expected location after saving."

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")










