from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

CREDENTIALS_JSON = '../remail/credentials.json'

GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
GMAIL_PICKLE = '../remail/gmail.pickle'

GDRIVE_SCOPES = ['https://www.googleapis.com/auth/drive']
GDRIVE_PICKLE = '../remail/drive.pickle'


def get_credentials(scopes, pickle_file):
    credentials = None

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_JSON, scopes)
            credentials = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(credentials, token)

    return credentials


def get_gmail_credentials():
    return get_credentials(GMAIL_SCOPES, GMAIL_PICKLE)


def get_gdrive_credentials():
    return get_credentials(GDRIVE_SCOPES, GDRIVE_PICKLE)
