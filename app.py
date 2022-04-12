from flask import Flask

from controller.crud_em_atendimento import CrudEmAtendimento
from controller.crud_fila_controller import CrudFila

app = Flask(__name__)
crud = CrudFila()
crud_em_atendimento = CrudEmAtendimento()

app.add_url_rule('/fila/inserir', view_func=crud.inserir_fila, methods=['POST'])
app.add_url_rule('/fila/update', view_func=crud.update_fila, methods=['POST'])
app.add_url_rule('/atendimento/update', view_func=crud_em_atendimento.update_em_atendimento, methods=['POST'])

if __name__ == '__main__':
    app.run()