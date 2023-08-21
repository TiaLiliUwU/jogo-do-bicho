# Código para gerenciamento do banco de dados
import questionary # tem que instalar
import sqlite3
import os
from algoritmo import Algoritmo
alg = Algoritmo()
from sorteio import Sorteio
sort = Sorteio()
from cc import CustomConsole
cc = CustomConsole()
from aposta import Apostas
a = Apostas()

class ReadWriteApostas:

    @staticmethod
    def read_aposta():
        pass
    
    @staticmethod
    def create():

        conexao = sqlite3.connect('aposta.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS anos (
                id INTEGER PRIMARY KEY,
                ano INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS meses (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dias (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS horarios (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia_id INTEGER,
                horario TEXT,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id),
                FOREIGN KEY (dia_id) REFERENCES dias(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS apostas_num (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia_id INTEGER,
                horario_id INTEGER,
                numero1 INTEGER,
                numero2 INTEGER,
                numero3 INTEGER,
                duro_cerc INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id),
                FOREIGN KEY (dia_id) REFERENCES dias(id),
                FOREIGN KEY (horario_id) REFERENCES horarios(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS apostas_ani (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia_id INTEGER,
                horario_id INTEGER,
                animal1 INTEGER,
                animal2 INTEGER,
                animal3 INTEGER,
                duro_cerc INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id),
                FOREIGN KEY (dia_id) REFERENCES dias(id),
                FOREIGN KEY (horario_id) REFERENCES horarios(id)
            )
        ''')

        conexao.commit()
        conexao.close()

    @staticmethod
    def write_aposta():

        aposta = []
        if isinstance(a.aposta, list):
            aposta.extend(a.aposta)
        else:
            aposta.append(a.aposta)
        duro_cerc = a.duro_cerc
        if duro_cerc == '':
            duro_cerc = 3
        while len(aposta) < 3:
            aposta.append(666)
        aposta.append(duro_cerc)
        data = str(Algoritmo.dia)
        ano, mes, dia = data.split("/")
        horario = str(Algoritmo.hora)

        ReadWriteApostas.create()

        conexao = sqlite3.connect('aposta.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT id FROM anos WHERE ano = ?', (ano,))
        resultado = cursor.fetchone()
        if resultado:
            ano_id = resultado[0]
        else:
            cursor.execute('INSERT INTO anos (ano) VALUES (?)', (ano,))
            ano_id = cursor.lastrowid

        cursor.execute('SELECT id FROM meses WHERE ano_id = ? AND mes = ?', (ano_id, mes))
        resultado = cursor.fetchone()
        if resultado:
            mes_id = resultado[0]
        else:
            cursor.execute('INSERT INTO meses (ano_id, mes) VALUES (?, ?)', (ano_id, mes))
            mes_id = cursor.lastrowid

        cursor.execute('SELECT id FROM dias WHERE ano_id = ? AND mes_id = ? AND dia = ?', (ano_id, mes_id, dia))
        resultado = cursor.fetchone()
        if resultado:
            dia_id = resultado[0]
        else:
            cursor.execute('INSERT INTO dias (ano_id, mes_id, dia) VALUES (?, ?, ?)', (ano_id, mes_id, dia))
            dia_id = cursor.lastrowid

        cursor.execute('SELECT id FROM horarios WHERE ano_id = ? AND mes_id = ? AND dia_id = ? AND horario = ?', (ano_id, mes_id, dia_id, horario))
        resultado = cursor.fetchone()
        if resultado:
            horario_id = resultado[0]
        else:
            cursor.execute('INSERT INTO horarios (ano_id, mes_id, dia_id, horario) VALUES (?, ?, ?, ?)', (ano_id, mes_id, dia_id, horario))
            horario_id = cursor.lastrowid

        # BUG AQUI
        if a.write_aposta == 1:
            cursor.execute('SELECT COUNT(*) FROM apostas_ani WHERE animal1 = ? AND animal2 = ? AND animal3 = ? AND duro_cerc = ?', aposta)
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                cursor.execute('INSERT INTO apostas_ani (ano_id, mes_id, dia_id, horario_id, animal1, animal2, animal3, duro_cerc) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (ano_id, mes_id, dia_id, horario_id, *aposta))
        else:
            cursor.execute('SELECT COUNT(*) FROM apostas_num WHERE numero1 = ? AND numero2 = ? AND numero3 = ? AND duro_cerc = ?', aposta)
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                cursor.execute('INSERT INTO apostas_num (ano_id, mes_id, dia_id, horario_id, numero1, numero2, numero3, duro_cerc) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (ano_id, mes_id, dia_id, horario_id, *aposta))

        conexao.commit()
        conexao.close()

class ReadWriteSorteios:

    anos = ''
    meses = ''
    dias = ''
    horas = ''
    sorteio = ''

    @staticmethod
    def consultar_sorteio():

        opcoes = []
        
        print("Busca de sorteios\n")

        if not os.path.exists('sorteio.db'):
            print("Nenhum sorteio cadastrado no banco de dados")
        else:
        
            conexao = sqlite3.connect('sorteio.db')
            cursor = conexao.cursor()
            cursor.execute('SELECT ano FROM anos')
            anos = [ano[0] for ano in cursor.fetchall()]

            if not anos:
                print("Nenhum sorteio cadastrado no banco de dados")
            else:

                for dds in anos:
                    opcoes.append({"name": f"{dds}", "value": f"{dds}"})

                ano = int(questionary.select("Foram encontrados sorteios para os seguintes anos:\n", choices=opcoes, instruction=' ', qmark='*').ask())
                cursor.execute('SELECT id FROM anos WHERE ano = ?', (ano,))
                ano_id = (cursor.fetchone())
                ano_id = ano_id[0]
                opcoes = []

                cursor.execute('SELECT mes FROM meses WHERE ano_id = ?', (ano_id,))
                meses = [mes[0] for mes in cursor.fetchall()]

                for dds in meses:
                    opcoes.append({"name": f"{dds}", "value": f"{dds}"})

                mes = int(questionary.select("Foram encontrados sorteios para os seguintes meses:\n", choices=opcoes, 
                instruction=' ', qmark='*').ask())
                cursor.execute('SELECT id FROM meses WHERE ano_id = ? AND mes = ?', (ano_id, mes))
                mes_id = cursor.fetchone()
                mes_id = mes_id[0]
                opcoes = []

                cursor.execute('SELECT dia FROM dias WHERE ano_id = ? AND mes_id = ?', (ano_id, mes_id))
                dias = [dia[0] for dia in cursor.fetchall()]

                for dds in dias:
                    opcoes.append({"name": f"{dds}", "value": f"{dds}"})

                dia = int(questionary.select("Foram encontrados sorteios para os seguintes dias:\n", choices=opcoes, instruction=' ', qmark='*').ask())
                cursor.execute('SELECT id FROM dias WHERE ano_id = ? AND mes_id = ? AND dia = ?', (ano_id, mes_id, dia))
                dia_id = cursor.fetchone()
                dia_id = dia_id[0]
                opcoes = []

                cursor.execute('SELECT horario FROM sorteios_num WHERE ano_id = ? AND mes_id = ? AND dia_id = ?', (ano_id, mes_id, dia_id))
                horas = [horario[0] for horario in cursor.fetchall()]

                for dds in horas:
                    opcoes.append({"name": f"{dds}", "value": f"{dds}"})

                hora = questionary.select("Foram encontrados sorteios para os seguintes horários:\n", choices=opcoes, instruction=' ', qmark='*').ask()

                cursor.execute('''
                    SELECT numero1, numero2, numero3, numero4, numero5 
                    FROM sorteios_num
                    WHERE ano_id = ? AND mes_id = ? AND dia_id = ? AND horario = ?
                ''', (ano_id, mes_id, dia_id, hora))

                sorteio_num = cursor.fetchone()

                cursor.execute('''
                    SELECT animal1, animal2, animal3, animal4, animal5 
                    FROM sorteios_ani
                    WHERE ano_id = ? AND mes_id = ? AND dia_id = ? AND horario = ?
                ''', (ano_id, mes_id, dia_id, hora))

                sorteio_ani = cursor.fetchone()
                
                cc.clear()

                if hora == '1200 UTC':
                    hora = '12:00'
                else:
                    hora = '18:00'

                print(f'Sorteio do dia {str(dia)}/{str(mes)}/{str(ano)} às {str(hora)}:\n')
                print(f'Animais: {", ".join(map(str, sorteio_ani))}')
                print(f'Números: {", ".join(map(lambda x: str(x).zfill(4), sorteio_num))}')

                conexao.close()


    @staticmethod
    def create():

        conexao = sqlite3.connect('sorteio.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS anos (
                id INTEGER PRIMARY KEY,
                ano INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS meses (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dias (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id)
            )
        ''')


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sorteios_num (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia_id INTEGER,
                horario TEXT,
                numero1 INTEGER,
                numero2 INTEGER,
                numero3 INTEGER,
                numero4 INTEGER,
                numero5 INTEGER,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id),
                FOREIGN KEY (dia_id) REFERENCES dias(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sorteios_ani (
                id INTEGER PRIMARY KEY,
                ano_id INTEGER,
                mes_id INTEGER,
                dia_id INTEGER,
                horario TEXT,
                animal1 TEXT,
                animal2 TEXT,
                animal3 TEXT,
                animal4 TEXT,
                animal5 TEXT,
                FOREIGN KEY (ano_id) REFERENCES anos(id),
                FOREIGN KEY (mes_id) REFERENCES meses(id),
                FOREIGN KEY (dia_id) REFERENCES dias(id)
            )
        ''')

        conexao.commit()
        conexao.close()

    @staticmethod
    def write_sorteio():

        sorteio_num = Sorteio.sorteios_num
        sorteio_ani = Sorteio.sorteios_ani
        data = str(Algoritmo.dia)
        ano, mes, dia = data.split("/")
        horario = Algoritmo.hora_sort

        ReadWriteSorteios.create()

        conexao = sqlite3.connect('sorteio.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT id FROM anos WHERE ano = ?', (ano,))
        resultado = cursor.fetchone()
        if resultado:
            ano_id = resultado[0]
        else:
            cursor.execute('INSERT INTO anos (ano) VALUES (?)', (ano,))
            ano_id = cursor.lastrowid

        cursor.execute('SELECT id FROM meses WHERE ano_id = ? AND mes = ?', (ano_id, mes))
        resultado = cursor.fetchone()
        if resultado:
            mes_id = resultado[0]
        else:
            cursor.execute('INSERT INTO meses (ano_id, mes) VALUES (?, ?)', (ano_id, mes))
            mes_id = cursor.lastrowid

        cursor.execute('SELECT id FROM dias WHERE ano_id = ? AND mes_id = ? AND dia = ?', (ano_id, mes_id, dia))
        resultado = cursor.fetchone()
        if resultado:
            dia_id = resultado[0]
        else:
            cursor.execute('INSERT INTO dias (ano_id, mes_id, dia) VALUES (?, ?, ?)', (ano_id, mes_id, dia))
            dia_id = cursor.lastrowid

        cursor.execute('SELECT id FROM sorteios_num WHERE ano_id = ? AND mes_id = ? AND dia_id = ? AND horario = ? AND numero1 = ? AND numero2 = ? AND numero3 = ? AND numero4 = ? AND numero5 = ?', (ano_id, mes_id, dia_id, horario, *sorteio_num))
        resultado = cursor.fetchone()
        if not resultado:
            cursor.execute('INSERT INTO sorteios_num (ano_id, mes_id, dia_id, horario, numero1, numero2, numero3, numero4, numero5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (ano_id, mes_id, dia_id, horario, *sorteio_num))

        cursor.execute('SELECT id FROM sorteios_ani WHERE ano_id = ? AND mes_id = ? AND dia_id = ? AND horario = ? AND animal1 = ? AND animal2 = ? AND animal3 = ? AND animal4 = ? AND animal5 = ?', (ano_id, mes_id, dia_id, horario, *sorteio_ani))
        resultado = cursor.fetchone()
        if not resultado:
            cursor.execute('INSERT INTO sorteios_ani (ano_id, mes_id, dia_id, horario, animal1, animal2, animal3, animal4, animal5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (ano_id, mes_id, dia_id, horario, *sorteio_ani))

        conexao.commit()
        conexao.close()