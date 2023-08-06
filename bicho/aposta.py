# Código para obter a aposta do jogador
from bichos import Animais
ani = Animais()
from duro_cerc import DuroCercado
dc = DuroCercado(tipo=None)
from cc import CustomConsole
cc = CustomConsole()
import questionary # tem que instalar
 
# Preciso urgentemente fazer uma forma do usuário visualizar sua aposta
class Numero:

    dezenas_input = []

    @staticmethod
    def multi_dezena(selec):

        Numero.dezenas_input = []
        for _ in range(selec):
            while True:
                cc.clear()
                print("Aposte em duas dezenas entre 00 e 99? \n")
                num_escolhida = int(input("\nDigite a dezena de aposta: "))
                if 0 <= num_escolhida <= 99:
                    if num_escolhida not in Numero.dezenas_input:
                        Numero.dezenas_input.append(num_escolhida)
                        break
                    else:
                        print("\nVocê já escolheu essa dezena. Por favor, escolha outra...")
                        cc.enter()  
                else:
                    cc.erro()
        Apostas.aposta = Numero.dezenas_input

    @staticmethod
    def mono_num(selec):

        if selec == 1:
            rang = [0, 99]
        elif selec == 2:
            rang = [100, 999]
        elif selec == 3:
            rang = [1000, 9999]

        dc.duro_cerc()
        while True:
            cc.clear()
            print(f"Aposte em uma dezena entre {rang[0]} e {rang[1]}? \n")
            num_escolhida = int(input("\nDigite a dezena de aposta: "))
            if rang[0] <= num_escolhida <= rang[1]:
                num_escolhida_formatada = "{:02d}".format(num_escolhida) # Isso aqui vai ficar aqui pq preciso elaborar a vizualização da aposta!
                Apostas.aposta = num_escolhida
                Apostas.duro_cerc = dc.tipo
                break
            else:
                cc.erro()

class Grupo:

    @staticmethod
    def select_ani():

        numeros_utilizados = set()
        opcoes = []
        num_opcao = 0

        for animal, numeros in ani.animais.items():
            numeros_nao_utilizados = [num for num in numeros if num not in numeros_utilizados]
            numeros_formatados = ', '.join(f'{numero % 100:02}' for numero in numeros_nao_utilizados)
            if numeros_nao_utilizados:
                opcoes.append({"name": f"{animal} - {str(numeros_formatados)}", "value": f"{num_opcao}"})
                numeros_utilizados.update(numeros_nao_utilizados)
                num_opcao += 1
        
        op = questionary.select("Selecione o animal desejado:\n", choices=opcoes, instruction=' ', qmark='*').ask()
        return int(op)

    @staticmethod
    def grupo(selec):

        Apostas.write_aposta = 1
        Apostas.aposta = []
        if selec == 1:
            dc.duro_cerc()
            Apostas.duro_cerc = dc.tipo
            Apostas.aposta = Grupo.select_ani()
        else:
            for _ in range(selec):  
                while True:
                    cc.clear()
                    animal_escolhido = Grupo.select_ani()
                    if animal_escolhido not in Apostas.aposta:
                        Apostas.aposta.append(animal_escolhido)
                        break
                    else:
                        print("\nVocê já escolheu esse grupo. Por favor, escolha outra...")
                        cc.enter()

class Apostas:
    
    aposta = ''
    duro_cerc = ''
    write_aposta = ''