from flask import Flask

from controller.crud_em_atendimento_controller import CrudEmAtendimentoController
from controller.crud_fila_controller import CrudFilaController
from controller.horarios_disponiveis_controller import HorariosDisponiveisMedicoController

app = Flask(__name__)
crud = CrudFilaController()
crud_em_atendimento = CrudEmAtendimentoController()
horarios_disponiveis_medico = HorariosDisponiveisMedicoController()

app.add_url_rule('/fila/inserir', view_func=crud.inserir_fila, methods=['POST'])
app.add_url_rule('/fila/update', view_func=crud.update_fila, methods=['PUT'])
app.add_url_rule('/fila/read/<string:codigo_medico>/<string:dia_mes_ano>/<string:codigo_paciente>', view_func=crud.read_posicao_fila, methods=['GET'])
app.add_url_rule('/fila/delete', view_func=crud.desmarcar_paciente_fila, methods=['DELETE'])

app.add_url_rule('/atendimento/update', view_func=crud_em_atendimento.update_em_atendimento, methods=['PUT'])
app.add_url_rule('/atendimento/read/<string:codigo_medico>/<string:dia_mes_ano>', view_func=crud_em_atendimento.read_paciente_em_atendimento, methods=['GET'])
app.add_url_rule('/atendimento/update/paciente-atendido', view_func=crud_em_atendimento.update_paciente_atendido, methods=['POST'])
#atendimento/read/paciente-atendido/<string:codigo_medico>/<string:dia_mes_ano>/<string:codigo_paciente>
#jogar toda responsabilidade da fila para API, quando a recepcionista clicar em okay. Passar para o proximo paciente

app.add_url_rule('/horarios-disponiveis-medico/<string:codigo_medico>/<string:dia_mes_ano>', view_func=horarios_disponiveis_medico.horarios_disponiveis, methods=['GET'])

if __name__ == '__main__':
    app.run()