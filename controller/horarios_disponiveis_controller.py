from flow.horario_disponivel_medico.horarios_disponiveis import HorariosDisponiveisMedicoFlow
from model.contexto_insert import Contexto


class HorariosDisponiveisMedicoController:

    def __init__(self):
        self.horarios_disponiveis_medico = HorariosDisponiveisMedicoFlow()

    def horarios_disponiveis(self,codigo_medico, dia_mes_ano):

        contexto = Contexto(
            codigo_medico=codigo_medico,
            dia_mes_ano=dia_mes_ano,
            codigo_paciente=None,
            hora=None,
            minuto=None
        )

        return self.horarios_disponiveis_medico.horarios_disponiveis_medico(contexto)
