from datetime import timedelta

from banco_dados.banco_dados_singleton import BancoDadosSingleton
from services.procurar_posicao import PosicaoFila


class Repository:

    def __init__(self):
        self.banco_dados = BancoDadosSingleton.instance()
        self.firebase = self.banco_dados.firebase
        self.posicao_fila = PosicaoFila()

    def inserir(self, contexto_insert):
        horario = timedelta(hours=contexto_insert.hora, minutes=contexto_insert.minuto)

        data = {
            'posicao': self.posicao_fila.posicao_no_insert(self.firebase, contexto_insert, horario.total_seconds()),
            'horario': horario
        }

        self.firebase.patch(
            str(contexto_insert.codigo_medico) + '/' +
            str(contexto_insert.dia_mes_ano) + '/' +
            'pacientes/' +
            str(contexto_insert.codigo_paciente),
            data
        )

    def update_horario(self, contexto_insert):
        horario = timedelta(hours=contexto_insert.hora, minutes=contexto_insert.minuto)

        data = {
            'horario': horario
        }

        self.firebase.patch(
            str(contexto_insert.codigo_medico) + '/' +
            str(contexto_insert.dia_mes_ano) + '/' +
            'pacientes/' +
            str(contexto_insert.codigo_paciente),
            data
        )

        self.posicao_fila.posicao_no_update(self.firebase, contexto_insert, horario.total_seconds())

    def read_posicao_fila(self, contexto):
        paciente = self.firebase.get(contexto.codigo_medico + '/' + contexto.dia_mes_ano + '/' +
                                     "pacientes/", contexto.codigo_paciente)

        return {'posicao': paciente['posicao']}

    def delete_paciente_fila(self, contexto):
        self.firebase.delete(contexto.codigo_medico + '/' + contexto.dia_mes_ano + '/' +
                             "pacientes/" + contexto.codigo_paciente, None)

        self.posicao_fila.posicao_apos_delete(self.firebase,contexto)
