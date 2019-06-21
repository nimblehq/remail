from __future__ import print_function

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from googleapiclient.discovery import build

from remail import auth


class Gmail():
    def __init__(self):
        self.service = build('gmail', 'v1', credentials=auth.get_gmail_credentials())
        super().__init__()

    def create_text_draft(self, to, cc, subject, message_text):
        message = MIMEText(message_text, 'html')
        message['to'] = to
        message['cc'] = cc
        message['from'] = "me"
        message['subject'] = subject
        encoded_msg = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

        body = {'message': encoded_msg}

        self.service.users().drafts().create(userId="me", body=body).execute()

    def create_html_draft(self, to, cc, subject, message_html):
        message = MIMEMultipart('alternative')
        message['to'] = to
        message['cc'] = cc
        message['from'] = "me"
        message['subject'] = subject
        message.attach(MIMEText(message_html, 'html'))
        encoded_msg = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

        body = {'message': encoded_msg}

        self.service.users().drafts().create(userId="me", body=body).execute()
