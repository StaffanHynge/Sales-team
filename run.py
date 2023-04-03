
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


get_user_name()


def get_num_meetings():
    """
    Let the user insert how many he/she is having today
    If it´s more than one number, it displays an error and asks again
    If it´s not a number, it displays an error and asks again
    """
    while True:
        num_str= (input("Enter the number of meeting you´re going to have today: "))
        if num_str.isdigit():
            num = int(num_str)
            return num
        else:
            print("Invalid input. Please enter a single number.\n")

num = get_num_meetings()
if num:
    print(f"You have {num} meetings today.")
else:
    print("Invalid input. Try again")



def add_meeting_to_worksheet():
    """
    Add a new row to the meetings worksheet with the number of meetings for each team member
    """
    print("Adding a new row to the meetings worksheet...\n")
    
    # prompt user for the number of meetings to add
    num_meetings = get_num_meetings()
    print(f"You have {num_meetings} meetings today.\n")
    
    # get the meetings worksheet
    meetings_worksheet = SHEET.worksheet('meetings')

    # handle the case where the value is not a valid integer
    
    # loop through each team member and update their meeting count
    for i, name in enumerate(expected_names):
        col_index = i + 1
        count = int(meetings_worksheet.cell(1, col_index).value) + num_meetings
        meetings_worksheet.update_cell(1, col_index, count)

    print("Row added successfully.")

add_meeting_to_worksheet()