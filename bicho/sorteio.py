# Código para sortear e verificar
import random
from bichos import Animais
ani = Animais()
from aposta import Apostas
a = Apostas()

# Fazer algoritmo de geração de sorteios procedural
# Verificação
class Verificação(): # Refatorar o código transformando a verificação de dezena, centena e milhar em uma coisa só!
    
    lista_animais = list(ani.animais.keys())
    
    @staticmethod
    def verificar_multi_num():

        ultimos_dois_digitos = [numero % 100 for numero in Sorteio.sorteios_num]
        print("Esses foram os números sorteados: ", Sorteio.sorteios_num_formatado)
        if all(elemento in ultimos_dois_digitos for elemento in a.aposta):
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_milhar():

        print("Esses foram os números sorteados: ", Sorteio.sorteios_num_formatado)
        if a.duro_cerc == False and a.aposta in Sorteio.sorteios_num:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == True and a.aposta == Sorteio.sorteios_num[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("Você perdeu... Tente novamente!")

    @staticmethod
    def verificar_centena():

        ultimos_tres_digitos = [numero % 1000 for numero in Sorteio.sorteios_num]
        print("Esses foram os números sorteados: ", Sorteio.sorteios_num_formatado)
        if a.duro_cerc == False and a.aposta in ultimos_tres_digitos:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == True and a.aposta == ultimos_tres_digitos[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("Você perdeu... Tente novamente!")

    @staticmethod
    def verificar_dezena():
        
        ultimos_dois_digitos = [numero % 100 for numero in Sorteio.sorteios_num]
        print("Esses foram os números sorteados: ", Sorteio.sorteios_num_formatado)
        if a.duro_cerc == False and a.aposta in ultimos_dois_digitos:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == True and a.aposta == ultimos_dois_digitos[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("Você perdeu... Tente novamente!")

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
    sorteios_num_formatado = []

    @staticmethod
    def sortear_animais():
        
        while len(Sorteio.sorteios_ani) < 5:
            animal = random.choice(list(ani.animais.keys()))
            if animal not in Sorteio.sorteios_ani:
                Sorteio.sorteios_ani.append(animal)

    @staticmethod
    def sortear_números():
        while len(Sorteio.sorteios_num) < 5:
            numero = random.randrange(10000)
            numero_formatado = f"{numero:04d}"
            if numero_formatado not in Sorteio.sorteios_num_formatado:
                Sorteio.sorteios_num_formatado.append(numero_formatado)
                Sorteio.sorteios_num.append(numero)