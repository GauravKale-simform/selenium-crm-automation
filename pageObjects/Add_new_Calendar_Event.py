import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewCalendar:
    Hover_Calendar_xpath = (By.XPATH,"//span[normalize-space()='Calendar']")
    Create_Calendar_xpath = (By.XPATH,"//div[@id='main-nav']//div[2]//button[1]//i[1]")
    End_date_label_xpath =(By.XPATH,"//label[normalize-space()='End Date']")

    Title_xpath = (By.XPATH,"//input[contains(@name,'title')]")

    Start_Date_xpath = (By.XPATH,"//label[text()='Start Date']/following-sibling::div[contains(@class, 'calendarField')]")
    Select_Start_Day_xpath = (By.XPATH,"//div[@aria-label='Choose Thursday, 17 October 2024']") #17 Oct Thursday
    Select_Start_Time_xath = (By.XPATH,"//li[normalize-space()='10:00']") #Morning 10 Am

    End_Date_xpath = (By.XPATH,"//label[text()='End Date']/following-sibling::div[contains(@class, 'calendarField')]")
    Select_End_Day_xpath = (By.XPATH,"//div[@aria-label='Choose Thursday, 17 October 2024']") # 17 Oct Thursday
    Select_End_Time_xath = (By.XPATH,"//li[normalize-space()='10:30']") #Morning 10.30 Am

    Category_xpath = (By.XPATH,"//div[@name='category']//i[@class='dropdown icon']")
    Category_Important_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Category_Opportunity_xpath = (By.XPATH,"//div[@name='category']//div[3]")
    Category_Optional_xpath = (By.XPATH,"//div[@name='category']//div[4]")
    Category_Critical_xpath = (By.XPATH,"//div[@name='category']//div[5]")
    Category_Meeting_xpath = (By.XPATH,"//div[@name='category']//div[6]")
    Category_Social_xpath = (By.XPATH,"//div[@name='category']//div[7]")
    Category_Time_Off_xpath = (By.XPATH,"//div[@name='category']//div[8]")
    Category_Private_xpath = (By.XPATH,"//div[@name='category']//div[9]")

    Tag_xpath = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[3]/div[2]/div[1]/div[1]/input[1]")
    Tag_Interview_xpath =(By.XPATH,"//span[normalize-space()='Interview Technical Round']")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    Location_xpath = (By.XPATH,"//textarea[@name='location']")

    All_Day_toggle_button_xpath = (By.XPATH,"//div[@class='ui toggle checkbox']//label[contains(text(),'All Day')]")

    Deal_xpath = (By.XPATH,"//div[@name='deal']//input[@type='text']")
    Deal_Opportunity_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[@role='option']")

    Task_xpath = (By.XPATH,"//div[@name='task']//input[@type='text']")
    Select_Task_xpath = (By.XPATH,"//span[contains(text(),'Schedule the interview and provide detailed feedba')]")

    Case_xpath = (By.XPATH,"//div[@name='case']//input[@type='text']")
    Select_Case_xpath = (By.XPATH,"//div[@name='case']//div[@role='listbox']//div[1]") #Descriptive

    Alert_Before_xpath = (By.XPATH,"//div[@name='minutesBefore']")
    Select_Alert_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]") #10 Min before

    Alert_Via_xpath = (By.XPATH,"//div[@name='channels']//i[@class='dropdown icon']")
    Select_Alert_Via_xpath = (By.XPATH,"(//div[@name='channels']//div[1])[2]") #Email

    Reminder_Time_xpath = (By.XPATH,"//input[@name='reminder_minutes']") #15 Min

    Participants_xpath = (By.XPATH,"//div[@name='participants'] //input[@aria-autocomplete='list']") #sr. manager
    Select_Participants_xpath = (By.XPATH,"//span[normalize-space()='Sr. Manager']")

    Company_xpath = (By.XPATH,"//div[@name='company'] //input[@aria-autocomplete='list']")
    Select_Company_xpath = (By.XPATH,"//span[normalize-space()='NextPoint']")

    Recurrence_xpath = (By.XPATH,"//a[normalize-space()='No recurrence. Click to set.']")
    Re_Interval_xpath = (By.XPATH,"//div[@name='freq']")
    Re_In_Daily_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]")
    Re_In_Weekly_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[2]")
    Re_In_Monthly_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[3]")
    Re_In_Yearly_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[4]")
    Re_In_Times_xpath = (By.XPATH,"//input[@name='count']")
    Re_In_Days_xpath = (By.XPATH,"//div[contains(@name,'byweekday')]")
    Re_In_Days_monday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]")
    Re_In_Days_tuesday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Re_In_Days_wednesday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[3]")
    Re_In_Days_thursday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[4]")
    Re_In_Days_friday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[5]")
    Re_In_Days_saturday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[6]")
    Re_In_Days_sunday_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[7]")
    Re_Interval_Time_xpath = (By.XPATH,"//input[@name='interval']")
    Re_In_Endat_xpath = (By.XPATH,"(//input[@class='calendarField'])[3]")
    Re_In_Endat_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Friday, 18 October 2024']")
    Re_In_Endat_Time_xpath = (By.XPATH,"//li[normalize-space()='18:00']")
    Re_Cancle_xpath = (By.XPATH,"//button[@class='ui black button']")
    Re_Set_xpath = (By.XPATH,"//button[normalize-space()='Set']")
    Recurrence_Clear_xpath = (By.XPATH,"//a[normalize-space()='Clear']")
    days_label_xpath = (By.XPATH,"//label[normalize-space()='Days']")

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")

    save_button_xpath = (By.XPATH,"//button[@class='ui linkedin button']")

    Star_xpath = (By.XPATH, '//*[@id="dashboard-toolbar"]/div[2]/div/div[1]')

    def __init__(self,driver):
        self.driver = driver

    def hover_and_click_add_new_calender(self):
        hover_on_add_calender = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddNewCalendar.Hover_Calendar_xpath))
        action = ActionChains(self.driver)
        action.move_to_element(hover_on_add_calender).perform()
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCalendar.Create_Calendar_xpath))
        add_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AddNewCalendar.End_date_label_xpath)).click()

    def enter_title(self,name):
        self.driver.find_element(*AddNewCalendar.Title_xpath).send_keys(name)

    def select_start_date(self):
        self.driver.find_element(*AddNewCalendar.Start_Date_xpath).click()
        self.driver.find_element(*AddNewCalendar.Select_Start_Day_xpath).click()
        self.driver.find_element(*AddNewCalendar.Select_Start_Time_xath).click()

    def select_end_date(self):
        self.driver.find_element(*AddNewCalendar.End_Date_xpath).click()
        self.driver.find_element(*AddNewCalendar.Select_End_Day_xpath).click()
        self.driver.find_element(*AddNewCalendar.Select_End_Time_xath).click()

    def select_category(self):
        self.driver.find_element(*AddNewCalendar.Category_xpath).click()
        self.driver.find_element(*AddNewCalendar.Category_Meeting_xpath).click()

    def enter_tag(self,tag):
        self.driver.find_element(*AddNewCalendar.Tag_xpath).send_keys(tag)
        tag_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Tag_Interview_xpath))
        tag_option.click()

    def enter_description(self,desc):
        self.driver.find_element(*AddNewCalendar.Description_xpath).send_keys(desc)

    def enter_location(self,location):
        self.driver.find_element(*AddNewCalendar.Location_xpath).send_keys(location)

    def enter_deal(self,deal):
        self.driver.find_element(*AddNewCalendar.Deal_xpath).send_keys(deal)
        deal_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Deal_Opportunity_xpath))
        deal_option.click()

    def enter_task(self,task):
        self.driver.find_element(*AddNewCalendar.Task_xpath).send_keys(task)
        task_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Select_Task_xpath))
        task_option.click()

    def enter_case(self,case):
        self.driver.find_element(*AddNewCalendar.Case_xpath).send_keys(case)
        case_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Select_Case_xpath))
        case_option.click()

    def select_alert(self):
        self.driver.find_element(*AddNewCalendar.Alert_Before_xpath).click()
        self.driver.find_element(*AddNewCalendar.Select_Alert_xpath).click()

    def select_alert_via(self):
        self.driver.find_element(*AddNewCalendar.Alert_Via_xpath).click()
        self.driver.find_element(*AddNewCalendar.Select_Alert_Via_xpath).click()

    def enter_remainder_time(self,min):
        self.driver.find_element(*AddNewCalendar.Reminder_Time_xpath).send_keys(min)

    def select_participants(self,part):
        self.driver.find_element(*AddNewCalendar.Participants_xpath).send_keys(part)
        part_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Select_Participants_xpath))
        part_option.click()

    def select_company(self,company):
        self.driver.find_element(*AddNewCalendar.Company_xpath).send_keys(company)
        c_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Select_Company_xpath))
        c_option.click()

    # def select_recurrence(self):

    def enter_identifier(self,idf):
        self.driver.find_element(*AddNewCalendar.Identifier_xpath).send_keys(idf)

    def select_recurrence(self):
        self.driver.find_element(*AddNewCalendar.Recurrence_xpath).click()

    def select_interval(self):
        self.driver.find_element(*AddNewCalendar.Re_Interval_xpath).click()
        monthly = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Re_In_Monthly_xpath))
        monthly.click()

    def select_days(self):
        self.driver.find_element(*AddNewCalendar.Re_In_Days_xpath).click()
        Thursday = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Re_In_Days_thursday_xpath))
        Thursday.click()
        self.driver.find_element(*AddNewCalendar.days_label_xpath).click()

    def select_re_times(self,intv):
        self.driver.find_element(*AddNewCalendar.Re_In_Times_xpath).send_keys(intv)

    def select_re_end_date(self):
        self.driver.find_element(*AddNewCalendar.Re_In_Endat_xpath).click()
        select_date = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Re_In_Endat_Date_xpath))
        select_date.click()
        select_time = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(AddNewCalendar.Re_In_Endat_Time_xpath))
        select_time.click()

    def set_recurrance(self):
        self.driver.find_element(*AddNewCalendar.Re_Set_xpath).click()
        self.driver.save_screenshot("C:/Users/gaurav/Desktop/Automation/CRM_Project/ScreenShots/set_reccurance.png")

    def clear_recurrence(self):
        self.driver.find_element(*AddNewCalendar.Recurrence_Clear_xpath).click()
        self.driver.save_screenshot("C:/Users/gaurav/Desktop/Automation/CRM_Project/ScreenShots/clearing_recurrence.png")


    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 100);")

    def save_event(self):
        self.driver.find_element(*AddNewCalendar.save_button_xpath).click()

    def verify_calender_event_created(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((AddNewCalendar.Star_xpath)))
            print("Successfully created a new contact.")
        except:
            print("Failed to create a new contact.")
            assert False















