# Código para obter a aposta do jogador
from bichos import Animais
ani = Animais()
from duro_cerc import DuroCercado
dc = DuroCercado(tipo=None)
from cc import CustomConsole
cc = CustomConsole()
 
# Preciso urgentemente fazer uma forma do usuário visualizar sua aposta
# Apostas em números - posso refatorar e transformar duque e terno em uma coisa só, certeza! Provavelmente o mesmo pra dezena, centena e milhar
class Numero:

    dezenas_input = []

    @staticmethod
    def terno_dezena():

        Numero.dezenas_input = []
        for _ in range(3):
            while True:
                cc.clear()
                print("Aposte em três dezenas entre 00 e 99? \n")
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
        #Numero.dezenas_input = ["{:02d}".format(num) for num in Numero.dezenas_input]
        Apostas.aposta = Numero.dezenas_input

    @staticmethod
    def duque_dezena():

        Numero.dezenas_input = []
        for _ in range(2):
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
        #Numero.dezenas_input = ["{:02d}".format(num) for num in Numero.dezenas_input]
        Apostas.aposta = Numero.dezenas_input

    @staticmethod
    def milhar():

        dc.duro_cerc()
        while True:
            cc.clear()
            print("Aposte em um milhar entre 1000 e 9999? \n")
            num_escolhida = int(input("\nDigite a dezena de aposta: "))
            if 1000 <= num_escolhida <= 9999:
                Apostas.aposta = num_escolhida
                Apostas.duro_cerc = dc.tipo
                break
            else:
                cc.erro()
    
    @staticmethod
    def centena():

        dc.duro_cerc()
        while True:
            cc.clear()
            print("Aposte em uma centena entre 100 e 999? \n")
            num_escolhida = int(input("\nDigite a dezena de aposta: "))
            if 100 <= num_escolhida <= 999:
                Apostas.aposta = num_escolhida
                Apostas.duro_cerc = dc.tipo
                break
            else:
                cc.erro()

    @staticmethod
    def dezena():

        dc.duro_cerc()
        while True:
            cc.clear()
            print("Aposte em uma dezena entre 00 e 99? \n")
            num_escolhida = int(input("\nDigite a dezena de aposta: "))
            if 0 <= num_escolhida <= 99:
                num_escolhida_formatada = "{:02d}".format(num_escolhida) # Isso aqui vai ficar aqui pq preciso elaborar a vizualização da aposta!
                Apostas.aposta = num_escolhida
                Apostas.duro_cerc = dc.tipo
                break
            else:
                cc.erro()

# Apostas em Grupo - posso refatorar e transformar duque e terno em uma coisa só, certeza!
class Grupo:

    lista_animais = list(ani.animais.keys())
    animais_input = []
    animais_conv = []

    @staticmethod
    def terno_grupo():

        Apostas.write_aposta = 1
        Apostas.aposta = []  
        for _ in range(3):  
            while True:
                cc.clear()
                print("Em quais grupos deseja apostar? \n")
                ani.mostrar_animais()
                animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
                if 0 <= animal_escolhido <= 24:
                    if animal_escolhido not in Grupo.animais_input:
                        Apostas.aposta.append(animal_escolhido)
                        break
                    else:
                        print("\nVocê já escolheu esse grupo. Por favor, escolha outra...")
                        cc.enter()  
                else:
                    cc.erro()

    @staticmethod
    def duque_grupo():

        Apostas.write_aposta = 1
        Apostas.aposta = []  
        for _ in range(2):  
            while True:
                cc.clear()
                print("Em quais grupos deseja apostar? \n")
                ani.mostrar_animais()
                animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
                if 0 <= animal_escolhido <= 24:
                    if animal_escolhido not in Grupo.animais_input:
                        Apostas.aposta.append(animal_escolhido)
                        break
                    else:
                        print("\nVocê já escolheu esse grupo. Por favor, escolha outra...")
                        cc.enter()  
                else:
                    cc.erro()
            
    
    @staticmethod
    def grupo():

        dc.duro_cerc()
        Apostas.write_aposta = 1
        while True:
            cc.clear()
            print("Em qual grupo deseja apostar? \n")
            ani.mostrar_animais()
            animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
            if 0 <= animal_escolhido <= 24:
                Apostas.aposta = animal_escolhido
                Apostas.duro_cerc = dc.tipo
                break
            else:
                cc.erro()

class Apostas:
    
    aposta = ''
    duro_cerc = ''
    write_aposta = ''