from flask import Flask
from flask_cors import CORS

from controller.crud_em_atendimento_controller import AtendimentoController
from controller.crud_fila_controller import CrudFilaController
from controller.gerar_pdf_controller import GerarPDFController
from controller.horarios_disponiveis_controller import HorariosDisponiveisMedicoController

app = Flask(__name__)
CORS(app)
crud_fila_controller = CrudFilaController()
atendimento_controller = AtendimentoController()
horarios_disponiveis_medico = HorariosDisponiveisMedicoController()
gerar_pdf_controller = GerarPDFController()

app.add_url_rule('/fila/inserir', view_func=crud_fila_controller.inserir_fila, methods=['POST'])
app.add_url_rule('/fila/update', view_func=crud_fila_controller.update_fila, methods=['PUT'])
app.add_url_rule('/fila/read/<string:codigo_medico>/<string:dia_mes_ano>/<string:codigo_paciente>', view_func=crud_fila_controller.read_posicao_fila, methods=['GET'])
app.add_url_rule('/fila/delete', view_func=crud_fila_controller.desmarcar_paciente_fila, methods=['DELETE'])

app.add_url_rule('/atendimento/inserir', view_func=atendimento_controller.inserir_em_atendimento, methods=['POST'])
app.add_url_rule('/atendimento/update', view_func=atendimento_controller.update_em_atendimento, methods=['PUT'])
app.add_url_rule('/atendimento/update/paciente-atendido', view_func=atendimento_controller.update_paciente_atendido, methods=['PUT'])
app.add_url_rule('/atendimento/read/<string:codigo_medico>/<string:dia_mes_ano>', view_func=atendimento_controller.read_paciente_em_atendimento, methods=['GET'])

app.add_url_rule('/horarios-disponiveis-medico/<string:codigo_medico>/<string:dia_mes_ano>', view_func=horarios_disponiveis_medico.horarios_disponiveis, methods=['GET'])

app.add_url_rule('/gerar-pdf', view_func=gerar_pdf_controller.gerar_pdf, methods=['POST'])

if __name__ == '__main__':
    app.run()