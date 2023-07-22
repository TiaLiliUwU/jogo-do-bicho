#código para fazer os menus
from cc import CustomConsole
cc = CustomConsole()
from sorteio import Sorteio, Verificação
sort = Sorteio()
veri = Verificação()
from aposta import Grupo
a = Grupo()

class MenuGrupo:

    @staticmethod
    def menu_grupo():
        while True:
            print("Qual aposta você quer realizar? \n\n1 - Grupo \n2 - Duque de grupo \n3 - Terno de grupo\n")
            modo = int(input("Selecione a opção desejada: "))
            sort.sortear_animais() # Ver melhor depois a questão dos sorteios
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