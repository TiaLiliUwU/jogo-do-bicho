# tentando de novo essa bosta
from cc import CustomConsole
cc = CustomConsole()
from aposta import Apostas
a = Apostas()
from menus import Menu
m = Menu()

# Menu principal
cc.clear()
while True:
    print("Testando essa coisa, não gostar respeitar!")
    print("\nBem-vindo ao Jogo do Bicho!\n")
    print("Você deseja realizar uma apostar de Grupo ou Número? \n\n1 - Grupo \n2 - Número\n")
    modo_aposta = int(input("Selecione seu tipo de aposta: "))
    if modo_aposta == 1:
        cc.clear()
        m.menu_grupo()
        break
    elif modo_aposta == 2:
        cc.clear()
        m.menu_num()
        break
    else:
        cc.erro()
cc.enter()
