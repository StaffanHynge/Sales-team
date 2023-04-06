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


expected_names = ['TOMMY', 'JENNIE', 'SARA', 'MICHAEL', 'FRED']


def get_user_name():
    """
    Get the user name.
    Check that the users name is one of the following in the list.
    if not print an error and the function loops.
    """
    print("Please enter your name.")
    print(f"Your name should be one of: {', '.join(expected_names)}\n")
    while True:

        data_str = input("Enter your name here:\n ").upper()
        print(f"Your name is {data_str}")

        if data_str in expected_names:
            print("Welcome!")
            return data_str
        else:
            print(f"Access Denied. Choose from: {', '.join(expected_names)}\n")


data_str = get_user_name()


def get_num_sales():
    """
    Let the user insert how many he/she is having today
    If it´s more than one number, it displays an error and asks again
    If it´s not a number, it displays an error and asks again
    """
    while True:
        num_str = (input("Enter the number of sales you´ve had today:\n "))
        if num_str.isdigit():
            num = int(num_str)
            return num
        else:
            print("Invalid input. Please enter a single number.\n")


num = get_num_sales()
if num:
    print(f"You have {num} sales today.")


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

    if num <= 10:
        num *= 10
        print("You get 10 euros for your first 10 units sold.")
    elif num <= 20:
        num_10 = 10 * 10
        num_11_20 = (num - 10) * 15
        num = num_10 + num_11_20
        print("You get 15 euros for your second 10 units sold.")
    else:
        num_10 = 10 * 10
        num_11_20 = 10 * 15
        num_inf = (num - 20) * 20
        num = num_10 + num_11_20 + num_inf
        print("You get 20 euros for unit number 21 and so on.")

    salary_worksheet = SHEET.worksheet('salary')
    salary_worksheet.append_row([num])
    print(f"You earned {num} euros today.")


update_salary_worksheet(num)


def update_products_worksheet(num):
    """
    Update Products worksheet, add new row with the list data provided
    """

    remaining = 10 - num
    if num >= 10:
        print("Great work! You've reached your sales goal of 10 units sold.")
    else:
        print(f"You need to sell {remaining} more units to reach your goal.")

    print("Thank you. Have a nice day")

    products_worksheet = SHEET.worksheet('goal')
    products_worksheet.append_row([remaining])


update_products_worksheet(num)
