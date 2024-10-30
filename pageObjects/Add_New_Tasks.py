from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddNewTask:
    Hover_Tasks_xpath = (By.XPATH,"//div[@class='menu-item-wrapper'][6]")
    Create_Tasks_xpath = (By.XPATH,"//div[@id='main-nav']//div[6]//button[1]//i[1]")
    Contact_label_xpath = (By.XPATH,"//label[normalize-space()='Type']")

    Title_xpath = (By.XPATH, "//input[contains(@name,'title')]")

    Assigned_to_xpath = (By.XPATH,"//div[@class='ui fluid selection dropdown']")
    Select_Assigned_xpath = (By.XPATH,"(//span[@class='text'][normalize-space()='Guarav Kale'])[2]")

    Type_xpath = (By.XPATH,"//div[@name='type']//div[@role='alert'][normalize-space()='Select']")
    Select_Type_xpath = (By.XPATH,"//span[normalize-space()='Business Support']") #business support

    Due_Date_xpath = (By.XPATH,"(//input[@class='calendarField'])[1]")
    Select_Due_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Friday, 18 October 2024']") #18 Oct
    Select_Due_Time_xpath = (By.XPATH,"//li[normalize-space()='18:00']")

    Contacts_xpath = (By.XPATH,"//div[@name='contact']//input[@type='text']")
    Select_Contacts_xpath = (By.XPATH,"//div[@class='selected item']//span[@class='text'][normalize-space()='Abhishek Radha Sen']") #Ramesh

    Company_xpath = (By.XPATH,"//div[@name='company']//input[@type='text']")
    Select_Company_xpath = (By.XPATH,"//span[normalize-space()='Testing Your Source']")

    Deal_xpath = (By.XPATH,"(//input[@class='search'])[3]")
    Select_Deal_xpath = (By.XPATH,"//span[normalize-space()='Deal - Inactive']")

    Case_xpath = (By.XPATH,"(//input[@class='search'])[4]")
    Select_Case_xpath = (By.XPATH,"//span[normalize-space()='Case Testing - 1']")

    Close_Date_xpath = (By.XPATH,"(//input[@class='calendarField'])[2]")
    Select_Close_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Monday, 21 October 2024']") #21 Oct
    Select_Close_Time_xpath = (By.XPATH,"//li[normalize-space()='18:00']")

    Tag_xpath = (By.XPATH,"(//input[@class='search'])[5]")
    Select_Tag_xpath = (By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div[6]/div[1]/div/div/div/div/span")

    Description_xpath = (By.XPATH, "//textarea[@name='description']")

    Completion_xpath = (By.XPATH,"//input[@name='completion']")

    Priority_xpath = (By.XPATH,"(//div[@name='priority'])[1]")
    Select_Priority_xpath = (By.XPATH,"//span[normalize-space()='Normal']") #Normal Priority

    Status_xpath = (By.XPATH,"(//div[@name='status'])[1]")
    Select_Status_xpath = (By.XPATH,"//span[contains(text(),'Reviewing')]") #Reviewing

    Identifier_xpath = (By.XPATH, "//input[@name='identifier']")

    Save_Button_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    Star_xpath = (By.XPATH, '//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_tasks(self):
        hover_on_add_tasks = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewTask.Hover_Tasks_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_add_tasks).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewTask.Create_Tasks_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewTask.Contact_label_xpath)).click()

    def enter_title(self,title):
        self.driver.find_element(*AddNewTask.Title_xpath).send_keys(title)

    def select_assigned_to(self):
        self.driver.find_element(*AddNewTask.Assigned_to_xpath).click()
        select_assign = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Assigned_xpath))
        select_assign.click()

    def select_type(self):
        self.driver.find_element(*AddNewTask.Type_xpath).click()
        select_type = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Type_xpath))
        select_type.click()

    def deu_date(self):
        self.driver.find_element(*AddNewTask.Due_Date_xpath).click()
        self.driver.find_element(*AddNewTask.Select_Due_Date_xpath).click()
        self.driver.find_element(*AddNewTask.Select_Due_Time_xpath).click()

    def enter_contact(self,contact):
        self.driver.find_element(*AddNewTask.Contacts_xpath).send_keys(contact)
        select_contact = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Contacts_xpath))
        select_contact.click()

    def enter_company(self,company):
        self.driver.find_element(*AddNewTask.Company_xpath).send_keys(company)
        select_company = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Company_xpath))
        select_company.click()

    def enter_deal(self,deal):
        self.driver.find_element(*AddNewTask.Deal_xpath).send_keys(deal)
        select_deal = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Deal_xpath))
        select_deal.click()

    def enter_case(self,case):
        self.driver.find_element(*AddNewTask.Case_xpath).send_keys(case)
        select_case = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Case_xpath))
        select_case.click()

    def close_date(self):
        self.driver.find_element(*AddNewTask.Close_Date_xpath).click()
        self.driver.find_element(*AddNewTask.Select_Close_Date_xpath).click()
        self.driver.find_element(*AddNewTask.Select_Close_Time_xpath).click()

    def enter_tags(self,tag):
        self.driver.find_element(*AddNewTask.Tag_xpath).send_keys(tag)
        select_tag = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Tag_xpath))
        select_tag.click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewTask.Description_xpath).send_keys(desc)

    def enter_completion(self,comp):
        self.driver.find_element(*AddNewTask.Completion_xpath).send_keys(comp)

    def select_priority(self):
        self.driver.find_element(*AddNewTask.Priority_xpath).click()
        select_priority = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Priority_xpath))
        select_priority.click()

    def select_status(self):
        self.driver.find_element(*AddNewTask.Status_xpath).click()
        select_status = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewTask.Select_Status_xpath))
        select_status.click()

    def enter_identifier(self,idef):
        self.driver.find_element(*AddNewTask.Identifier_xpath).send_keys(idef)

    def save_task(self):
        self.driver.find_element(*AddNewTask.Save_Button_xpath).click()

    def verify_new_deal_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewTask.Star_xpath)))
            print("Successfully created a new task.")
        except:
            print("Failed to create a new contact.")
            assert False







