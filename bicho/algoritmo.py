# Esse código é para criação do sorteio procedural
import ntplib # Precisa ser instalado
import requests
from datetime import datetime, time, timedelta
import pytz # Precisa ser instalado
from requests_html import HTMLSession # precisa ser instalado
s = HTMLSession()
from bichos import Animais
a = Animais()

# O programa irá gerar 2 sorteios por dia: às 2pm e às 6pm
# Se tudo correr bem, o programa apresentará o mesmo resultado independente do local onde for rodado

# Algoritmo
class Algoritmo():
    
    local = ''
    chave = ''
    dia = ''
    hora = ''
    hora_aposta = ''
    dds_alg = ''
    dic_cidades = {
        "Rio+de+Janeiro": [-22.9068, -43.1729],
        "São+Gonçalo": [-22.8262, -43.0509],
        "Duque+de+Caxias": [-22.7856, -43.3117],
        "Nova+Iguaçu": [-22.7556, -43.4603],
        "Campos+dos+Goytacazes": [-21.7620, -41.3186],
        "Belford+Roxo": [-22.7642, -43.3992],
        "Niterói": [-22.8832, -43.1032],
        "São+João+de+Meriti": [-22.8032, -43.3726],
        "Petrópolis": [-22.52, -43.19],
        "Volta+Redonda": [-22.5235, -44.0952],
        "Macaé": [-22.3709, -41.7842],
        "Magé": [-22.6639, -43.0311],
        "Itaboraí": [-22.7566, -42.8636],
        "Cabo+Frio": [-22.8859, -42.0281],
        "Maricá": [-22.9196, -42.8186],
        "Nova+Friburgo": [-22.2932, -42.5371],
        "Barra+Mansa": [-22.5453, -44.1712],
        "Angra+dos+Reis": [-23.0011, -44.3192],
        "Mesquita": [-22.7825, -43.4601],
        "Teresópolis": [-22.4166, -42.9752],
        "Rio+das+Ostras": [-22.5174, -41.9478],
        "Nilópolis": [-22.8055, -43.4233],
        "Queimados": [-22.7168, -43.5552],
        "Araruama": [-22.8697, -42.3320],
        "Resende": [-22.4686, -44.4469],
        "Itaguaí": [-22.8520, -43.7758],
        "São+Pedro+da+Aldeia": [-22.8428, -42.1020],
        "Itaperuna": [-21.1997, -41.8798],
        "Japeri": [-22.6437, -43.6605],
        "Barra+do+Piraí": [-22.4715, -43.8266],
        "Saquarema": [-22.9298, -42.5095]
    }
    
    cidades = list(dic_cidades.keys())

    @staticmethod
    def get_local(): # Fazer essa porra ficar repetndo até conseguir

        ntp_server = 'pool.ntp.org'   
        fuso_horario_sp = pytz.timezone('America/Sao_Paulo')
        client = ntplib.NTPClient()

        try:
            response = client.request(ntp_server, version=3)
            ntp_time = datetime.fromtimestamp(response.tx_time, tz=fuso_horario_sp)   
        except ntplib.NTPException:
            print("Estou sem clima para os resultados de hoje 0,0")

        Algoritmo.hora = ntp_time.time()
        if Algoritmo.hora < time(hour=12):
            local = Algoritmo.cidades[ntp_time.day-2]
            Algoritmo.dia = ntp_time.strftime('%Y-%m-%d')
        else:
            local = Algoritmo.cidades[ntp_time.day-1]
            Algoritmo.dia = ntp_time.date()
        Algoritmo.local = local
        Algoritmo.chave = Algoritmo.dic_cidades[local]


    @staticmethod
    def get_previsao():

        lat = Algoritmo.chave[0]
        lon = Algoritmo.chave[1]
        api_key = '994c5421e4e5432e09a97b1e884ca128'
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'

        req = requests.get(url)
        req_dic = req.json()
        
        if Algoritmo.hora < time(hour=12):
            dt_obj = datetime.strptime(f'{Algoritmo.dia} 18:00', "%Y-%m-%d %H:%M")
            Algoritmo.hora_aposta = '18:00'
        elif time(hour=12) <= Algoritmo.hora < time(hour=18):
            dt_obj = datetime.strptime(f'{Algoritmo.dia + timedelta(days=1)} 12:00', "%Y-%m-%d %H:%M")
            Algoritmo.hora_aposta = '12:00'
        else:
            dt_obj = datetime.strptime(f'{Algoritmo.dia + timedelta(days=1)} 18:00', "%Y-%m-%d %H:%M")
            Algoritmo.hora_aposta = '18:00'
        timestamp = int(dt_obj.timestamp())

        for data in req_dic['list']:
            if data['dt'] == timestamp:
                found_data = data
                break
        
        temp = found_data['main']['temp']
        feels_like = found_data['main']['feels_like']
        pressure = found_data['main']['pressure']
        sea_level = found_data['main']['sea_level']
        grnd_level = found_data['main']['grnd_level']
        humidity = found_data['main']['humidity']
        clouds = found_data['clouds']['all']
        speed = found_data['wind']['speed']
        deg = found_data['wind']['deg']
        gust = found_data['wind']['gust']
        visibility = found_data['visibility']
        pop = found_data['pop']

        Algoritmo.dds_alg = [temp, feels_like, pressure, sea_level, grnd_level, humidity, clouds, speed, deg, gust, visibility, pop]