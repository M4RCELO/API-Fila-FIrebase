from flow.inserir_paciente_fila import InserirPacienteNaFilaFlow
from flask import request

from flow.update_horario_paciente_fila import UpdateHorarioPacienteNaFilaFlow
from model.contexto_insert import ContextoInsert


class CrudFila:

    def __init__(self):
        self.inserir_na_fila = InserirPacienteNaFilaFlow()
        self.update_na_fila = UpdateHorarioPacienteNaFilaFlow()

    def inserir_fila(self):
        request_data = request.get_json()
        contexto_insert = ContextoInsert(
            codigo_medico=request_data['codigo_medico'],
            minuto=request_data['minuto'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            hora=request_data['hora']
        )
        self.inserir_na_fila.inserir(contexto_insert)
        return "OK"

    def update_fila(self):
        request_data = request.get_json()
        contexto_insert = ContextoInsert(
            codigo_medico=request_data['codigo_medico'],
            minuto=request_data['minuto'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            hora=request_data['hora']
        )
        self.update_na_fila.update_horario(contexto_insert)
        return "OK"