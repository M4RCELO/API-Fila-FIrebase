from flow.gerar_pdf.gerar_pdf import GerarPDFFlow
from model.contexto_gerar_pdf import ContextoGerarPDF
from flask import request


class GerarPDFController:

    def __init__(self):
        self.gerar_pdf_flow = GerarPDFFlow()

    def gerar_pdf(self):
        request_data = request.get_json()
        contexto_gerar_pdf = ContextoGerarPDF(
            codigo_medico=request_data['codigo_medico'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            html=request_data['html']
        )

        return self.gerar_pdf_flow.gerar_pdf(contexto_gerar_pdf)
