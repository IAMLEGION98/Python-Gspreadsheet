import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('<YOUR_JSON_FILENAME>.json',scope)
client= gspread.authorize(creds)
sheet = client.open('<YOUR_SPREADSHEET_NAME>').sheet1
traders = sheet.get_all_records()
print(traders)
sheet.update_cell(3,2,'47.5')   #CELL value to modify with
print(traders)   #print all contents of sheet

