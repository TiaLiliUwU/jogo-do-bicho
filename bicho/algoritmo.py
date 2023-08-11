# Esse código é para criação do sorteio procedural
import ntplib # Precisa ser instalado
import csv
from datetime import datetime, time, timedelta
import pytz # Precisa ser instalado
from requests_html import HTMLSession # precisa ser instalado
s = HTMLSession()
from bichos import Animais
a = Animais()

# Caro eu do futuro, Sierra, ou seja lá quem esteja lendo este código,
# eu não consegui fazer essa joça funcionar puxando os dados da internet.
# Uma alternativa que eu encontrei foi baixar os dados do governo e armazenar offline.
# Ainda vou criar uma forma de fazer isso automaticamente. 
#
# Por favor, incremente o contador de horas gastas nesse código:
# 
# horas_gastas = 185

class Algoritmo():
    
    chave = ''
    dia = ''
    dia_dds = ''
    hora = ''
    hora_sort = ''
    dds_alg = []
    timestamp = ''
    cidades = [
        "ANGRA DOS REIS.CSV",
        "ARRAIAL DO CABO.CSV",
        "BAURU.CSV",
        "CAMBUCI.CSV",
        "CAMPOS DO JORDAO.CSV",
        "CAMPOS DOS GOYTACAZES.CSV",
        "CARMO.CSV",
        "DUQUE DE CAXIAS.CSV",
        "FRANCA.CSV",
        "MACAE.CSV",
        "NITEROI.CSV",
        "NOVA FRIBURGO.CSV",
        "PARATY.CSV",
        "Paty do Alferes.CSV",
        "PICO DO COUTO.CSV",
        "PORTO ALEGRE.CSV",
        "PRESIDENTE PRUDENTE.CSV",
        "RESENDE.CSV",
        "RIO CLARO.CSV",
        "RIO DE JANEIRO.CSV",
        "RIO GRANDE.CSV",
        "SANTA MARIA MADALENA.CSV",
        "SANTA MARIA.CSV",
        "SANTANA DO LIVRAMENTO.CSV",
        "SAO PAULO.CSV",
        "SAQUAREMA.CSV",
        "SEROPEDICA.CSV",
        "SILVA JARDIM.CSV",
        "TERESOPOLIS.CSV",
        "TRES RIOS.CSV",
        "VALENCA.CSV"
    ]
    
    @staticmethod
    def get_local(): # Fazer essa porra ficar repetndo até conseguir

        ntp_server = 'pool.ntp.org'   
        fuso_horario_sp = pytz.timezone('America/Sao_Paulo')
        client = ntplib.NTPClient()

        try:
            response = client.request(ntp_server, version=3)
            ntp_time = datetime.fromtimestamp(response.tx_time, tz=fuso_horario_sp)   
        except ntplib.NTPException:
            print("Estou sem clima para os resultados de hoje 0,0\n\n\n\n")

        Algoritmo.hora = (ntp_time.time())
        Algoritmo.dia = ntp_time.strftime('%Y/%m/%d')
        
        # Esse código não vai funcionar corretamente em ano bissexto
        if time(hour=12) <= Algoritmo.hora < time(hour=18):
            Algoritmo.chave = Algoritmo.cidades[ntp_time.day-1]
            Algoritmo.dia_dds = (datetime.strptime(Algoritmo.dia, '%Y/%m/%d') - timedelta(days=365)).strftime('%Y/%m/%d')
            Algoritmo.hora_sort = '1200 UTC'
        elif time(hour=18) <= Algoritmo.hora:
            Algoritmo.chave = Algoritmo.cidades[ntp_time.day-1]
            Algoritmo.dia_dds = (datetime.strptime(Algoritmo.dia, '%Y/%m/%d') - timedelta(days=365)).strftime('%Y/%m/%d')
            Algoritmo.hora_sort = '1800 UTC'
        elif time(hour=0) <= Algoritmo.hora < time(hour=12):
            Algoritmo.chave = Algoritmo.cidades[ntp_time.day-2]
            Algoritmo.dia_dds = (datetime.strptime(Algoritmo.dia, '%Y/%m/%d') - timedelta(days=366)).strftime('%Y/%m/%d')
            Algoritmo.hora_sort = '1800 UTC'

    @staticmethod
    def get_previsao():

        path = f'etc\{Algoritmo.chave}'
        with open(path, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv, delimiter=';')
            next(leitor)
            for dds in leitor:
                linha_data = dds[0].strip()
                linha_horario = dds[1].strip()
                if linha_data == Algoritmo.dia_dds and linha_horario == Algoritmo.hora_sort:
                    dds = list(filter(lambda item: item.strip() != '', dds))
                    for item in dds[2:]:
                        item = item.strip()
                        if ',' in item:
                            Algoritmo.dds_alg.append(float(item.replace(',', '.')))
                        else:
                            Algoritmo.dds_alg.append(int(item))