from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from chuck_pyutils import core as utils

config = utils.read_config(utils.get_file_path(__file__, 'config.ini'))
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = config['GOOGLE']['SPREADSHEET_ID']
ROW_NUM = 5
SAMPLE_RANGE_NAME = f'A{ROW_NUM}:K{ROW_NUM}'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(values)
        for cell in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(f"Taco Name: {cell[1]}\nPlace: {cell[0]}\nPrice per taco: ${cell[2]}\nMain Protein: {cell[4]}\nHard or soft shell: {cell[5]}\nFlour or corn shell: {cell[6]}\nRating out of 5 stars: {cell[7]}\nBest part: {cell[8]}\nIngredients: {cell[9]}\nSpice level (none, mild, medium, hot): {cell[10]}")

if __name__ == '__main__':
    main()