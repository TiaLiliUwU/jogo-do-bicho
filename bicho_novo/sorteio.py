# Código para sortear e verificar
import random
from bichos import Animais
ani = Animais()
from aposta import Apostas
a = Apostas()

# Verificação
class Verificação():
    
    lista_animais = list(ani.animais.keys())

    @staticmethod
    def verificar_multi_grupo():
        
        print("Esses foram os animais sorteados: ", Sorteio.sorteios_ani)
        if all(elemento in Sorteio.sorteios_ani for elemento in a.aposta):
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_grupo():
        
        print("Esses foram os animais sorteados: ", Sorteio.sorteios_ani)
        if a.duro_cerc == False and a.aposta in Sorteio.sorteios_ani:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == True and a.aposta == Sorteio.sorteios_ani[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("Você perdeu... Tente novamente!")

# Sorteios
class Sorteio:

    sorteios_ani = []
    sorteios_num = []

    @staticmethod
    def sortear_animais():
        
        while len(Sorteio.sorteios_ani) < 5:
            animal = random.choice(list(ani.animais.keys()))
            if animal not in Sorteio.sorteios_ani:
                Sorteio.sorteios_ani.append(animal)

    @staticmethod
    def sortear_números():
        while len(Sorteio.sorteios_num) < 5:
            numero = random.choice(range(0, 9999))  # Escolhe um número aleatoriamente para o animal escolhido
            numero_formatado = str(numero).zfill(4)
            if numero_formatado not in Sorteio.sorteios_num:
                Sorteio.sorteios_num.append(numero_formatado)