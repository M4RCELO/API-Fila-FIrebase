from repository.repository_em_atendimento import RepositoryEmAtendimento


class InserirAtendimentoFlow:

    def __init__(self):
        self.repository = RepositoryEmAtendimento()

    def inserir(self, contexto_inserir_atendimento):
        self.repository.inserir_atendimento(contexto=contexto_inserir_atendimento)
