import time

from pageObjects.Add_new_Calendar_Event import AddNewCalendar
from pageObjects.Login_Page import Login

class TestCalenderEvent ():
    def test_add_new_calender_event(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.ANCAL = AddNewCalendar(self.driver)
        self.ANCAL.hover_and_click_add_new_calender()
        self.ANCAL.enter_title('Technical Round Of Interview')
        self.ANCAL.select_start_date()
        self.ANCAL.select_end_date()
        self.ANCAL.select_category()
        self.ANCAL.enter_tag('Interview')
        self.ANCAL.enter_description('We have schedule an interview today')
        self.ANCAL.enter_location('Microsoft Teams')
        self.ANCAL.enter_deal('Opportunity')
        self.ANCAL.enter_task('Schedule the interview')
        self.ANCAL.enter_case('Descriptive')
        self.ANCAL.scroll_down()
        self.ANCAL.select_alert()
        self.ANCAL.select_alert_via()
        self.ANCAL.enter_remainder_time('15')
        self.ANCAL.scroll_down()
        self.ANCAL.select_participants('Manager')
        self.ANCAL.select_company('Next')
        self.ANCAL.select_recurrence()
        self.ANCAL.select_interval()
        self.ANCAL.select_days()
        self.ANCAL.select_re_times('2')
        self.ANCAL.select_re_end_date()
        self.ANCAL.set_recurrance()
        time.sleep(1)
        self.ANCAL.clear_recurrence()
        time.sleep(1)
        self.ANCAL.enter_identifier('Nothing to identify')
        self.ANCAL.save_event()
        time.sleep(1)
        self.ANCAL.verify_calender_event_created()


