from services.disponibilidade_horarios import HorariosDisponiveisMedico


class HorariosDisponiveisMedicoFlow:

    def __init__(self):
        self.disponibilidade_horario = HorariosDisponiveisMedico()

    def horarios_disponiveis_medico(self,contexto):
        return self.disponibilidade_horario.horarios_disponiveis(contexto)