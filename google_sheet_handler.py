from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

scopes = ['https://www.googleapis.com/auth/spreadsheets']
# Replace CLIENT_ID and CLIENT_SECRET with the values of your OAuth 2.0 client ID and client secret, respectively
creds = Credentials.from_authorized_user_info(info={'client_id': 'CLIENT_ID', 'client_secret': 'CLIENT'}, scopes=scopes)

# Now you can use the creds object to authenticate your requests to the Google API

service = build('sheets', 'v4', credentials=creds)

# Define the spreadsheet and range to read
spreadsheet_id = '1SMKobKXfK5time-GNDiIY8nKEKJ_mTf8l1CVPf7r1wI'
range_name = 'Sommar2023!A1:MK43'

# Call the Sheets API to read the data
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])

# Print the data to the console
print(values)