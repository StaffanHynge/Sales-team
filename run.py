
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
    Check that the users name is one of the following in the list.
    if not print an error and the function loops.
    """
    
    expected_names = ['Tommy', 'Jennie', 'Sara', 'Michael', 'Fred', 'Louise']
    
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


get_user_name()


def get_num_meetings():

    num_meetings = int(input("Enter the number of meeting you´re going to have today: "))
    print(f"You have {num_meetings} meetings today")

get_num_meetings()
