import pdfkit

from services.inserir_no_driver import InserirDriveService


class GerarPDFService:

    def __init__(self):
        self.inserir_driver = InserirDriveService()

    def gerar(self, contexto):
        path_wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        name_path_download = "C:/Users/marce/Downloads/Receitas/" + contexto.codigo_medico + contexto.dia_mes_ano + contexto.codigo_paciente + ".pdf"

        html_initial = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            <br><br>
        """

        html_final = """
        </body>
        </html>
        """

        pdfkit.from_string(
            html_initial + contexto.html + html_final,
            name_path_download,
            configuration=config
        )

        return self.inserir_driver.inserir(contexto,name_path_download)
