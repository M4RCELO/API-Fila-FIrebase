from banco_dados.firestore_database_singleton import FirestoreDatabaseSingleton
from banco_dados.realtime_database_singleton import RealtimeDatabaseSingleton
from model.contexto_update_atendimento import ContextoUpdateAtendimento


class RepositoryEmAtendimento:

    def __init__(self):
        self.firebase= RealtimeDatabaseSingleton.instance().firebase
        self.db = FirestoreDatabaseSingleton.instance().db

    def inserir_atendimento(self,contexto):

        self.firebase.patch(
            str(contexto.codigo_medico) + '/' +
            str(contexto.dia_mes_ano) + '/',
            {'em_atendimento': {'paciente': 0}}
        )

    def update_em_atendimento(self,contexto_update_atendimento):

        data = {
            'paciente': contexto_update_atendimento.em_atendimento
        }

        self.firebase.patch(
            contexto_update_atendimento.codigo_medico + '/' +
            contexto_update_atendimento.dia_mes_ano + '/' +
            "em_atendimento",
            data
        )

    def read_em_atendimento(self,contexto):
        return self.firebase.get(contexto.codigo_medico + '/' + contexto.dia_mes_ano, "em_atendimento")

    def update_paciente_atendido(self,contexto_paciente_atendido):

        dict_pacientes = self.firebase.get(str(contexto_paciente_atendido.codigo_medico) + '/' + contexto_paciente_atendido.dia_mes_ano,
                                           "pacientes")

        proximo_paciente = []

        for i in dict_pacientes:

            if dict_pacientes[i]['posicao'] == contexto_paciente_atendido.posicao_paciente_atendido:

                data = {
                    'atendido': True
                }

                self.firebase.patch(
                    contexto_paciente_atendido.codigo_medico + '/' +
                    contexto_paciente_atendido.dia_mes_ano + '/' +
                    "pacientes/" + i,
                    data
                )

            if not dict_pacientes[i]['atendido'] and dict_pacientes[i]['posicao'] >= contexto_paciente_atendido.posicao_paciente_atendido+1:
                proximo_paciente.append(dict_pacientes[i]['posicao'])

        if len(proximo_paciente) > 0:
            contexto_update_atendimento = ContextoUpdateAtendimento(
                codigo_medico=contexto_paciente_atendido.codigo_medico,
                dia_mes_ano=contexto_paciente_atendido.dia_mes_ano,
                em_atendimento=min(proximo_paciente)
            )

            self.update_em_atendimento(contexto_update_atendimento)
            self.db.collection('fila').document(contexto_paciente_atendido.codigo_medico+contexto_paciente_atendido.dia_mes_ano).update({'paciente':min(proximo_paciente)})

        else:
            contexto_update_atendimento = ContextoUpdateAtendimento(
                codigo_medico=contexto_paciente_atendido.codigo_medico,
                dia_mes_ano=contexto_paciente_atendido.dia_mes_ano,
                em_atendimento=contexto_paciente_atendido.posicao_paciente_atendido
            )

            self.update_em_atendimento(contexto_update_atendimento)
            self.db.collection('fila').document(contexto_paciente_atendido.codigo_medico+contexto_paciente_atendido.dia_mes_ano).update({'concluido': True})


