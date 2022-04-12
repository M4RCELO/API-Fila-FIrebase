import json


class PosicaoFila:

    def posicao_no_insert(self, firebase, contexto_insert, horario):

        maior_posicao_fila = 0
        posicao_fila = []

        dict_pacientes = firebase.get(str(contexto_insert.codigo_medico) + '/' + contexto_insert.dia_mes_ano,
                                      "pacientes")

        if dict_pacientes != None:
            for i in dict_pacientes:

                posicao_paciente = int(dict_pacientes[i]['posicao'])
                horario_paciente = int(dict_pacientes[i]['horario'])

                if posicao_paciente > maior_posicao_fila:
                    maior_posicao_fila = posicao_paciente

                if horario_paciente > horario:
                    posicao_fila.append(posicao_paciente)

                    data = {
                        'posicao': posicao_paciente + 1,
                    }

                    firebase.patch(
                        str(contexto_insert.codigo_medico) + '/' + contexto_insert.dia_mes_ano + '/pacientes/' + i,
                        data
                    )

            if len(posicao_fila) == 0:
                return maior_posicao_fila + 1
            else:
                return min(posicao_fila)

        else:
            return 1

    def posicao_no_update(self, firebase, contexto_insert, horario):

        posicao = 0
        dict_pacientes = firebase.get(str(contexto_insert.codigo_medico) + '/' + contexto_insert.dia_mes_ano,
                                      "pacientes")

        codigo_paciente = str(contexto_insert.codigo_paciente)

        dict_pacientes_atualizado = dict_pacientes
        dict_pacientes_atualizado[codigo_paciente]['horario'] = horario

        dict_para_ordenar = {}

        for i in dict_pacientes_atualizado:
            dict_para_ordenar[i] = dict_pacientes_atualizado[i]['horario']

        for i in sorted(dict_para_ordenar.items(), key = lambda kv:(kv[1], kv[0])):
            
            posicao+=1

            if posicao!=dict_pacientes[i[0]]['posicao']:
                data = {
                    'posicao': posicao,
                }

                firebase.patch(
                    str(contexto_insert.codigo_medico) + '/' + contexto_insert.dia_mes_ano + '/pacientes/' + i[0],
                    data
                )