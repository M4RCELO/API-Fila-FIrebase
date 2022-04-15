from repository.repository import Repository


class DesmarcarPacienteNaFilaFlow:

    def __init__(self):
        self.repository = Repository()

    def desmarcar_paciente(self, contexto):
        self.repository.desmarcar_paciente_fila(contexto=contexto)