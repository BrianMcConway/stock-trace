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
fruit_veg = SHEET.worksheet('fruit_veg')
data = meat_fish.get_all_values()
dry_goods = SHEET.worksheet("dry_goods")
data = dry_goods.get_all_values()
chilled_goods = SHEET.worksheet('chilled_goods')
data = chilled_goods.get_all_values()
frozen_items = SHEET.worksheet('frozen_items')
data = frozen_items.get_all_values()

#print(data)
print("----------------------------------\n") #Welcome message
print("WELCOME TO STOCK-TRACE\n")
print("----------------------------------\n")

def main_menu():   #Main Menu
    print("1. Current Stock")
    print("2. Input New Items")
    print("3. Use Stock Items\n")

    
    print("----------------------------------\n") 
    option = int(input("Please select an option from 1-3: \n")) #Input main menu options
    if option == 1:
        print("Current Stock:")
        submenu_current()
    elif option == 2:
        print("Input New Stock Items")
    elif option == 3:
        print("Use Stock Items")
    else: 
        print("Invalid Choice. Please enter a number between 1 & 3") #add letters as invalid choice
    
def submenu_current(): #Submenu for current stock
    while True:
        print("1. Meat & Fish")
        print("2. Fruit & Veg")
        print("3. Dry Goods")
        print("4. Chilled Goods")
        print("5. Frozen Items")
        print("6. Return to Main Menu")
        print("----------------------------------\n")
    
        option = int(input("Please select an option from 1-6: \n")) #Input for submenu current stock
        if option == 1:
            print("Meat & Fish")
            data = meat_fish.get_all_values()
            for row in data:
                print(row)
        elif option == 2:
            print("Fruit & Veg")
            data = fruit_veg.get_all_values()
            for row in data:
                print(row)
        elif option == 3:
            print("Dry Goods")
            data = dry_goods.get_all_values()
            for row in data:
                print(row)
        elif option == 4:
            print("Chilled Goods")
            data = chilled_goods.get_all_values()
            for row in data:
                print(row)
        elif option == 5:
            print("Frozen Items")
            data = frozen_items.get_all_values()
            for row in data:
                print(row)
        elif option == 6:
            print("Return to Main Menu") #check this function for menu being added to list
            main_menu()
            break
        else: 
            print("Invalid Choice. Please enter a number between 1 & 6")
         
main_menu()




