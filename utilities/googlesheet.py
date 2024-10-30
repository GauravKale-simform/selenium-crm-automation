import gspread
from google.oauth2.service_account import Credentials

class GoogleSheetReader:
    def __init__(self, credentials_file, sheet_name, worksheet_name):
        self.credentials_file = credentials_file
        self.sheet_name = sheet_name
        self.worksheet_name = worksheet_name
        self.scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.creds = Credentials.from_service_account_file(self.credentials_file, scopes=self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(self.sheet_name)
        self.worksheet = self.sheet.worksheet(self.worksheet_name)

    def get_all_records(self):
        return self.worksheet.get_all_records()





# import gspread
# from google.oauth2.service_account import Credentials
#
# CREDENTIALS_FILE = './credentials.json'
# SHEET_NAME = 'CRM_testdata'
# WORKSHEET_NAME = 'Sheet1'
#
# scope = [
#     'https://www.googleapis.com/auth/spreadsheets',
#     'https://www.googleapis.com/auth/drive'
# ]
# creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
# client = gspread.authorize(creds)
#
# sheet = client.open(SHEET_NAME)
# worksheet = sheet.worksheet(WORKSHEET_NAME)
#
# data = worksheet.get_all_records()
#
# for row in data:
#     print(row)



