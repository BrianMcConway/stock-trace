import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('stock-trace')

meat_fish = SHEET.worksheet('meat_fish')

data = meat_fish.get_all_values()

#print(data)
2
def menu():
    print("[1] Current Stock")
    print("[2] Input New Items")
    print("[3] Use Stock Items")
    print("[4] Exit\n")

menu()
option = int(input("Please select an option from 1-4\n"))



