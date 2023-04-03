
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

def get_user_name():
    """
    Get the user name.
    """
    print("Please enter your name.")
    print("Your name should be one of the following.")
    print("Tommy, Jennie, Sara, Michael, Fred, Louise\n")

    data_str = input("Enter your name here: ")
    print(f"Your name is {data_str}")


get_user_name()
