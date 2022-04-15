from repository.repository import Repository


class UpdateHorarioPacienteNaFilaFlow:

    def __init__(self):
        self.repository = Repository()

    def update_horario(self, contexto_insert):
        self.repository.update_horario(contexto_insert=contexto_insert)
