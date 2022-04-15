from repository.repository_em_atendimento import RepositoryEmAtendimento


class UpdatePacienteAtendidoFlow:

    def __init__(self):
        self.repository = RepositoryEmAtendimento()

    def update_paciente_atendido(self,contexto_paciente_atendido):
        self.repository.update_paciente_atendido(contexto_paciente_atendido)