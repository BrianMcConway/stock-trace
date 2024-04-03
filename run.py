import gspread
from google.oauth2.service_account import Credentials
import os
from patterns import PATTERNS

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


#OS to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




# Function to build a word using the patterns
def build_word(word):
    for i in range(5):  # Iterate over each line of the word
        line = ''
        for letter in word:
            pattern = PATTERNS[letter.lower()]
            line += pattern[i] + '  '  # Add spaces between letters
        print(line)


# Welcome message
def welcome_message():
    clear_screen()
    
    print("--------------------------------------------------\n")

    words = ["Stock", "Trace"]

    for word in words:
        build_word(word)
        
        print()  # Add an empty line between words

    print("--------------------------------------------------\n")
    print("WELCOME TO STOCK TRACE\n")
    print("--------------------------------------------------\n")

    input("Press Enter to go to the main menu\n")




# Main Menu
def main_menu():
    clear_screen()
    print("--------------------------------------------------\n")
    print("1. Current Stock")
    print("2. Input New Items")
    print("3. Use Stock Items\n")
    print("--------------------------------------------------\n")
    
    while True:
        # Input main menu options
        option = input("Please select an option from 1-3:\n").strip()  # Trim leading and trailing whitespace
        
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 3:
                break
            else:
                print("Invalid Input!\n Please enter a number between 1 & 3\n")
        else:
            print("Invalid Input!\n Please enter a number between 1 & 3\n")

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
        print("Invalid Choice!\n Please enter a number between 1 & 3\n")


# Submenu for current stock
def submenu_current():
    clear_screen()
    print("----------------------------------\n")
    print("1. Meat & Fish")
    print("2. Fruit & Veg")
    print("3. Dry Goods")
    print("4. Chilled Goods")
    print("5. Frozen Items")
    print("6. Return to Main Menu\n")
    print("----------------------------------\n")

    while True: 
        option = input("Please select an option from 1-6:\n").strip() 

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 6:
                if option == 1:
                    clear_screen()
                    menu_category("Meat & Fish", meat_fish)
                elif option == 2:
                    clear_screen()
                    menu_category("Fruit & Veg", fruit_veg)
                elif option == 3:
                    clear_screen()
                    menu_category("Dry Goods", dry_goods)
                elif option == 4:
                    clear_screen()
                    menu_category("Chilled Goods", chilled_goods)
                elif option == 5:
                    clear_screen()
                    menu_category("Frozen Items", frozen_items)
                elif option == 6:
                    clear_screen()
                    main_menu()
                    break
            else:
                print("Invalid Input!\nPlease enter a number between 1 and 6.\n")
        else:
            print("Invalid Input!\nPlease enter a number between 1 and 6.\n")

# Helper function to display category data
def menu_category(category_name, category_sheet):
    clear_screen()
    print("----------------------------------")
    print(category_name)
    print("----------------------------------\n")
    data = category_sheet.get_all_values()
    for row in data:
        print("{:<20} {:<20} {:<10}".format(row[0], row[1], row[2]))
    print("----------------------------------\n")
    input("Press 'Enter' to return to the Current Stock Menu\n")
    submenu_current()  # Display the submenu current menu after pressing Enter
    clear_screen()
    


def input_new_menu():
    clear_screen()
    print("--------------------------------------------------")
    print("Input New Items")
    print("--------------------------------------------------\n")
    print("1. Meat & Fish")
    print("2. Fruit & Veg")
    print("3. Dry Goods")
    print("4. Chilled Goods")
    print("5. Frozen Items")
    print("6. Return to Main Menu")
    print("--------------------------------------------------\n")

    while True:
        option = input("Please select an option from 1-6:\n").strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 6:
                if option == 1:
                    add_stock(meat_fish, "Meat & Fish")
                elif option == 2:
                    add_stock(fruit_veg, "Fruit & Veg")
                elif option == 3:
                    add_stock(dry_goods, "Dry Goods")
                elif option == 4:
                    add_stock(chilled_goods, "Chilled Goods")
                elif option == 5:
                    add_stock(frozen_items, "Frozen Items")
                elif option == 6:
                    print("Returning to Main Menu")
                    main_menu()
                    break
            else:
                print("Invalid Choice. Please enter a number between 1 & 6\n")
        else:
            print("Invalid Input. Please enter a valid number between 1 & 6\n")

def add_stock(inventory_sheet, category_name):
    
        clear_screen()
        print("--------------------------------------------------")
        print("Input New Items")
        print("--------------------------------------------------\n")
        while True:
            item_name = input(f"Please enter {category_name} item name, or type 'exit' to go back to the menu:\n").lower()
            if item_name == "exit":
                input_new_menu()  # Display the menu again after exiting add_stock
                return  # Exit the function if the user enters "exit"

            amount_to_add = input("Please enter the amount to add:\n").strip()

            if amount_to_add.isdigit():
                amount_to_add = int(amount_to_add)
                cell = inventory_sheet.find(item_name)
                if cell:
                    current_amount = int(inventory_sheet.cell(cell.row, cell.col + 2).value)
                    new_amount = current_amount + amount_to_add
                    inventory_sheet.update_cell(cell.row, cell.col + 2, new_amount)
                    print(f"Added {amount_to_add} to {item_name}. New amount: {new_amount}")
                else:
                    print(f"Item '{item_name}' not found in the category.")
            elif amount_to_add.lower() == "exit":
                input_new_menu()  # Display the menu again after exiting add_stock
                return  # Exit the function if the user enters "exit"
            else:
                print("Invalid input for amount. Please enter a valid number.")



def use_stock_menu():
    clear_screen()
    print("--------------------------------------------------")
    print("Use Stock Items")
    print("--------------------------------------------------\n")
    print("1. Meat & Fish")
    print("2. Fruit & Veg")
    print("3. Dry Goods")
    print("4. Chilled Goods")
    print("5. Frozen Items")
    print("6. Return to Main Menu")
    print("--------------------------------------------------\n")

    while True:
        option = input("Please select an option from 1-6:\n").strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 6:
                if option == 1:
                    use_stock(meat_fish, "Meat & Fish")
                elif option == 2:
                    use_stock(fruit_veg, "Fruit & Veg")
                elif option == 3:
                    use_stock(dry_goods, "Dry Goods")
                elif option == 4:
                    use_stock(chilled_goods, "Chilled Goods")
                elif option == 5:
                    use_stock(frozen_items, "Frozen Items")
                elif option == 6:
                    print("Returning to Main Menu")
                    main_menu()
                    return
            else:
                print("Invalid Choice. Please enter a number between 1 & 6:\n")
        else:
            print("Invalid Input. Please enter a valid number between 1 & 6:\n")


def use_stock(inventory_sheet, category_name):
    
        clear_screen()
        print("--------------------------------------------------")
        print("Use Stock Items")
        print("--------------------------------------------------\n")
        while True:
            item_name = input(f"Please enter {category_name} item name, or type 'exit' to go back to menu:\n").lower()
            if item_name == "exit":
                use_stock_menu()  # Display the menu again after exiting use_stock
                return  # Exit the function if the user enters "exit"

            amount_to_use = input("Please enter the amount to use:\n")

            if amount_to_use.isdigit():
                amount_to_use = int(amount_to_use)
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
            elif amount_to_use.lower() == "exit":
                use_stock_menu()  # Display the menu again after exiting use_stock
                return  # Exit the function if the user enters "exit"
            else:
                print("Invalid input for amount. Please enter a valid number.")



if __name__ == '__main__':
    welcome_message()
    main_menu()

