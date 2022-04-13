from repository.repository_em_atendimento import RepositoryEmAtendimento


class ReadPacienteEmAtendimentoFlow:

    def __init__(self):
        self.repository = RepositoryEmAtendimento()

    def read_paciente_em_atendimento(self,contexto):
        return self.repository.read_em_atendimento(contexto)