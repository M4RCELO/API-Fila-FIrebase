from services.gerar_pdf_service import GerarPDFService


class GerarPDFFlow:

    def __init__(self):
        self.gerar_pdf_service = GerarPDFService()

    def gerar_pdf(self, contexto):
        return self.gerar_pdf_service.gerar(contexto)