from cc import CustomConsole
cc = CustomConsole()
from aposta import Apostas
a = Apostas()
from menus import Menu
m = Menu()
from banco import ReadWriteSorteios
rw = ReadWriteSorteios()
from pyfiglet import figlet_format # tem que instalar
from rich.console import Console # tem que instalar
rc = Console()
import questionary # tem que instalar

# Opções
opcoes = [
    {"name": "Apostar", "value": "opcao1"},
    {"name": "Verificar apostas (não desenvolvido)", "value": "opcao2"},
    {"name": "Verificar sorteios", "value": "opcao3"},
    {"name": "Sair", "value": "sair"},
]

# Menu principal
cc.clear()
rc.print(figlet_format('O Jogo do Bicho', font='small'), style='green bold')
print("Under development\n")
op = questionary.select("Selecione uma opção:\n", choices=opcoes, instruction=' ', qmark='*').ask()
if op == "opcao1":
    cc.clear()
    m.menu_aposta()
elif op == "opcao2":
    pass
elif op == "opcao3":
    cc.clear()
    rw.consultar_anos()
elif op == "sair":
    cc.clear()