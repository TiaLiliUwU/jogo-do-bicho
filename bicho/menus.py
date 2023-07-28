#código para fazer os menus
from cc import CustomConsole
cc = CustomConsole()
from sorteio import Sorteio, Verificação
sort = Sorteio()
veri = Verificação()
from aposta import Grupo, Numero # Eu posso jogar dados pra aposta sem cair em loop, isso será usado pra refatorar os códigos
a = Grupo()
n = Numero()

# Menu das apostas
class Menu:

    @staticmethod
    def menu_aposta():

        sort.sort() # Olhar twitter pra ver os comentários
        while True:
            print("Deseja apostar em Grupos ou Números? \n\n1 - Grupos \n2 - Números\n")
            op = int(input("Selecione seu tipo de aposta: "))
            if op == 1:
                cc.clear()
                Menu.menu_grupo()
                break
            elif op == 2:
                cc.clear()
                Menu.menu_num()
                break
            else:
                cc.erro()

    @staticmethod
    def menu_num():
        while True:
            print("Qual aposta deseja realizar? \n\n1 - Dezena \n2 - Centena \n3 - Milhar \n4 - Duque de dezenas \n5 - Terno de dezenas")
            modo = int(input("Selecione a opção desejada: "))
            if modo == 1:
                n.dezena()
                veri.verificar_dezena()
                break
            elif modo == 2:
                n.centena()
                veri.verificar_centena()
                break
            elif modo == 3:
                n.milhar()
                veri.verificar_milhar()
                break
            elif modo == 4:
                n.duque_dezena()
                veri.verificar_multi_num()
                break
            elif modo == 5:
                n.terno_dezena()
                veri.verificar_multi_num()
                break
            else:
                cc.erro()
                cc.enter()

    # Menu das apostas em grupo
    @staticmethod
    def menu_grupo():
        while True:
            print("Qual aposta deseja realizar? \n\n1 - Grupo \n2 - Duque de grupo \n3 - Terno de grupo\n")
            modo = int(input("Selecione a opção desejada: "))
            if modo == 1:
                a.grupo()
                veri.verificar_grupo()
                break
            elif modo == 2:
                a.duque_grupo()
                veri.verificar_multi_grupo()
                break
            elif modo == 3:
                a.terno_grupo()
                veri.verificar_multi_grupo()
                break
            else:
                cc.erro()
                cc.enter()