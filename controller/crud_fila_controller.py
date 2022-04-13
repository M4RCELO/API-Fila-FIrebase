from flow.crud_fila.delete_paciente_fila import DeletePacienteNaFilaFlow
from flow.crud_fila.inserir_paciente_fila import InserirPacienteNaFilaFlow
from flask import request

from flow.crud_fila.read_posicao_fila import ReadPosicaoNaFilaFlow
from flow.crud_fila.update_horario_paciente_fila import UpdateHorarioPacienteNaFilaFlow
from model.contexto_insert import Contexto


class CrudFila:

    def __init__(self):
        self.inserir_na_fila = InserirPacienteNaFilaFlow()
        self.update_na_fila = UpdateHorarioPacienteNaFilaFlow()
        self.read_posicao_na_fila = ReadPosicaoNaFilaFlow()
        self.delete_paciente_na_fila = DeletePacienteNaFilaFlow()

    def inserir_fila(self):
        request_data = request.get_json()
        contexto_insert = Contexto(
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
        contexto_insert = Contexto(
            codigo_medico=request_data['codigo_medico'],
            minuto=request_data['minuto'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            hora=request_data['hora']
        )
        self.update_na_fila.update_horario(contexto_insert)
        return "OK"

    def read_posicao_fila(self, codigo_medico, dia_mes_ano, codigo_paciente):
        contexto = Contexto(
            codigo_medico=codigo_medico,
            dia_mes_ano=dia_mes_ano,
            codigo_paciente=codigo_paciente,
            hora=None,
            minuto=None
        )

        return self.read_posicao_na_fila.posicao_fila(contexto)

    def delete_paciente_fila(self):
        request_data = request.get_json()
        contexto_delete = Contexto(
            codigo_medico=request_data['codigo_medico'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            hora=None,
            minuto=None
        )

        self.delete_paciente_na_fila.delete_paciente(contexto_delete)

        return "OK"