from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'], label['id'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

    request = {
        'labelIds': ['Label_3051323260890540466'],
        'topicName': 'projects/home-k3s-329518/topics/Kindle-highlights'
    }
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        # r = service.users().watch(userId='me', body=request).execute()
        # r = service.users().history().list(userId='me', startHistoryId="5349388").execute()
        # r = service.users().messages().get(userId='me', id="17e85be320e555d2").execute()
        r = service.users().messages().attachments().get(userId='me', messageId="17e85be320e555d2",
                                                         id="ANGjdJ_fXteM5CCNWmad7iTzoGGNTmaGZBeg3erFUubeXlaDWOdT39U6sVhS2S233T_TdsDMRLBM3qjZWmH4ZeEoxfiqt7SdWwpwInwL2FU0Auwf0YKzrZMksQNXONrMJwHltNoUpb1ZpLqP_wQv48WPk3NfmfOw0Ep1MsiRp0QNGfqDdDiSsjZ4ekzb2o7GZDLfpSxJq6BIJTFViB7rJzvntvz1lYM1F1eYJUywFlBCnj23uPPc4T_FInolStcKCaSrwQLcuyvmpTt5BWf2-XQR2z4i5SK8MoMSLZE-7wOth-xLJr30qc-2i-65yEyrjTc5jj28Lw39Frv-MbJ2n_gHqpql7BUwBe6JtBON0MhUTla9Zd42mhlB5fz9WRs").execute()

# .replace(/_/g, '/').replace(/-/g, '+')
        print(base64.b64decode(r.get("data").replace("_", "/").replace("-", "+")))

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
