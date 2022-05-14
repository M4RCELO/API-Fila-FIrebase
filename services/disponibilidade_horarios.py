from banco_dados.firestore_database_singleton import FirestoreDatabaseSingleton
from banco_dados.realtime_database_singleton import RealtimeDatabaseSingleton
from utils.gerar_horarios import UtilsTime


class HorariosDisponiveisMedico:

    def __init__(self):
        self.db = FirestoreDatabaseSingleton.instance().db
        self.firebase = RealtimeDatabaseSingleton.instance().firebase

    def horarios_disponiveis(self, contexto):

        doc_ref = self.db.collection('funcionarios').document(contexto.codigo_medico).collection('atendimentos').document(contexto.dia_mes_ano)
        dict_pacientes = self.firebase.get(str(contexto.codigo_medico) + '/' + contexto.dia_mes_ano,
                                           "pacientes")

        dict_horarios_disponiveis = {'horarios_disponiveis': []}

        dict_horarios = doc_ref.get().to_dict()

        utils_time = UtilsTime()

        horario_inicio = dict_horarios['inicio'].split(':')
        horario_fim = dict_horarios['fim'].split(':')
        intervalo_minutos = dict_horarios['intervalo']

        inicio = (int(horario_inicio[0]), int(horario_inicio[1]))
        fim = (int(horario_fim[0]), int(horario_fim[1]))
        intervalo = (0, intervalo_minutos)

        for hora in utils_time.gerador_de_horarios(inicio, fim, intervalo):
            hora_split = str(hora).split(":")
            hora_str = hora_split[0] + ":" + hora_split[1]
            if hora_str not in dict_horarios['horarios_indisponiveis']:
                dict_horarios_disponiveis['horarios_disponiveis'].append(hora_str)

        if dict_pacientes!=None:

            for i in dict_pacientes:
                horario_paciente = utils_time.conversor_segundos_horas(dict_pacientes[i]['horario'])
                if horario_paciente in dict_horarios_disponiveis['horarios_disponiveis']:
                    dict_horarios_disponiveis['horarios_disponiveis'].remove(horario_paciente)


        return dict_horarios_disponiveis