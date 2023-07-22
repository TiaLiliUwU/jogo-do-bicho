# Código para obter a aposta do jogador
from bichos import Animais
ani = Animais()
from duro_cerc import DuroCercado
dc = DuroCercado(tipo=None)
from cc import CustomConsole
cc = CustomConsole()


# Apostas em Grupo
class Grupo:

    lista_animais = list(ani.animais.keys())
    animais_input = []
    animais_conv = []

    @staticmethod
    def get_aposta():
                
        for animal in Grupo.animais_input:
            Grupo.animais_conv.append(Grupo.lista_animais[animal])
        Apostas.aposta = Grupo.animais_conv

    @staticmethod
    def terno_grupo():

        cc.clear()
        print("Em quais grupos deseja apostar? \n")
        ani.mostrar_animais()  # Elaborar melhor essa lista
        while True:
            animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
            verifica_lista = len(Grupo.animais_input)
            if 0 <= animal_escolhido <= 24:
                if verifica_lista == 0:
                    Grupo.animais_input.append(animal_escolhido)
                elif animal_escolhido != Grupo.animais_input[0] and verifica_lista == 1:
                    Grupo.animais_input.append(animal_escolhido)
                elif animal_escolhido != Grupo.animais_input[1] and animal_escolhido != Grupo.animais_input[0]:
                    Grupo.animais_input.append(animal_escolhido)
                    break
                else:
                    print("\nVocê escolheu o mesmo animal novamente. Por favor, escolha outro.")
            else:
                cc.erro()
        Grupo.get_aposta()

    @staticmethod
    def duque_grupo():

        cc.clear()
        print("Em quais grupos deseja apostar? \n")
        ani.mostrar_animais()  # Elaborar melhor essa lista
        while True:
            animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
            if 0 <= animal_escolhido <= 24:
                if not Grupo.animais_input:
                    Grupo.animais_input.append(animal_escolhido)
                elif animal_escolhido != Grupo.animais_input[0]:
                    Grupo.animais_input.append(animal_escolhido)
                    break
                else:
                    print("\nVocê escolheu o mesmo animal novamente. Por favor, escolha outro.")
            else:
                cc.erro()
        Grupo.get_aposta()
            
    
    @staticmethod
    def grupo():

        dc.duro_cerc()
        while True:
            cc.clear()
            print("Em qual grupo deseja apostar? \n")
            ani.mostrar_animais() # Elaborar melhor essa lista
            animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
            if 0 <= animal_escolhido <= 24:
                Apostas.aposta = Grupo.lista_animais[animal_escolhido]
                Apostas.duro_cerc = dc.tipo
                break
            else:
                cc.erro()

class Apostas:
    
    aposta = ''
    duro_cerc = ''
    

