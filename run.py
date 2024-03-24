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
fruit_veg = SHEET.worksheet('fruit_veg')
dry_goods = SHEET.worksheet("dry_goods")
chilled_goods = SHEET.worksheet('chilled_goods')
frozen_items = SHEET.worksheet('frozen_items')

print("----------------------------------\n") # Welcome message
print("WELCOME TO STOCK-TRACE\n")
print("----------------------------------\n")

def main_menu():   # Main Menu
    print("----------------------------------\n")
    print("1. Current Stock")
    print("2. Input New Items")
    print("3. Use Stock Items\n")
    print("----------------------------------\n") 
    option = int(input("Please select an option from 1-3: \n")) # Input main menu options
    if option == 1:
        print("Current Stock:")
        submenu_current()
    elif option == 2:
        print("Input New Stock Items")
        input_new_menu()
    elif option == 3:
        print("Use Stock Items")
        use_stock_menu()
    else: 
        print("Invalid Choice. Please enter a number between 1 & 3\n ") # add letters as invalid choice
    
def submenu_current(): # Submenu for current stock
    while True:
        print("----------------------------------\n")
        print("1. Meat & Fish")
        print("2. Fruit & Veg")
        print("3. Dry Goods")
        print("4. Chilled Goods")
        print("5. Frozen Items")
        print("6. Return to Main Menu\n")
        print("----------------------------------\n")
        
        option = int(input("Please select an option from 1-6: \n")) # Input for submenu current stock
        
        if option == 1:
            print("----------------------------------")
            print("Meat & Fish")
            print("----------------------------------\n")
            data = meat_fish.get_all_values()
            for row in data:
                print("{:<30} {:<10} {:<10}".format(row[0], row[1], row[2]))
            input("Press any key to return to the Current Stock Menu\n ")
        elif option == 2:
            print("----------------------------------")
            print("Fruit & Veg")
            print("----------------------------------\n")
            data = fruit_veg.get_all_values()
            for row in data:
                print("{:<30} {:<10} {:<10}".format(row[0], row[1], row[2]))
            input("Press any key to return to the Current Stock Menu\n ")
        elif option == 3:
            print("----------------------------------")
            print("Dry Goods")
            print("----------------------------------\n")
            data = dry_goods.get_all_values()
            for row in data:
                print("{:<30} {:<10} {:<10}".format(row[0], row[1], row[2]))
            input("Press any key to return to the Current Stock Menu\n ")
        elif option == 4:
            print("----------------------------------")
            print("Chilled Goods")
            print("----------------------------------\n ")
            data = chilled_goods.get_all_values()
            for row in data:
                print("{:<30} {:<10} {:<10}".format(row[0], row[1], row[2]))
            input("Press any key to return to the Current Stock Menu\n ")
        elif option == 5:
            print("----------------------------------")
            print("Frozen Items")
            print("----------------------------------\n")
            data = frozen_items.get_all_values()
            for row in data:
                print("{:<30} {:<10} {:<10}".format(row[0], row[1], row[2]))
            input("Press any key to return to the Current Stock Menu\n ")
        elif option == 6:
            print("Return to Main Menu")
            main_menu()
            break
        else: 
            print("Invalid Choice. Please enter a number between 1 & 6: \n")
            
def input_new_menu():
    while True:
        print("----------------------------------\n")
        print("1. Meat & Fish")
        print("2. Fruit & Veg")
        print("3. Dry Goods")
        print("4. Chilled Goods")
        print("5. Frozen Items")
        print("6. Return to Main Menu")
        print("----------------------------------\n")
        
        option = input("Please select an option from 1-6: \n")
        
        if option == '1':
            add_stock(meat_fish)
        elif option == '2':
            add_stock(fruit_veg)
        elif option == '3':
            add_stock(dry_goods)
        elif option == '4':
            add_stock(chilled_goods)
        elif option == '5':
            add_stock(frozen_items)
        elif option == '6':
            print("Return to Main Menu")
            main_menu()
            break
        else:
            print("Invalid Choice. Please enter a number between 1 & 6\n ")
            
def add_stock(inventory_sheet):
    while True:
        item_name = input("Please enter item name, or type 'exit' to go back to menu: ").lower()  # Convert input to lowercase
        if item_name == "exit":
            return  # Exit the function if the user enters "exit"
        
        amount_to_add = int(input("Please enter the amount to add:\n "))
        
        cell = inventory_sheet.find(item_name)
        
        if cell:
            current_amount = int(inventory_sheet.cell(cell.row, cell.col + 2).value)
            
            new_amount = current_amount + amount_to_add
            
            inventory_sheet.update_cell(cell.row, cell.col + 2, new_amount)
            
            print(f"Added {amount_to_add} to {item_name}. New amount: {new_amount}")
        else:
            print(f"Item '{item_name}' not found in the category.")
    

      
def use_stock_menu():
    while True:
        print("----------------------------------\n")
        print("1. Meat & Fish")
        print("2. Fruit & Veg")
        print("3. Dry Goods")
        print("4. Chilled Goods")
        print("5. Frozen Items")
        print("6. Return to Main Menu")
        print("----------------------------------\n")
        
        option = input("Please select an option from 1-6:\n ")
        
        if option == '1':
            use_stock(meat_fish)
        elif option == '2':
            use_stock(fruit_veg)
        elif option == '3':
            use_stock(dry_goods)
        elif option == '4':
            use_stock(chilled_goods)
        elif option == '5':
            use_stock(frozen_items)
        elif option == '6':
            print("Return to Main Menu")
            main_menu()
            break
        else:
            print("Invalid Choice. Please enter a number between 1 & 6\n ")
            
def use_stock(inventory_sheet):
    while True:
        item_name = input("Please enter item name, or type 'exit' to go back to menu: ").lower()
        if item_name == "exit":
            return  # Exit the function if the user enters "exit"
        
        amount_to_use = int(input("Please enter the amount to use:\n "))
        
        cell = inventory_sheet.find(item_name)
        
        if cell:
            current_amount = int(inventory_sheet.cell(cell.row, cell.col + 2).value)
            
            if current_amount >= amount_to_use:
                new_amount = current_amount - amount_to_use
                inventory_sheet.update_cell(cell.row, cell.col + 2, new_amount)
                print(f"Used {amount_to_use} from {item_name}. New amount: {new_amount}")
            else:
                print("Error: Insufficient stock.")
        else:
            print(f"Item '{item_name}' not found in the category.")  
        
main_menu()

