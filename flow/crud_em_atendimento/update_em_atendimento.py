from repository.repository_em_atendimento import RepositoryEmAtendimento


class UpdateEmAtendimentoFlow:

    def __init__(self):
        self.repository = RepositoryEmAtendimento()

    def update(self, contexto_update_em_atendimento):
        self.repository.update_em_atendimento(contexto_update_atendimento=contexto_update_em_atendimento)