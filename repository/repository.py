from datetime import timedelta

from banco_dados.firestore_database_singleton import FirestoreDatabaseSingleton
from banco_dados.realtime_database_singleton import RealtimeDatabaseSingleton
from services.procurar_posicao import PosicaoFila


class Repository:

    def __init__(self):
        self.firebase = RealtimeDatabaseSingleton.instance().firebase
        self.db = FirestoreDatabaseSingleton.instance().db
        self.posicao_fila = PosicaoFila(self.firebase)

    def inserir(self, contexto_insert):
        horario = timedelta(hours=contexto_insert.hora, minutes=contexto_insert.minuto)

        data = {
            'atendido': False,
            'horario': horario,
            'posicao': self.posicao_fila.posicao_no_insert(contexto_insert, horario.total_seconds())
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

        self.posicao_fila.posicao_no_update(contexto_insert, horario.total_seconds())

    def read_posicao_fila(self, contexto):
        paciente = self.firebase.get(contexto.codigo_medico + '/' + contexto.dia_mes_ano + '/' +
                                     "pacientes/", contexto.codigo_paciente)

        return paciente

    def desmarcar_paciente_fila(self, contexto):
        self.firebase.delete(contexto.codigo_medico + '/' + contexto.dia_mes_ano + '/' +
                             "pacientes/" + contexto.codigo_paciente, None)

        self.posicao_fila.posicao_apos_desmarcar(contexto)