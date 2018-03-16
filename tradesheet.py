import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope= ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('<YOUR_JSON_FILENAME>.json',scope)
client=gspread.authorize(creds)
sheet= client.open('<YOUR_SPREADSHEET_NAME>').sheet1  #CELL value to modify with
data=sheet.get_all_records()
print(data)  #print all contents of sheet
