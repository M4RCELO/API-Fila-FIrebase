from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class InserirDriveService:

    def __init__(self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile("mycreds.txt")

        self.drive = GoogleDrive(gauth)

    def inserir(self, contexto, path_download):

        data_folders = {}
        folders = []
        id_folders = {}

        file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for i in range(len(file_list)):
            data_folders[file_list[i]['title']] = {'id': file_list[i]['id']}

        for i in data_folders:
            str = "\'" + data_folders[i]['id'] + "\'" + " in parents and trashed=false"
            file_list = self.drive.ListFile({'q': str}).GetList()
            for file in file_list:
                folders.append(file['title'])
                id_folders[file['title']] = {'id': file['id']}

            data_folders[i]['folders'] = folders

        codigo_medico = contexto.codigo_medico
        dia_mes_ano = contexto.dia_mes_ano

        if codigo_medico not in data_folders:
            folder_doctor = self.drive.CreateFile(
                {'title': codigo_medico, 'mimeType': 'application/vnd.google-apps.folder'})
            folder_doctor.Upload()
            parent_id_doctor = folder_doctor['id']

            folder_day = self.drive.CreateFile({'title': dia_mes_ano, 'parents': [{'id': parent_id_doctor}],
                                                'mimeType': 'application/vnd.google-apps.folder'})
            folder_day.Upload()
            parent_id_day = folder_day['id']

        else:
            parent_id_doctor = data_folders[codigo_medico]['id']

            if dia_mes_ano not in data_folders[codigo_medico]['folders']:

                folder_day = self.drive.CreateFile({'title': dia_mes_ano, 'parents': [{'id': parent_id_doctor}],
                                                    'mimeType': 'application/vnd.google-apps.folder'})
                folder_day.Upload()
                parent_id_day = folder_day['id']

            else:
                parent_id_day = id_folders[dia_mes_ano]['id']

        file_pdf = self.drive.CreateFile({'title': contexto.codigo_paciente, 'parents': [{'id': parent_id_day}]})
        file_pdf.SetContentFile(path_download)
        file_pdf.Upload(param={'supportsTeamDrives': True})

        body_permissions = {
            'id': 'anyoneWithLink',
            'type': 'anyone',
            'value': 'anyoneWithLink',
            'withLink': True,
            'role': 'reader'
        }

        file_pdf.auth.service.permissions().insert(
            fileId = file_pdf['id'], body = body_permissions, supportsTeamDrives=True
        ).execute(http=file_pdf.http)

        return "https://drive.google.com/file/d/" + file_pdf['id'] + "/view?usp=sharing"
