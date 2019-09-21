import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import *


class GSheetIO():
    """object that allows client to read and write from a Google Sheet"""
    def __init__(self, sheetName):
        """create GSheetIO object that interacts with GSheet with name sheetName"""
        self.sheetName = sheetName
        self.sheet = self.openSheet()

    def openSheet(self):
        """open google sheet"""
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
        file = gspread.authorize(credentials)
        return file.open(self.sheetName).sheet1


# set day
# if day != today, start new column
# every time write, write to first blank cells in columns