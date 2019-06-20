from __future__ import print_function

import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build

from remail import auth


class Gmail():
    def __init__(self):
        self.service = build('gmail', 'v1', credentials=auth.get_gmail_credentials())
        super().__init__()

    def create_draft(self, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = "me"
        message['subject'] = subject

        message_body = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
        message = {'message': message_body}

        self.service.users().drafts().create(userId="me", body=message).execute()
