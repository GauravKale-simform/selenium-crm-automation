from select import select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewDocument:
    Hover_Documents_xpath = (By.XPATH,"//div[@class='menu-item-wrapper'][9]")
    Create_Documents_xpath = (By.XPATH,"//div[@id='main-nav']//div[9]//button[1]//i[1]")
    Tags_label_xpath = (By.XPATH,"//label[normalize-space()='Tags']")

    Title_xpath = (By.XPATH,"//input[@name='title']")

    Tag_xpath = (By.XPATH, "(//input[@class='search'])[2]")
    Select_Tag_xpath = (By.XPATH, "(//span[normalize-space()='technology'])[2]")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    File_xpath = (By.XPATH,"//input[@name='file']")

    Contact_xpath = (By.XPATH,"(//input[@class='search'])[3]")
    Select_Contact_xpath = (By.XPATH,"//span[normalize-space()='Rajesh Kumar']")

    Company_xpath = (By.XPATH, "//div[@name='company']//input[@type='text']")
    Select_Company_xpath = (By.XPATH, "//span[normalize-space()='NextPoint']")

    Deal_xpath = (By.XPATH, "(//input[@class='search'])[5]")
    Select_Deal_xpath = (By.XPATH, "//span[normalize-space()='Deal - Active']")

    Case_xpath = (By.XPATH,"//div[@name='case']//input[@type='text']")
    Select_Case_xpath = (By.XPATH,"//span[normalize-space()='Case Testing - 2']")

    Task_xpath = (By.XPATH,"//div[@name='task']//input[@type='text']")
    Select_Task_xpath = (By.XPATH,"//span[normalize-space()='Requirements Gathering']")

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")

    Star_xpath = (By.XPATH, '//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    Save_Button_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_tasks(self):
        hover_on_add_cases = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewDocument.Hover_Documents_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_add_cases).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewDocument.Create_Documents_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewDocument.Tags_label_xpath)).click()

    def enter_title(self,title):
        self.driver.find_element(*AddNewDocument.Title_xpath).send_keys(title)

    def enter_tag(self,tag):
        self.driver.find_element(*AddNewDocument.Tag_xpath).send_keys(tag)
        select_tag = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDocument.Select_Tag_xpath))
        select_tag.click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewDocument.Description_xpath).send_keys(desc)

    def select_file(self):
        file_path = ("C://Users//gaurav//Desktop//Automation//Testing Document uploading")
        upload_file = self.driver.find_element(*AddNewDocument.File_xpath)
        upload_file.send_keys(file_path)

    def enter_contact(self,cnt):
        self.driver.find_element(*AddNewDocument.Contact_xpath).send_keys(cnt)
        select_contact = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDocument.Select_Contact_xpath))
        select_contact.click()

    def enter_company(self,company):
        self.driver.find_element(*AddNewDocument.Company_xpath).send_keys(company)
        select_company = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDocument.Select_Company_xpath))
        select_company.click()

    def enter_deal(self,deal):
        self.driver.find_element(*AddNewDocument.Deal_xpath).send_keys(deal)
        select_deal = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDocument.Select_Deal_xpath))
        select_deal.click()

    def enter_case(self,case):
        self.driver.find_element(*AddNewDocument.Case_xpath).send_keys(case)
        select_case = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDocument.Select_Case_xpath))
        select_case.click()

    def enter_task(self,task):
        self.driver.find_element(*AddNewDocument.Task_xpath).send_keys(task)
        select_task = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewDocument.Select_Task_xpath))
        select_task.click()

    def enter_identifier(self,idf):
        self.driver.find_element(*AddNewDocument.Identifier_xpath).send_keys(idf)

    def save_task(self):
        self.driver.find_element(*AddNewDocument.Save_Button_xpath).click()

    def verify_new_deal_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewDocument.Star_xpath)))
            print("Successfully created a new document.")
        except:
            print("Failed to create a new document.")
            assert False


