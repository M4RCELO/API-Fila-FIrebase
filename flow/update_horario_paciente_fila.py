from repository.repository import Repository


class UpdateHorarioPacienteNaFilaFlow:

    def update_horario(self, contexto_insert):
        repository = Repository()
        repository.update_horario(contexto_insert=contexto_insert)
