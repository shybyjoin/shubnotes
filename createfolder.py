from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERION,SCOPES)

folders = [ 'shub_folder']

for folder in folders:
        file_metadata = {
                'name': folder,
                'mimeType' : 'application/vnd.google-apps.folder'
        # ' parents': []
        }
        service.files().create(body=file_metadata).execute()


