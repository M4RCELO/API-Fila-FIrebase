from repository.repository_em_atendimento import RepositoryEmAtendimento


class UpdateEmAtendimentoFlow:

    def update(self, contexto_update_em_atendimento):
        repository = RepositoryEmAtendimento()
        repository.update_em_atendimento(contexto_update_atendimento=contexto_update_em_atendimento)