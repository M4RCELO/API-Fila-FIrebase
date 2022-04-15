from datetime import datetime, timedelta
import time


class UtilsTime:

    def gerador_de_horarios(self, inicio, fim, intervalo):

        inicio = datetime(2017, 1, 1, *inicio)
        fim = datetime(2017, 1, 1, *fim)

        iHoras, iMinutos = intervalo

        intervalo = timedelta(hours=iHoras, minutes=iMinutos)

        while inicio <= fim:
            yield inicio.time()
            inicio += intervalo

    def conversor_segundos_horas(self,segundos):
        return time.strftime("%H:%M", time.gmtime(segundos))
