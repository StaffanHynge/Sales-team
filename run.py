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
SHEET = GSPREAD_CLIENT.open('sales-team')


expected_names = ['Tommy', 'Jennie', 'Sara', 'Michael', 'Fred', 'Louise']

def get_user_name():
    """
    Get the user name.
    Check that the users name is one of the following in the list.
    if not print an error and the function loops.
    """
    print("Please enter your name.")
    print(f"Your name should be one of the following: {', '.join(expected_names)}\n")
    while True:

        data_str = input("Enter your name here: ")
        print(f"Your name is {data_str}")

        if data_str in expected_names:
            print("Welcome!")
            return data_str
        else:
            print(f"Access Denied. Your name should be one of the following: {', '.join(expected_names)}\n")

data_str = get_user_name()

def get_num_sales():
    """
    Let the user insert how many he/she is having today
    If it´s more than one number, it displays an error and asks again
    If it´s not a number, it displays an error and asks again
    """
    while True:
        num_str= (input("Enter the number of sales you´re going to have today: "))
        if num_str.isdigit():
            num = int(num_str)
            return num
        else:
            print("Invalid input. Please enter a single number.\n")

num = get_num_sales()
if num:
    print(f"You have {num} sales today.")
else:
    print("Invalid input. Try again")

    # Är något på spåren här

def update_sales_worksheet(data_str, num):
    """
    Update sales worksheet, add new row with the list data provided
    """

    sales_worksheet = SHEET.worksheet('sales')
    row = [data_str, num]
    sales_worksheet.append_row(row)

update_sales_worksheet(data_str, num)

def update_salary_worksheet(num):
    """
    Update Salary worksheet, add new row with the list data provided
    """

    # Multiply num 
    if num <= 10:
        num *= 10
        print("You sold up to 10 units. Your earning is multiplied by 10.")
    elif num <= 20:
        num_10 = 10 * 10
        num_11_20 = (num - 10) * 15
        num = num_10 + num_11_20
        print("You sold up to 20 units. Your earnings for first 10 units is multiplied by 10, and for the next 10 units it is multiplied by 15.")
    else:
        num_10 = 10 * 10
        num_11_20 = 10 * 15
        num_inf = (num - 20) * 20
        num = num_10 + num_11_20 + num_inf
        print("You sold more than 20 units. Your earnings for first 10 units is multiplied by 10, for the next 10 units it is multiplied by 15, and for all units greater than 20 it is multiplied by 20.")

    salary_worksheet = SHEET.worksheet('salary')
    salary_worksheet.append_row([num])
    print(f"You earned {num} euros today.")

update_salary_worksheet(num)

def update_products_worksheet(num):
    """
    Update Products worksheet, add new row with the list data provided
    """
    # 100 - num
    num = abs(100 - num)

    products_worksheet = SHEET.worksheet('products')
    products_worksheet.append_row([num])
    print(f"We have {num} products left in the store.")

update_products_worksheet(num)