from flask import request

from flow.update_em_atendimento import UpdateEmAtendimentoFlow
from model.contexto_update_atendimento import ContextoUpdateAtendimento


class CrudEmAtendimento:

    def __init__(self):
        self.update_atendimento = UpdateEmAtendimentoFlow()

    def update_em_atendimento(self):
        request_data = request.get_json()
        contexto_update_em_atendimento = ContextoUpdateAtendimento(
            codigo_medico= request_data['codigo_medico'],
            dia_mes_ano= request_data['dia_mes_ano'],
            em_atendimento=request_data['em_atendimento']
        )
        self.update_atendimento.update(contexto_update_em_atendimento=contexto_update_em_atendimento)
        return "OK"