from flow.fila.delete_paciente_fila import DesmarcarPacienteNaFilaFlow
from flow.fila.inserir_paciente_fila import InserirPacienteNaFilaFlow
from flask import request

from flow.fila.read_posicao_fila import ReadPosicaoNaFilaFlow
from flow.fila.update_horario_paciente_fila import UpdateHorarioPacienteNaFilaFlow
from model.contexto_insert import Contexto


class CrudFilaController:

    def __init__(self):
        self.inserir_na_fila = InserirPacienteNaFilaFlow()
        self.update_na_fila = UpdateHorarioPacienteNaFilaFlow()
        self.read_posicao_na_fila = ReadPosicaoNaFilaFlow()
        self.desmarcar_paciente_na_fila = DesmarcarPacienteNaFilaFlow()

    def inserir_fila(self):
        request_data = request.get_json()
        contexto_insert = Contexto(
            codigo_medico=request_data['codigo_medico'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            hora=request_data['hora'],
            minuto=request_data['minuto']
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

    def desmarcar_paciente_fila(self):
        request_data = request.get_json()
        contexto_delete = Contexto(
            codigo_medico=request_data['codigo_medico'],
            dia_mes_ano=request_data['dia_mes_ano'],
            codigo_paciente=request_data['codigo_paciente'],
            hora=None,
            minuto=None
        )

        self.desmarcar_paciente_na_fila.desmarcar_paciente(contexto_delete)

        return "OK"
