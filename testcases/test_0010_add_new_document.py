import time

from pageObjects.Add_new_document import AddNewDocument
from pageObjects.Login_Page import Login


class TestAddNewDocuments ():
    def test_add_new_task(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_email('gauravkale.sinhgad@gmail.com')
        self.lp.enter_password('Royal@12345')
        self.lp.click_login_button()
        self.AND = AddNewDocument(self.driver)
        self.AND.hover_and_click_add_new_tasks()
        self.AND.enter_title('Document testing')
        self.AND.enter_tag('technology')
        self.AND.enter_description('Description about the testing documents')
        self.AND.select_file()
        self.AND.enter_contact('Sean')
        self.AND.enter_company('Next')
        self.AND.enter_deal('Testing')
        self.AND.enter_case('Case')
        self.AND.enter_task('WCC')
        self.AND.enter_identifier('Testing of identifier')
        self.AND.save_task()
        self.AND.verify_new_deal_created()










