#código para fazer os menus
import questionary
from cc import CustomConsole
cc = CustomConsole()
from sorteio import Sorteio, Verificação
sort = Sorteio()
veri = Verificação()
from aposta import Grupo, Numero
a = Grupo()
n = Numero()
from banco import ReadWriteSorteios, ReadWriteApostas
rw = ReadWriteSorteios()
rwa = ReadWriteApostas()
from algoritmo import Algoritmo
alg = Algoritmo()

# Menu das apostas
class Menu:

    @staticmethod
    def menu_aposta():

        opcoes = [
            {"name": "Grupos", "value": "opcao1"},
            {"name": "Números", "value": "opcao2"},
        ]

        sort.sort()
        rw.write_sorteio()
        op = questionary.select("Deseja apostar em Grupos ou Números?\n", choices=opcoes, instruction=' ', qmark='*').ask()
        cc.clear()
        if op == 'opcao1':
            Menu.menu_grupo()
        elif op == 'opcao2':
            Menu.menu_num()

    @staticmethod
    def menu_num():

        opcoes = [
            {"name": "Dezena", "value": "1"},
            {"name": "Centena", "value": "2"},
            {"name": "Milhar", "value": "3"},
            {"name": "Duque de dezenas", "value": "4"},
            {"name": "Terno de dezenas", "value": "5"},
        ]

        modo = int(questionary.select("Qual aposta deseja realizar?\n", choices=opcoes, instruction=' ', qmark='*').ask())
        if 1 <= modo <= 3:
            n.mono_num(modo)
            rwa.write_aposta()
            veri.verificar_mono_num(modo)
        elif 4 <= modo <= 5:
            n.multi_dezena(modo - 2)
            rwa.write_aposta()
            veri.verificar_multi_num()

    # Menu das apostas em grupo
    @staticmethod
    def menu_grupo():

        opcoes = [
            {"name": "Grupo", "value": "1"},
            {"name": "Duque de grupo", "value": "2"},
            {"name": "Terno de grupo", "value": "3"},
        ]

        modo = int(questionary.select("Qual aposta deseja realizar?\n", choices=opcoes, instruction=' ', qmark='*').ask())

        a.grupo(modo)
        rwa.write_aposta()
        cc.clear()
        if modo > 1:
            veri.verificar_multi_grupo()
        else:
            veri.verificar_grupo()
        
            
