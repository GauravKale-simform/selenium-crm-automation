from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewDeals:
    Hover_Deals_xpath = (By.XPATH,"//span[normalize-space()='Deals']")
    Create_Deals_xpath = (By.XPATH,"//div[@id='main-nav']//div[5]//button[1]//i[1]")
    Contacts_label_xpath = (By.XPATH,"//label[normalize-space()='Contacts']")

    Title_xpath = (By.XPATH,"//input[contains(@name,'title')]")

    Assigned_to_xpath = (By.XPATH,"//div[@class='ui fluid selection dropdown']")
    Select_Assigned_xpath = (By.XPATH,"(//span[@class='text'][normalize-space()='Guarav Kale'])[2]")

    Company_xpath = (By.XPATH,"//div[@name='company']//input[@type='text']")
    Select_Company_xpath = (By.XPATH,"//div[@name='company']//div[@role='listbox']//div[2]") #Next Point

    Products_xpath = (By.XPATH,"//div[@name='products']//input[@type='text']")
    Select_Products_xpath = (By.XPATH,"//div[@name='products']//div[2]") # Product C

    Contacts_xpath = (By.XPATH,"//div[@name='contacts']//input[@type='text']")
    Select_Contacts_xpath = (By.XPATH,"//span[@class='text'][contains(text(),'Sean')]") #Sean Paul

    Close_Date_xpath = (By.XPATH,"//input[@class='calendarField']")
    Select_Close_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Thursday, 17 October 2024']")
    Select_Close_Time_xpath = (By.XPATH,"//li[normalize-space()='18:00']")

    Tag_xpath = (By.XPATH,"(//input[@class='search'])[4]")
    Select_Tag_xpath = (By.XPATH,"//span[normalize-space()='technology']")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    Probability_xpath = (By.XPATH,"//input[@name='probability']")

    Amount_xpath = (By.XPATH,"//input[@name='amount']")

    Commission_xpath = (By.XPATH,"//input[@name='commission']")

    Stage_xpath = (By.XPATH,"(//div[@name='stage'])[1]")
    Select_Stage_xpath = (By.XPATH,"//div[@name='stage']//div[5]") #Quote

    Status_xpath = (By.XPATH,"//div[normalize-space()='Select']")
    Select_Status_xpath = (By.XPATH,"//div[@name='status']//div[3]")

    Next_Steps_xpath = (By.XPATH,"//textarea[@name='next_step']")

    Type_xpath = (By.XPATH,"//div[@name='type']//div[@role='alert'][normalize-space()='Select']")
    Select_Type_xpath = (By.XPATH,"//span[normalize-space()='Opportunity']")

    Source_xpath = (By.XPATH,"//div[@name='source']//div[@role='alert'][normalize-space()='Select']")
    Select_Source_xpath = (By.XPATH,"//div[@name='source']//div[5]")

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")

    Save_Button_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    Star_xpath = (By.XPATH, '//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    Closed_Button = (By.XPATH,"//div[@class='ui toggle checkbox']")

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_deals(self):
        hover_on_add_deals = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewDeals.Hover_Deals_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_add_deals).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewDeals.Create_Deals_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewDeals.Contacts_label_xpath)).click()

    def enter_title(self,title):
        self.driver.find_element(*AddNewDeals.Title_xpath).send_keys("Testing Deal 1")

    def select_assigned_to(self):
        self.driver.find_element(*AddNewDeals.Assigned_to_xpath).click()
        select_assigned_to = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Assigned_xpath))
        select_assigned_to.click()

    def select_company(self,company):
        self.driver.find_element(*AddNewDeals.Company_xpath).send_keys(company)
        select_company = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Company_xpath))
        select_company.click()

    def enter_products(self,product):
        self.driver.find_element(*AddNewDeals.Products_xpath).send_keys(product)
        select_product = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Products_xpath))
        select_product.click()

    def enter_contact(self,contact):
        self.driver.find_element(*AddNewDeals.Contacts_xpath).send_keys(contact)
        select_contact = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Contacts_xpath))
        select_contact.click()

    def select_close_date(self):
        self.driver.find_element(*AddNewDeals.Close_Date_xpath).click()
        self.driver.find_element(*AddNewDeals.Select_Close_Date_xpath).click()
        self.driver.find_element(*AddNewDeals.Select_Close_Time_xpath).click()

    def select_tag(self,tag):
        self.driver.find_element(*AddNewDeals.Tag_xpath).send_keys(tag)
        select_tag = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Tag_xpath))
        select_tag.click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewDeals.Description_xpath).send_keys(desc)

    def enter_probability(self,prob):
        self.driver.find_element(*AddNewDeals.Probability_xpath).send_keys(prob)

    def enter_amount(self,amt):
        self.driver.find_element(*AddNewDeals.Amount_xpath).send_keys(amt)

    def enter_commission(self,commi):
        self.driver.find_element(*AddNewDeals.Commission_xpath).send_keys(commi)

    def select_stage(self):
        self.driver.find_element(*AddNewDeals.Stage_xpath).click()
        select_stage = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Stage_xpath))
        select_stage.click()

    def select_status(self):
        self.driver.find_element(*AddNewDeals.Status_xpath).click()
        select_status = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Status_xpath))
        select_status.click()

    def enter_next_step(self,ens):
        self.driver.find_element(*AddNewDeals.Next_Steps_xpath).send_keys(ens)

    def select_type(self):
        self.driver.find_element(*AddNewDeals.Type_xpath).click()
        select_type = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Type_xpath))
        select_type.click()

    def select_source(self):
        self.driver.find_element(*AddNewDeals.Source_xpath).click()
        select_source = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDeals.Select_Source_xpath))
        select_source.click()

    def enter_identifier(self,idef):
        self.driver.find_element(*AddNewDeals.Identifier_xpath).send_keys(idef)

    def closed_button_click(self):
        self.driver.find_element(*AddNewDeals.Closed_Button).click()

    def save_deal(self):
        self.driver.find_element(*AddNewDeals.Save_Button_xpath).click()

    def verify_new_deal_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewDeals.Star_xpath)))
            print("Successfully created a new deal.")
        except:
            print("Failed to create a new contact.")
            assert False

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 100);")


