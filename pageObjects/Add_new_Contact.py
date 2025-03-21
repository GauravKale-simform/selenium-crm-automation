from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewContact:
    Hover_Contacts_xpath = (By.XPATH,"//div[@class='menu-item-wrapper'][3]")
    Create_Contacts_xpath = (By.XPATH,"// div[ @ id = 'main-nav'] // div[3] // button[1] // i[1]")

    Email_Label_xpath = (By.XPATH,"//label[normalize-space()='Email']")

    First_Name_xpath = (By.XPATH,"//input[@name='first_name']")
    Last_Name_xpath = (By.XPATH,"//input[@name='last_name']")
    Middle_Name_xpath = (By.XPATH,"//input[@name='middle_name']")

    Company_xpath = (By.XPATH,"//div[@name='company']//input[@type='text']")
    Select_Company_xpath = (By.XPATH,"//span[normalize-space()='NextPoint']")

    Tag_xpath = (By.XPATH,"//div[@class='ui fluid multiple search selection dropdown']//input[@type='text']")
    Select_Tag_xpath = (By.XPATH,"//span[@class='text'][normalize-space()='Automation']")

    Email_xpath = (By.XPATH,"//input[@placeholder='Email address']")
    Type_of_Email = (By.XPATH,"//input[@placeholder='Personal email, Business, Alt...']")

    Category_xpath = (By.XPATH,"//div[@name='category']//i[@class='dropdown icon']")
    Category_Lead_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Category_Customer_xpath = (By.XPATH,"//div[@name='category']//div[3]")
    Category_Contact_xpath = (By.XPATH,"//div[@name='category']//div[4]")
    Category_Affiliate_xpath = (By.XPATH,"//div[@name='category']//div[5]")

    Status_xpath = (By.XPATH,"//div[@name='status']//i[@class='dropdown icon']")
    Status_New_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Status_Active_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[3]")
    Status_Inactive_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[4]")
    Status_On_Hold_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[5]")
    Status_Terminated_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[6]")
    Status_Hot_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[7]")

    Description_xpath = (By.XPATH, "//textarea[@name='description']")

    Social_Channel_xpath = (By.XPATH,"//div[@name='channel_type']")
    Social_Twitter_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]")
    Social_Facebook_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Social_LinkedIn_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[3]")
    Social_TikTok_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[4]")
    Social_Instagram_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[5]")
    Social_Yelp_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[6]")
    Enter_Social_Channel_link = (By.XPATH,"//div[@class='ui field'][.//label[normalize-space()='Social channels']]//div[@class='ui input']//input[@name='value']")

    Time_Zone_xpath = (By.XPATH,"//div[@name='timezone']//input[@type='text']")
    Time_ZoneKolkata_xpath = (By.XPATH, "//span[normalize-space()='Asia/Kolkata']")

    Address_Street_xpath = (By.XPATH, "//input[@placeholder='Street Address']")
    Address_City_xpath = (By.XPATH, "//input[@placeholder='City']")
    Address_State_xpath = (By.XPATH, "//input[@placeholder='State / County']")
    Address_Post_Code_xpath = (By.XPATH,"//input[@placeholder='Post Code']")
    Address_Country_xpath = (By.XPATH, "//div[@name='country']//input[@type='text']")
    Address_Country_India_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']")
    Address_Country_Australia_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Australia']")
    Address_Country_Brazil_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Brazil']")
    Address_Country_Canada_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Canada']")
    Address_Country_China_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='China']")
    Address_Country_Egypt_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Egypt']")

    Phone_Country_xpath = (By.XPATH,"//div[@name='hint']//input[@type='text']")
    Phone_Country_India_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']")
    Phone_Country_Australia_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Australia']")
    Phone_Country_Brazil_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Brazil']")
    Phone_Country_Canada_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Canada']")
    Phone_Country_China_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='China']")
    Phone_Country_Egypt_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='Egypt']")
    Phone_Number_xpath = (By.XPATH,"//input[@placeholder='Number']")
    Type_of_Phone_Number_xpath = (By.XPATH,"//input[@placeholder='Home, Work, Mobile...']") #Home,work,mobile

    Position_xpath = (By.XPATH,"//input[@name='position']")
    Department_xpath = (By.XPATH,"//input[@name='department']")

    Supervisor_xpath = (By.XPATH,"//div[@name='supervisor']//input[@type='text']")
    Select_Supervison_xpath = (By.XPATH,"//span[normalize-space()='Sr Manager']")

    Assistant_xpath = (By.XPATH,"//div[@name='assistant']//input[@type='text']")
    Select_Assistance_xpath = (By.XPATH,"//span[normalize-space()='L2 Lead']")

    Referred_by_xpath = (By.XPATH,"//div[@name='referred_by']//input[@type='text']")
    Select_Referred_by_xpath = (By.XPATH,"//span[normalize-space()='Social Media']")

    Source_xpath = (By.XPATH,"//div[@name='source']//i[@class='dropdown icon']")
    Source_Website_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Source_Google_xpath = (By.XPATH,"//div[@name='source']//div[3]")
    Source_Referral_xpath = (By.XPATH,"//div[@name='source']//div[4]")
    Source_Facebook_xpath = (By.XPATH,"//div[@name='source']//div[5]")
    Source_Repeat_Customer_xpath = (By.XPATH,"//div[@name='source']//div[6]")

    Do_not_Call_Toggle_button = (By.XPATH,"//div[@class='ui toggle checkbox']//label[contains(text(),'Do not Call')]")
    Do_not_Text_Toggle_button = (By.XPATH, "//div[@class='ui toggle checkbox']//label[contains(text(),'Do not Text')]")
    Do_not_Email_Toggle_button = (By.XPATH, "//div[@class='ui toggle checkbox']//label[contains(text(),'Do not Email')]")

    Birthday_day_xpath = (By.XPATH,"//input[@placeholder='Day']")
    Birthday_month_xpath = (By.XPATH,"//div[normalize-space()='Month']")
    Jan_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Feb_xpath = (By.XPATH,"//div[@name='month']//div[3]")
    Mar_xpath = (By.XPATH,"//div[@name='month']//div[4]")
    Apr_xpath = (By.XPATH,"//div[@name='month']//div[5]")
    May_xpath = (By.XPATH,"//div[@name='month']//div[6]")
    Jun_xpath = (By.XPATH,"//div[@name='month']//div[7]")
    Jul_xpath = (By.XPATH,"//div[@name='month']//div[8]")
    Aug_xpath = (By.XPATH,"//div[@name='month']//div[9]")
    Sep_xpath = (By.XPATH,"//div[@name='month']//div[10]")
    Oct_xpath = (By.XPATH,"//div[@name='month']//div[11]")
    Nov_xpath = (By.XPATH,"//div[@name='month']//div[12]")
    Dec_xpath = (By.XPATH,"//div[@name='month']//div[13]")
    Birthday_year_xpath = (By.XPATH,"//input[@placeholder='Year']")

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")

    Image_upload_xpath = (By.XPATH,"//input[@name='image']")
    file_path = "C:/Users/gaurav/Downloads/indian_flag.png"

    Save_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    Star_xpath = (By.XPATH,'//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_contact(self):
        hover_on_contact_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewContact.Hover_Contacts_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_contact_element).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewContact.Create_Contacts_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewContact.Email_Label_xpath)).click()

    def enter_first_name(self,fname):
        self.driver.find_element(*AddNewContact.First_Name_xpath).send_keys(fname)

    def enter_last_name(self,lname):
        self.driver.find_element(*AddNewContact.Last_Name_xpath).send_keys(lname)

    def enter_middle_name(self,mname):
        self.driver.find_element(*AddNewContact.Middle_Name_xpath).send_keys(mname)

    def enter_company(self,com):
        self.driver.find_element(*AddNewContact.Company_xpath).send_keys(com)
        company = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewContact.Select_Company_xpath))
        company.click()

    def enter_tag(self, tag):
        self.driver.find_element(*AddNewContact.Tag_xpath).send_keys(tag)
        tag_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewContact.Select_Tag_xpath))
        tag_option.click()

    def enter_email(self,email):
        self.driver.find_element(*AddNewContact.Email_xpath).send_keys(email)

    def enter_type_email(self,type):
        self.driver.find_element(*AddNewContact.Type_of_Email).send_keys(type)

    def enter_category(self):
        self.driver.find_element(*AddNewContact.Category_xpath).click()
        self.driver.find_element(*AddNewContact.Category_Customer_xpath).click()

    def enter_status(self):
        self.driver.find_element(*AddNewContact.Status_xpath).click()
        self.driver.find_element(*AddNewContact.Status_Active_xpath).click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewContact.Description_xpath).send_keys(desc)

    def enter_social_channel(self):
        self.driver.find_element(*AddNewContact.Social_Channel_xpath).click()
        self.driver.find_element(*AddNewContact.Social_LinkedIn_xpath).click()

    def enter_sc_link(self,scl):
        self.driver.find_element(*AddNewContact.Enter_Social_Channel_link).send_keys(scl)

    def select_timezone(self,timezone):
        self.driver.find_element(*AddNewContact.Time_Zone_xpath).send_keys(timezone)
        kolkata_option = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(AddNewContact.Time_ZoneKolkata_xpath))
        kolkata_option.click()
    def enter_street_address(self,street):
        self.driver.find_element(*AddNewContact.Address_Street_xpath).send_keys(street)

    def enter_city_address(self,city):
        self.driver.find_element(*AddNewContact.Address_City_xpath).send_keys(city)

    def enter_state_address(self,state):
        self.driver.find_element(*AddNewContact.Address_State_xpath).send_keys(state)

    def enter_post_code(self,postcode):
        self.driver.find_element(*AddNewContact.Address_Post_Code_xpath).send_keys(postcode)

    def enter_country_address(self,country):
        self.driver.find_element(*AddNewContact.Address_Country_xpath).send_keys(country)
        self.driver.find_element(*AddNewContact.Address_Country_India_xpath).click()

    def enter_phone_country(self,country):
        self.driver.find_element(*AddNewContact.Phone_Country_xpath).send_keys(country)
        self.driver.find_element(*AddNewContact.Phone_Country_India_xpath).click()

    def enter_phone_number(self,phonenum):
        self.driver.find_element(*AddNewContact.Phone_Number_xpath).send_keys(phonenum)

    def enter_phone_type(self,phonetype):
        self.driver.find_element(*AddNewContact.Type_of_Phone_Number_xpath).send_keys(phonetype)

    def enter_position(self,pos):
        self.driver.find_element(*AddNewContact.Position_xpath).send_keys(pos)

    def enter_department(self,dept):
        self.driver.find_element(*AddNewContact.Department_xpath).send_keys(dept)

    def enter_supervisor(self,spv):
        self.driver.find_element(*AddNewContact.Supervisor_xpath).send_keys(spv)
        manager_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(AddNewContact.Select_Supervison_xpath))
        manager_option.click()
        #self.driver.find_element(*AddNewContact.Supervisor_Manager_xpath).click()

    def enter_assistant(self,ast):
        self.driver.find_element(*AddNewContact.Assistant_xpath).send_keys(ast)
        support_staff_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewContact.Select_Assistance_xpath))
        support_staff_option.click()
        #self.driver.find_element(*AddNewContact.Assistant_Support_staff_xpath).click()

    def enter_referred_by(self,ref):
        self.driver.find_element(*AddNewContact.Referred_by_xpath).send_keys(ref)
        friend_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewContact.Select_Referred_by_xpath))
        friend_option.click()
        #self.driver.find_element(*AddNewContact.Referred_by_Friend_xpath).click()

    def enter_source(self):
        self.driver.find_element(*AddNewContact.Source_xpath).click()
        self.driver.find_element(*AddNewContact.Source_Website_xpath).click()

    def toggle_do_not_call(self, state=True):
        toggle_button_call = self.driver.find_element(*AddNewContact.Do_not_Call_Toggle_button)
        is_toggled_on = toggle_button_call.is_selected()
        if is_toggled_on != state:
            toggle_button_call.click()

    def toggle_do_not_text(self, state=True):
        toggle_button_text = self.driver.find_element(*AddNewContact.Do_not_Text_Toggle_button)
        is_toggled_on = toggle_button_text.is_selected()
        if is_toggled_on != state:
            toggle_button_text.click()

    def toggle_do_not_email(self, state=True):
        toggle_button_email = self.driver.find_element(*AddNewContact.Do_not_Email_Toggle_button)
        is_toggled_on = toggle_button_email.is_selected()
        if is_toggled_on != state:
            toggle_button_email.click()

    def enter_birthday_day(self,day):
        self.driver.find_element(*AddNewContact.Birthday_day_xpath).send_keys(day)

    def enter_birthday_month(self):
        self.driver.find_element(*AddNewContact.Birthday_month_xpath).click()
        self.driver.find_element(*AddNewContact.Jul_xpath).click()

    def enter_birthday_year(self,year):
        self.driver.find_element(*AddNewContact.Birthday_year_xpath).send_keys(year)

    def enter_identifier(self,idt):
        self.driver.find_element(*AddNewContact.Identifier_xpath).send_keys(idt)

    def upload_image(self,file_path):
        wait = WebDriverWait(self.driver, 10)
        image_upload = wait.until(EC.presence_of_element_located(AddNewContact.Image_upload_xpath))
        image_upload.send_keys(file_path)

    def save_profile(self):
        self.driver.find_element(*AddNewContact.Save_xpath).click()
        WebDriverWait(self.driver, 10)

    def verify_contact_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewContact.Star_xpath)))
            print("Successfully created a new contact.")
        except:
            print("Failed to create a new contact.")
            assert False


    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 100);")




















