from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewCases:
    Hover_Cases_xpath = (By.XPATH,"//div[@class='menu-item-wrapper'][6]")
    Create_Cases_xpath = (By.XPATH,"//div[@id='main-nav']//div[7]//button[1]//i[1]")
    Contact_label_xpath = (By.XPATH,"//label[normalize-space()='Contact']")

    Title_xpath = (By.XPATH, "//input[contains(@name,'title')]")

    Assigned_to_xpath = (By.XPATH,"//div[@class='ui fluid selection dropdown']")
    Select_Assigned_xpath = (By.XPATH,"(//span[@class='text'][normalize-space()='Guarav Kale'])[2]")

    Contact_xpath = (By.XPATH,"(//input[@class='search'])[1]")
    Select_Contact_xpath = (By.XPATH,"//span[normalize-space()='Rajesh Kumar']") #Rajesh Kumar Deshmukh

    Company_xpath = (By.XPATH, "//div[@name='company']//input[@type='text']")
    Select_Company_xpath = (By.XPATH, "//div[@name='company']//div[@role='listbox']//div[2]")

    Deal_xpath = (By.XPATH, "(//input[@class='search'])[3]")
    Select_Deal_xpath = (By.XPATH, "//span[contains(text(),'Deal - Inactive')]")

    Type_xpath = (By.XPATH, "(//div[@name='type'])[1]")
    Select_Type_xpath = (By.XPATH, "//span[normalize-space()='Business Support']")

    Deadline_xpath = (By.XPATH,"(//input[@class='calendarField'])[1]")
    Select_Deadline_xpath = (By.XPATH,"//div[@aria-label='Choose Monday, 21 October 2024']")
    Select_Deadline_time_xpath = (By.XPATH,"//li[normalize-space()='18:00']")

    Close_Date_xpath = (By.XPATH,"(//input[@class='calendarField'])[2]")
    Select_Close_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Tuesday, 22 October 2024']")
    Select_Close_Time_xpath = (By.XPATH,"//li[normalize-space()='18:00']")

    Tag_xpath = (By.XPATH, "(//input[@class='search'])[4]")
    Select_Tag_xpath = (By.XPATH, "(//span[normalize-space()='business'])[2]")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    Priority_xpath = (By.XPATH, "(//div[@name='priority'])[1]")
    Select_Priority_xpath = (By.XPATH, "//span[normalize-space()='Normal']")

    Status_xpath = (By.XPATH,"(//div[@name='status'])[1]")
    Select_Status_xpath = (By.XPATH,"//span[contains(text(),'Reviewing')]")

    Identifier_xpath = (By.XPATH, "//input[@name='identifier']")

    Save_Button_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    Star_xpath = (By.XPATH, '//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_tasks(self):
        hover_on_add_cases = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewCases.Hover_Cases_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_add_cases).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCases.Create_Cases_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCases.Contact_label_xpath)).click()

    def enter_title(self,title):
        self.driver.find_element(*AddNewCases.Title_xpath).send_keys(title)

    def select_assigned_to(self):
        self.driver.find_element(*AddNewCases.Assigned_to_xpath).click()
        select_assigned = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Assigned_xpath))
        select_assigned.click()

    def enter_contact(self,contact):
        self.driver.find_element(*AddNewCases.Contact_xpath).send_keys(contact)
        select_contact = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Contact_xpath))
        select_contact.click()

    def enter_company(self,company):
        self.driver.find_element(*AddNewCases.Company_xpath).send_keys(company)
        select_company = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Company_xpath))
        select_company.click()

    def enter_deal(self,deal):
        self.driver.find_element(*AddNewCases.Deal_xpath).send_keys(deal)
        select_deal = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Deal_xpath))
        select_deal.click()

    def select_type(self):
        self.driver.find_element(*AddNewCases.Type_xpath).click()
        select_type = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Type_xpath))
        select_type.click()

    def select_deadline(self):
        self.driver.find_element(*AddNewCases.Deadline_xpath).click()
        self.driver.find_element(*AddNewCases.Select_Deadline_xpath).click()
        self.driver.find_element(*AddNewCases.Select_Deadline_time_xpath).click()

    def select_close_date(self):
        self.driver.find_element(*AddNewCases.Close_Date_xpath).click()
        self.driver.find_element(*AddNewCases.Select_Close_Date_xpath).click()
        self.driver.find_element(*AddNewCases.Select_Close_Time_xpath).click()

    def enter_tag(self,tag):
        self.driver.find_element(*AddNewCases.Tag_xpath).send_keys(tag)
        select_tag = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Tag_xpath))
        select_tag.click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewCases.Description_xpath).send_keys(desc)

    def select_priority(self):
        self.driver.find_element(*AddNewCases.Priority_xpath).click()
        select_priority = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Priority_xpath))
        select_priority.click()

    def select_status(self):
        self.driver.find_element(*AddNewCases.Status_xpath).click()
        select_status = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCases.Select_Status_xpath))
        select_status.click()

    def enter_identifier(self,idef):
        self.driver.find_element(*AddNewCases.Identifier_xpath).send_keys(idef)

    def save_task(self):
        self.driver.find_element(*AddNewCases.Save_Button_xpath).click()

    def verify_new_deal_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewCases.Star_xpath)))
            print("Successfully created a new task.")
        except:
            print("Failed to create a new contact.")
            assert False













