from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddNewCalendar:
    Hover_Calendar_xpath = (By.XPATH,"//span[normalize-space()='Calendar']")
    Create_Calendar_xpath = (By.XPATH,"//div[@id='main-nav']//div[2]//button[1]//i[1]")
    End_date_label_xpath =(By.XPATH,"//label[normalize-space()='End Date']")

    Start_Date_xpath = (By.XPATH,"//label[text()='Start Date']/following-sibling::div[contains(@class, 'calendarField')]")
    Select_Start_Day_xpath = (By.XPATH,"//div[@aria-label='Choose Monday, 26 August 2024']") #26 Aug Monday
    Select_Start_Time_xath = (By.XPATH,"//li[normalize-space()='10:00']") #Morning 10 Am

    End_Date_xpath = (By.XPATH,"//label[text()='End Date']/following-sibling::div[contains(@class, 'calendarField')]")
    Select_End_Day_xpath = (By.XPATH,"//div[@aria-label='Choose Monday, 26 August 2024']") #26 Aug Monday
    Select_End_Time_xath = (By.XPATH,"//li[normalize-space()='11:00']") #Morning 10 Am

    Category_xpath = (By.XPATH,"//div[@name='category']//i[@class='dropdown icon']")
    Category_Important_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[2]")
    Category_Opportunity_xpath = (By.XPATH,"//div[@name='category']//div[3]")
    Category_Optional_xpath = (By.XPATH,"//div[@name='category']//div[4]")
    Category_Critical_xpath = (By.XPATH,"//div[@name='category']//div[5]")
    Category_Meeting_xpath = (By.XPATH,"//div[@name='category']//div[6]")
    Category_Social_xpath = (By.XPATH,"//div[@name='category']//div[7]")
    Category_Time_Off_xpath = (By.XPATH,"//div[@name='category']//div[8]")
    Category_Private_xpath = (By.XPATH,"//div[@name='category']//div[9]")

    Tag_xpath = (By.XPATH,"//div[@class='ui active visible fluid multiple search selection dropdown']")
    Tag_Interview_xpath =(By.XPATH,"//span[normalize-space()='Interview Technical Round']")

    Description_xpath = (By.XPATH,"//textarea[@name='description']")

    Location_xpath = (By.XPATH,"//textarea[@name='location']")

    All_Day_toggle_button_xpath = (By.XPATH,"//div[@class='ui toggle checkbox']//label[contains(text(),'All Day')]")

    Deal_xpath = (By.XPATH,"//div[@name='deal']//input[@type='text']")
    Deal_Opportunity_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[@role='option']")

    Task_xpath = (By.XPATH,"//div[@name='task']//input[@type='text']")
    Select_Task_xpath = (By.XPATH,"//span[contains(text(),'Schedule the interview and provide detailed feedba')]")

    Case_xpath = (By.XPATH,"//div[@name='case']//input[@type='text']")
    Select_Case_xpath = (By.XPATH,"//div[@name='case']//div[@role='listbox']//div[2]")

    Alert_Before_xpath = (By.XPATH,"//div[@name='minutesBefore']")
    Select_Alert_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]")

    Alert_Via_xpath = (By.XPATH,"//div[@name='channels']//i[@class='dropdown icon']")
    Select_Alert_Via_xpath = (By.XPATH,"//div[@name='channels']//div[2]")

    Reminder_Time_xpath = (By.XPATH,"//input[@name='reminder_minutes']")

    Participants_xpath = (By.XPATH,"//div[@name='participants']")
    Select_Participants_xpath = (By.XPATH,"//span[@class='text'][normalize-space()='Sr. Manager']")

    Company_xpath = (By.XPATH,"//div[@name='company']//input[@type='text']")
    Select_Company_xpath = (By.XPATH,"//span[normalize-space()='NextPoint']")

    Recurrence_xpath = (By.XPATH,"//a[normalize-space()='No recurrence. Click to set.']")
    Re_Interval_xpath = (By.XPATH,"//div[@name='freq']")
    Re_In_Daily_xpath = (By.XPATH,"//div[@class='visible menu transition']//div[1]")
    Re_In_Weekly_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[2]")
    Re_In_Monthly_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[3]")
    Re_In_Yearly_xpath = (By.XPATH, "//div[@class='visible menu transition']//div[4]")
    Re_In_Times_xpath = (By.XPATH,"//input[@name='count']")
    Re_In_Endat_xpath = (By.XPATH,"//input[@class='calendarField react-datepicker-ignore-onclickoutside']")
    Re_In_Endat_Date_xpath = (By.XPATH,"//div[@aria-label='Choose Monday, 26 August 2024']")
    Re_In_Endat_Time_xpath = (By.XPATH,"//li[normalize-space()='15:00']")
    Re_Cancle_xpath = (By.XPATH,"//button[@class='ui black button']")
    Re_Set_xpath = (By.XPATH,"//button[normalize-space()='Set']")
    Recurrence_Clear_xpath = (By.XPATH,"//a[normalize-space()='Clear']")

    Identifier_xpath = (By.XPATH,"//input[@name='identifier']")








