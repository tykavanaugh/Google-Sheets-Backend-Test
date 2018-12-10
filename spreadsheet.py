import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
pp = pprint.PrettyPrinter()
sheet = client.open('My Legislators 2017').sheet1
results = sheet.cell(6,11)
pp.pprint(results)

row = ["I'm", "updating", "crap" ,"via" ,"python"]
index = 3
sheet.insert_row(row,index)
results = sheet.row_values(3)

pp.pprint(results)
sheet.update_cell(6,11,"555-555-5555")
results = sheet.cell(6,11)
