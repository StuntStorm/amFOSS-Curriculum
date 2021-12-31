import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials

import mysqlcredentials as mc

scope = ['https://spreadsheets.google.com/feeds', \
       'https://www.googleapis.com/auth/drive']


creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_url(sheetName).get_worksheet(worksheetIndex)
print(sheet.get_all_values()[1:])
#Will work on this later
