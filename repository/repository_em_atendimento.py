from banco_dados.banco_dados_singleton import BancoDadosSingleton


class RepositoryEmAtendimento:

    def __init__(self):
        banco_dados = BancoDadosSingleton.instance()
        self.Firebase = banco_dados.firebase

    def update_em_atendimento(self,contexto_update_atendimento):

        data = {
            'paciente': contexto_update_atendimento.em_atendimento
        }

        self.Firebase.patch(
            contexto_update_atendimento.codigo_medico + '/' +
            contexto_update_atendimento.dia_mes_ano + '/' +
            "em_atendimento",
            data
        )

    def read_em_atendimento(self,codigo_medico, dia_mes):
        return self.Firebase.get(codigo_medico + '/' + dia_mes, "em_atendimento")

