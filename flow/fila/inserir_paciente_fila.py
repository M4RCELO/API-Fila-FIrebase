from repository.repository import Repository


class InserirPacienteNaFilaFlow:

    def __init__(self):
        self.repository = Repository()

    def inserir(self, contexto_insert):
        self.repository.inserir(contexto_insert=contexto_insert)
