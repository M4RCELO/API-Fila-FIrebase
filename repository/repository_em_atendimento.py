from banco_dados.realtime_database_singleton import RealtimeDatabaseSingleton


class RepositoryEmAtendimento:

    def __init__(self):
        self.firebase= RealtimeDatabaseSingleton.instance().firebase

    def update_em_atendimento(self,contexto_update_atendimento):

        data = {
            'paciente': contexto_update_atendimento.em_atendimento
        }

        self.firebase.patch(
            contexto_update_atendimento.codigo_medico + '/' +
            contexto_update_atendimento.dia_mes_ano + '/' +
            "atendimento",
            data
        )

    def read_em_atendimento(self,contexto):
        return self.firebase.get(contexto.codigo_medico + '/' + contexto.dia_mes_ano, "em_atendimento")

    def update_paciente_atendido(self,contexto_paciente_atendido):

        dict_pacientes = self.firebase.get(str(contexto_paciente_atendido.codigo_medico) + '/' + contexto_paciente_atendido.dia_mes_ano,
                                           "pacientes")

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




