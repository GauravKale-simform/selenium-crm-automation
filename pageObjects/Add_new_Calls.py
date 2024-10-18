import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewCalls:
    Hover_Calls_xpath = (By.XPATH,"//span[normalize-space()='Calls']")
    Create_Calls_xpath = (By.XPATH,"//div[@id='main-nav']//div[8]//button[1]//i[1]")
    CallScript_label_xpath = (By.XPATH,"//label[normalize-space()='Call Script']")

    Call_Time_xpath = (By.XPATH,"(//input[@type='text'])[2]")
    Select_Call_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Monday, 28 October 2024']")
    Select_Call_Time_xpath = (By.XPATH,"//li[normalize-space()='14:00']")

    Type_xpath = (By.XPATH, "(//div[@name='type'])[1]")
    Select_Type_xpath = (By.XPATH, "//span[normalize-space()='Call']")

    Call_Script_xpath = (By.XPATH,"//div[contains(text(),'Select')]")

    Duration_xpath = (By.XPATH,"//input[@name='duration']")

    Start_Time_xpath = (By.XPATH, "(//input[@type='text'])[5]")
    Select_Start_Date_Time_xpath = (By.XPATH, "//div[@aria-label='Choose Monday, 28 October 2024']")
    Select_Start_Time_xpath = (By.XPATH, "//li[normalize-space()='15:00']")

    Flag_xpath = (By.XPATH,"(//div[@name='flag'])[1]")
    Select_Flat_xpath = (By.XPATH,"//span[contains(text(),'Important')]")

    Tag_xpath = (By.XPATH, "(//input[@class='search'])[2]")
    Select_Tag_xpath = (By.XPATH, "(//span[normalize-space()='business'])[2]")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    Participants_xpath = (By.XPATH,'//*[@id="main-content"]/div/div[2]/form/div[5]/div[2]/div/div/input')
    Select_Participants_xpath = (By.XPATH,"//div[@model_type='contact']") #nextpoint

    Deal_xpath = (By.XPATH, "//div[@name='deal']//input[@type='text']")
    Select_Deal_xpath = (By.XPATH, "//span[contains(text(),'Testing Deal 02 - Inactive')]")

    Case_xpath = (By.XPATH,"//div[@name='case']//input[@type='text']")
    Select_Case_xpath = (By.XPATH,"//span[normalize-space()='Case Testing - 01']")

    Task_xpath = (By.XPATH,"//div[@name='task']//input[@type='text']")
    Select_Task_xpath = (By.XPATH,"//span[normalize-space()='Team Meeting']")

    Conference_Call_Number_Country_xpath = (By.XPATH,"//div[@name='hint']//input[@type='text']")
    India_xpath = (By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']")

    Phone_Number_xpath = (By.XPATH,"//input[@placeholder='Number']")

    Type_of_Phone_Number_xpath = (By.XPATH,"//input[@placeholder='Home, Work, Mobile...']") #Home,work,mobile

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")

    Star_xpath = (By.XPATH, '//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    Save_Button_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_deals(self):
        hover_on_add_deals = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewCalls.Hover_Calls_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_add_deals).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCalls.Create_Calls_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCalls.CallScript_label_xpath)).click()

    def select_call_time(self):
        self.driver.find_element(*AddNewCalls.Call_Time_xpath).click()
        self.driver.find_element(*AddNewCalls.Select_Call_Date_xpath).click()
        self.driver.find_element(*AddNewCalls.Select_Call_Time_xpath).click()

    def select_type(self):
        self.driver.find_element(*AddNewCalls.Type_xpath).click()
        select_type = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Type_xpath))
        select_type.click()

    def enter_callscript(self,cs):
        self.driver.find_element(*AddNewCalls.Call_Script_xpath).send_keys(cs)

    def enter_duration(self,dura):
        self.driver.find_element(*AddNewCalls.Duration_xpath).send_keys(dura)

    def select_start_time(self):
        self.driver.find_element(*AddNewCalls.Start_Time_xpath).click()
        self.driver.find_element(*AddNewCalls.Select_Start_Date_Time_xpath).click()
        self.driver.find_element(*AddNewCalls.Select_Start_Time_xpath).click()

    def select_flag(self):
        self.driver.find_element(*AddNewCalls.Flag_xpath).click()
        select_flag = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Flat_xpath))
        select_flag.click()

    def enter_tag(self,tag):
        self.driver.find_element(*AddNewCalls.Tag_xpath).send_keys(tag)
        select_tag = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Tag_xpath))
        select_tag.click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewCalls.Description_xpath).send_keys(desc)

    def enter_participants(self,par):
        self.driver.find_element(*AddNewCalls.Participants_xpath).send_keys(par)
        select_par = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Participants_xpath))
        select_par.click()

    # def enter_participants(self,par):
    #     parti = self.driver.find_element(By.XPATH,"//div[@class='ui field'] //label[.='Participants']")
    #     self.driver.find_element(locate_with(By.XPATH,"//input[@class='search']").below(parti)).send_keys(par)
    #     # self.driver.find_element(*AddNewCalls.Participants_xpath).send_keys(par)
    #     select_par = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Participants_xpath))
    #     select_par.click()

    def enter_deal(self,deal):
        self.driver.find_element(*AddNewCalls.Deal_xpath).send_keys(deal)
        select_deal = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Deal_xpath))
        select_deal.click()

    def enter_case(self,case):
        self.driver.find_element(*AddNewCalls.Case_xpath).send_keys(case)
        select_case = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Case_xpath))
        select_case.click()

    def enter_task(self,task):
        self.driver.find_element(*AddNewCalls.Task_xpath).send_keys(task)
        select_task = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.Select_Task_xpath))
        select_task.click()

    def select_country(self):
        self.driver.find_element(*AddNewCalls.Conference_Call_Number_Country_xpath).click()
        select_india = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalls.India_xpath))
        select_india.click()

    def enter_phone_number(self,epn):
        self.driver.find_element(*AddNewCalls.Phone_Number_xpath).send_keys(epn)

    def enter_type_phone(self,etp):
        self.driver.find_element(*AddNewCalls.Type_of_Phone_Number_xpath).send_keys(etp)

    def enter_identifier(self,idef):
        self.driver.find_element(*AddNewCalls.Identifier_xpath).send_keys(idef)

    def save_task(self):
        self.driver.find_element(*AddNewCalls.Save_Button_xpath).click()

    def verify_new_deal_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewCalls.Star_xpath)))
            print("Successfully created a new calls.")
        except:
            print("Failed to create a new calls.")
            assert False

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
















