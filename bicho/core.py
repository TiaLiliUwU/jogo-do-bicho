# tentando de novo essa bosta
from cc import CustomConsole
cc = CustomConsole()
from aposta import Apostas
a = Apostas()
from menus import Menu
m = Menu()
from banco import ReadWriteSorteios
rw = ReadWriteSorteios()

# Menu principal
cc.clear()
while True:
    print("Testando essa coisa, não gostar respeitar!")
    print("\nBem-vindo ao Jogo do Bicho!\n")
    print("O que deseja fazer? \n\n1 - Verificar sorteios \n2 - Verificar apostas (não desenvolvido) \n3 - Apostar\n")
    op = int(input("Selecione uma opção: "))
    if op == 1:
        cc.clear()
        rw.consultar_anos()
        break
    elif op == 2:
        pass
        break
    elif op == 3:
        cc.clear()
        m.menu_aposta()
        break
    else:
        cc.erro()
cc.enter()
