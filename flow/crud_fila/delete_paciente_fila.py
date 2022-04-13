from repository.repository import Repository


class DeletePacienteNaFilaFlow:

    def __init__(self):
        self.repository = Repository()

    def delete_paciente(self, contexto):
        self.repository.delete_paciente_fila(contexto=contexto)