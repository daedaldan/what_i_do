import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time


class GSheetIO():
    """object that allows client to read and write from a Google Sheet"""
    def __init__(self, sheetName):
        """create GSheetIO object that interacts with GSheet with name sheetName"""
        self.sheetName = sheetName
        self.sheet = self.openSheet("creds.json")
        self.today = datetime.today()
        self.startCol, self.startRow = self.startWrite()

    def openSheet(self, jsonKey):
        """open google sheet"""
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonKey, scope)
        file = gspread.authorize(credentials)
        return file.open(self.sheetName).sheet1

    def startWrite(self):
        col = 0
        row = 1
        dateFound = False
        sheet_values = self.sheet.get_all_values()
        if len(sheet_values) == 0:
            sheet_values.append([])
        for value in sheet_values[0]:
            col += 1
            if value == self.formatDate(self.today):
                dateFound = True
                break
        if not dateFound:
            col += 2
            self.sheet.update_cell(1, col, self.formatDate(self.today))
        while self.sheet.cell(row, col).value != "":
            row += 1
        self.formatDate(self.today)
        return col, row

    def writeTask(self, name, start, end, length):
        self.sheet.update_cell(self.startRow, self.startCol-1, name)
        self.sheet.update_cell(self.startRow, self.startCol, self.formatTime(start))
        self.sheet.update_cell(self.startRow+1, self.startCol, self.formatTime(end))
        self.startRow += 2

    def formatDate(self, myDate):
        return myDate.strftime("%m/%d")

    def formatTime(self, myTime):
        return myTime.strftime("%H:%M:%S")
