from repository.repository import Repository


class InserirPacienteNaFilaFlow:

    def inserir(self, contexto_insert):
        repository = Repository()
        repository.inserir(contexto_insert=contexto_insert)
