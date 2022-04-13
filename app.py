from flask import Flask

from controller.crud_em_atendimento import CrudEmAtendimento
from controller.crud_fila_controller import CrudFila

app = Flask(__name__)
crud = CrudFila()
crud_em_atendimento = CrudEmAtendimento()

app.add_url_rule('/fila/inserir', view_func=crud.inserir_fila, methods=['POST'])
app.add_url_rule('/fila/update', view_func=crud.update_fila, methods=['PUT'])
app.add_url_rule('/fila/read/<string:codigo_medico>/<string:dia_mes_ano>/<string:codigo_paciente>', view_func=crud.read_posicao_fila, methods=['GET'])
app.add_url_rule('/fila/delete', view_func=crud.delete_paciente_fila, methods=['DELETE'])

app.add_url_rule('/atendimento/update', view_func=crud_em_atendimento.update_em_atendimento, methods=['PUT'])
app.add_url_rule('/atendimento/read/<string:codigo_medico>/<string:dia_mes_ano>', view_func=crud_em_atendimento.read_paciente_em_atendimento, methods=['GET'])

if __name__ == '__main__':
    app.run()