from Google import Create_Service
from googleapiclient.http import MediaFileUpload


CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERION,SCOPES)

folder_id = '*folderid*'
file_names = ['folder_name.jpg']
mime_types = ['image/jpeg']

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload('./partition/{0}'.format(file_name), mimetype=mime_type, resumable= True)
   
    service.files().create(
       body=file_metadata,
       media_body = media,
       fields= 'id'
   ).execute()
    
    
   
