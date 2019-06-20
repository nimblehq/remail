from __future__ import print_function

from googleapiclient.discovery import build

from remail import auth


class Gdrive():
    def __init__(self):
        self.service = build('drive', 'v3', credentials=auth.get_gdrive_credentials())
        super().__init__()

    def get_release_folder(self):
        folder = None
        page_token = None
        while True:
            response = self.service.files().list(
                q="mimeType = 'application/vnd.google-apps.folder' and name = '2.19.0'",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                if file.get('name') == '2.19.0':
                    folder = file
                    break

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

        return folder.get('id')

    def create_beta_folder(self, parent_id, beta):
        file_metadata = {
            'name': 'Beta%s' % beta,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_id]
        }
        folder = self.service.files().create(body=file_metadata,
                                             fields='id').execute()

        return folder.get('id')

    def get_beta_folder_link(self, file_id):
        user_permission = {
            'role': 'reader',
            'type': 'anyone'
        }
        self.service.permissions().create(fileId=file_id,
                                          body=user_permission).execute()
        folder = self.service.files().get(fileId=file_id,
                                          fields='webViewLink').execute()

        return folder.get('webViewLink')
