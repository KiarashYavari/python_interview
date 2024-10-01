# https://docs.google.com/spreadsheets/d/1w_D7eAjM23BmKI8paWIBXBRc0hrHJXDnclLa2KI8Vus/edit?usp=sharing

from googleapiclient.discovery import build
from authentication import authenticate


def read_spreadsheet_id(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read().strip()
    
# The ID and range of the spreadsheet.
SPREADSHEET_ID = read_spreadsheet_id('spreadsheet_id.txt')
RANGE_NAME = 'Sheet1!A1:D'


# Create a service object
creds = authenticate()
service = build('sheets', 'v4', credentials=creds)

# Call google sheet API to operate read or write on it
sheet = service.spreadsheets()

def add_item(sheet: object, item_id: str, item_name: str, quantity: int, price: float) -> None:
    values = [
        [item_id, item_name, quantity, price]
    ]
    body = {
        'values': values
    }
    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID, 
        range=RANGE_NAME, 
        valueInputOption='USER_ENTERED', 
        body=body
    ).execute()
    print(f"{result.get('updates').get('updatedCells')} cells appended.")

# Add a new item
# add_item(sheet, '007', 'planner 25-26', 75, 1.50)

def read_inventory(sheet: object) -> None:
    
    # it will return the response of google API in dictionary type format
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    # result --> {'range': 'Sheet1!A1:D1000', 'majorDimension': 'ROWS', 'values': [['4', 'Notebook', '50', '2.5'], ['5', 'Pencils', '100', '0.75'], ['6', 'pen', '100', '1']]}
    # save the values key from google API response dictionary, if no values key then []
    rows = result.get('values', [])
    if not rows:
        print('No data found.')
    else:
        print('Inventory data:')
        for row in rows:
            print(row)

# Call the function to read data
read_inventory(sheet)
