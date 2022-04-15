from repository.repository import Repository


class ReadPosicaoNaFilaFlow:

    def __init__(self):
        self.repository = Repository()

    def posicao_fila(self,contexto):
        return self.repository.read_posicao_fila(contexto=contexto)
