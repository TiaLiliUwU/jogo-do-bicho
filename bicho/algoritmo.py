# Esse código é para criação do sorteio procedural
import ntplib # Precisa ser instalado
from datetime import datetime, time
import pytz # Precisa ser instalado
from requests_html import HTMLSession # precisa ser instalado
s = HTMLSession()
from bichos import Animais
a = Animais()

# Parametros a serem usados: localização, clima (por consequência o dia) horário.
# O programa irá gerar 2 sorteios por dia: às 2pm e às 6pm
# Se tudo correr bem, o programa apresentará o mesmo resultado independente do local onde for rodado

# Algoritmo
class Algoritmo():
    
    local = ''
    chave = ''
    dia_hora = ''
    dds_alg = ''
    dic_cidades = {
   
    "Rio+de+Janeiro": '4c8707d8c58adcbfc8a180ca0031e61fa18c13475c807f2346cbc5b0d75477f2',
    "São+Gonçalo": '647ab79b9b1714aa8a5a18a160baaa48eff927450da190a7e41857bae6b3b79a',
    "Duque+de+Caxias": 'ee8daaa28b0b2bbf268a2032dc0f8ac6e9bb92b1b3fa4df92b45c29b40002dd7',
    "Nova+Iguaçu": '01b9d6a87abf12df2979b42b5a73012b32a0a541438c05000ee1d434d7e29efd',
    "Campos+dos+Goytacazes": '13c123f62c671fa22f4df03e5963dcbc318be0b283b43d425b5b69c603c9c471',
    "Belford+Roxo": '82111dc75ebbde15bc3a812a991ea0afab23b3a25771bfa9ceaddae9de025156',
    "Niterói": '64c078df690193fdd97de0af8dcc6129b8497c7477e031938ab3a1b6491a4b04',
    "São+João+de+Meriti": 'a6b3629546052689acb807aa264eb930af7417a3f1137af88325ca5a3403b58a',
    "Petrópolis": 'f089510b5124b571f0784421ddbfc39fd24811a86ef59c18d25a40f3c0536ff7',
    "Volta+Redonda": '9b9c099430094c615e63afd2e5fb18129e862acdb6b354d598512bdb4e5534e7',
    "Macaé": '49d5b60ac19377118e96655b7255c35a3d2734575c4022d9d28a767713d03f2a',
    "Magé": '1c7a627d8cfbffa0fb5e7d4b52fe1fb2d4c2dead1342a61f2ee367cf436c8d28',
    "Itaboraí": '514e02b2f5e0389eec56a366d28691b12c19d424feb28816fd1b935df94cc424',
    "Cabo+Frio": 'eb00d642285646f38c051232f836f5c0c86c142d90bc447ebd9eb05ad2519b02',
    "Maricá": '2296b14bb55ab7fda4172b63b445eface32c94e1ab83bbb1169e2e126845a390',
    "Nova+Friburgo": '44ef1e1142a4825c038d4a1c2493f1204e394d0b6a4ea7399ecdf83e903fea58',
    "Barra+Mansa": 'a0762bb8082f05514f6e6cedc43d2ef2775850493766aa7ca7008b884fd32b8f',
    "Angra+dos+Reis": '9b0762d05b2364fc16e8874da3dc071e18231fbcf5af325359285216d0cb5cad',
    "Mesquita": '95f5d585ae287239b3dce21208d4c221c9ab7089268a95ba8c1cd971e87871ad',
    "Teresópolis": '269a997eda8248645ccdb8947de7af85691f7ea2841b56a28fdd624486c6f064',
    "Rio+das+Ostras": '2e59afaa48b2796c3bef1dc49885e02ff3867b5251c1d39cf12124ede3b71b31',
    "Nilópolis": '2b34df0761d434fa90f082b551c5427209f52073c167173f55a4cb485253c144',
    "Queimados": '3ede373357c4b9b240514ed56a957fe2a9ad9be100f0e58880d1888ee8424d0d',
    "Araruama": '7430555568edd46fb62a3c3bda7670a1269ca0eb961869b56f897cba57ab7ed1',
    "Resende": '04cbbdf0632a852818fe28c34b7269ec97123f31bec89c2cc76e4b2242ddea68',
    "Itaguaí": '5b9d2d01ed6c4642c88f794d8e05d788d9fa5181293a5dbc5f304b34f3863bcd',
    "São+Pedro+da+Aldeia": '5575e19789642084cd974b201427e691a3edd244b31ea40207f86bf04e779036',
    "Itaperuna": 'ab172d924ee239774f4a84d933eb8a3f43c0bae73c95018370db313a4047a75a',
    "Japeri": 'be5a7c399f9cb3ce51b98eed4fa1b6bdc7b73b6d4228f6215473defe964dfb05',
    "Barra+do+Piraí": 'ca816d9f5b19b29372c41213f070d7341461417bbe718340e3d09ab55091190c',
    "Saquarema": '333ab90abeffe671c5105c325bc3111a3c3698e24a8a34a5ebc960f5cc41d115'
    }
    
    cidades = list(dic_cidades.keys())

    @staticmethod
    def get_local(): # Fazer essa porra ficar repetndo até conseguir

        ntp_server = 'pool.ntp.org'   
        fuso_horario_sp = pytz.timezone('America/Sao_Paulo')
        client = ntplib.NTPClient()
        response = client.request(ntp_server, version=3)
        ntp_time = datetime.fromtimestamp(response.tx_time, tz=fuso_horario_sp)
        Algoritmo.dia_hora = ntp_time.time()
        if Algoritmo.dia_hora < time(hour=12):
            local = Algoritmo.cidades[ntp_time.day-1]
        else:
            local = Algoritmo.cidades[ntp_time.day]
        Algoritmo.local = local
        Algoritmo.chave = Algoritmo.dic_cidades[local]


    @staticmethod
    def get_previsao(chave):

        url1 = f'https://weather.com/pt-BR/clima/horaria/l/{chave}'
        url2 = f'https://weather.com/pt-BR/clima/10dias/l/{chave}'

        r1 = s.get(url1, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
        r2 = s.get(url2, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

        maxi = r2.html.find('details.DaypartDetails--DayPartDetail--2XOOV.Disclosure--themeList--1Dz21[id="detailIndex1"] span.DailyContent--temp--1s3a7', first=True).text  # em Cº        
        mini = r2.html.find('details.DaypartDetails--DayPartDetail--2XOOV.Disclosure--themeList--1Dz21[id="detailIndex1"] span.DailyContent--temp--1s3a7.DailyContent--tempN--33RmW', first=True).text  # em Cº        

        # Provavelemente eu consigo refatorar isso:

        # sorteio 12 horas, olhando o dia seguinte
        temp_12 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] span.DetailsSummary--tempValue--jEiXE', first=True).text  # em Cº        
        sense_12 = (r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] span.DetailsTable--value--2YD0-', first=True).text) # em Cº
        vento_12 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] span.Wind--windWrapper--3Ly7c.DetailsTable--value--2YD0-', first=True).text  # em Km/h
        umidade_12 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] [data-testid="HumiditySection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        uv_12 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] [data-testid="uvIndexSection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        nebulosidade_12 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex15"] [data-testid="CloudCoverSection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        chuva_12 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex15"] [data-testid="Precip"].DetailsSummary--precip--1a98O [data-testid="PercentageValue"]', first=True).text
        # sorteio 18 horas, olhando o dia seguinte
        temp_18 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex22"] span.DetailsSummary--tempValue--jEiXE', first=True).text  # em Cº
        sense_18 = (r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex22"] span.DetailsTable--value--2YD0-', first=True).text) # em Cº
        vento_18 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex22"] span.Wind--windWrapper--3Ly7c.DetailsTable--value--2YD0-', first=True).text  # em Km/h
        umidade_18 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex22"] [data-testid="HumiditySection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        uv_18 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex22"] [data-testid="uvIndexSection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        nebulosidade_18 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex21"] [data-testid="CloudCoverSection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        chuva_18 = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex21"] [data-testid="Precip"].DetailsSummary--precip--1a98O [data-testid="PercentageValue"]', first=True).text
        
        #sorteio 18, olhando o dia de hoje (em caso de meia noite)

        maxi_a = r2.html.find('details.DaypartDetails--DayPartDetail--2XOOV.Disclosure--themeList--1Dz21[id="detailIndex1"] span.DailyContent--temp--1s3a7', first=True).text  # em Cº        
        mini_a = r2.html.find('details.DaypartDetails--DayPartDetail--2XOOV.Disclosure--themeList--1Dz21[id="detailIndex1"] span.DailyContent--temp--1s3a7.DailyContent--tempN--33RmW', first=True).text  # em Cº        


        temp_18_a = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] span.DetailsSummary--tempValue--jEiXE', first=True).text  # em Cº
        sense_18_a = (r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] span.DetailsTable--value--2YD0-', first=True).text) # em Cº
        vento_18_a = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] span.Wind--windWrapper--3Ly7c.DetailsTable--value--2YD0-', first=True).text  # em Km/h
        umidade_18_a = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] [data-testid="HumiditySection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        uv_18_a = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] [data-testid="uvIndexSection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        nebulosidade_18_a = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] [data-testid="CloudCoverSection"].DetailsTable--listItem--Z-5Vi span.DetailsTable--value--2YD0-', first=True).text
        chuva_18_a = r1.html.find('details.DaypartDetails--DayPartDetail--2XOOV[id="detailIndex16"] [data-testid="Precip"].DetailsSummary--precip--1a98O [data-testid="PercentageValue"]', first=True).text

        while True:
            if Algoritmo.dia_hora < time(hour=12):
                dds_cache = [maxi_a, mini_a, temp_18_a, sense_18_a, vento_18_a, umidade_18_a, uv_18_a, nebulosidade_18_a, chuva_18_a]
            elif Algoritmo.dia_hora >= time(hour=12) and Algoritmo.dia_hora < time(hour=18):
                dds_cache = [maxi, mini, temp_12, sense_12, vento_12, umidade_12, uv_12, nebulosidade_12, chuva_12]
            else:
                dds_cache = [maxi, mini, temp_18, sense_18, vento_18, umidade_18, uv_18, nebulosidade_18, chuva_18]#

            Algoritmo.dds_alg = [int(''.join(filter(str.isdigit, item))) for item in dds_cache]
            break