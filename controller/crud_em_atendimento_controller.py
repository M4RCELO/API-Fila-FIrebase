from flask import request

from flow.atendimento.read_paciente_em_atendimento import ReadPacienteEmAtendimentoFlow
from flow.atendimento.update_atendido import UpdatePacienteAtendidoFlow
from flow.atendimento.update_em_atendimento import UpdateEmAtendimentoFlow
from model.contexto_insert import Contexto
from model.contexto_paciente_atendido import ContextoPacienteAtendido
from model.contexto_update_atendimento import ContextoUpdateAtendimento


class AtendimentoController:

    def __init__(self):
        self.update_atendimento = UpdateEmAtendimentoFlow()
        self.read_paciente_atendimento = ReadPacienteEmAtendimentoFlow()
        self.update_atendido = UpdatePacienteAtendidoFlow()

    def update_em_atendimento(self):
        request_data = request.get_json()
        contexto_update_em_atendimento = ContextoUpdateAtendimento(
            codigo_medico=request_data['codigo_medico'],
            dia_mes_ano=request_data['dia_mes_ano'],
            em_atendimento=request_data['em_atendimento']
        )
        self.update_atendimento.update(contexto_update_em_atendimento=contexto_update_em_atendimento)
        return "OK"

    def read_paciente_em_atendimento(self, codigo_medico, dia_mes_ano):
        contexto_em_atendimento = Contexto(
            codigo_medico=codigo_medico,
            dia_mes_ano=dia_mes_ano,
            codigo_paciente=None,
            hora=None,
            minuto=None
        )
        return self.read_paciente_atendimento.read_paciente_em_atendimento(contexto_em_atendimento)

    def update_paciente_atendido(self):
        request_data = request.get_json()
        contexto_paciente_atendido = ContextoPacienteAtendido(
            codigo_medico=request_data['codigo_medico'],
            dia_mes_ano=request_data['dia_mes_ano'],
            posicao_paciente_atendido=request_data['posicao_paciente_atendido']
        )
        self.update_atendido.update_paciente_atendido(contexto_paciente_atendido)
        return "OK"
