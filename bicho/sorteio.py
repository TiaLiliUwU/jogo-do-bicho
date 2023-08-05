# Código para sortear e verificar
import random
from bichos import Animais
ani = Animais()
from aposta import Apostas
a = Apostas()
from algoritmo import Algoritmo

# Verificação
class Verificação(): # Refatorar o código transformando a verificação de dezena, centena e milhar em uma coisa só!

    animais_aposta_conv = []

    @staticmethod
    def convert():
        
        lista_animais = list(ani.animais.keys())

        if isinstance(a.aposta, list):
            for animal in a.aposta:
                Verificação.animais_aposta_conv.append(lista_animais[animal])
        else:
            Verificação.animais_aposta_conv = lista_animais[a.aposta]

        
     
    @staticmethod
    def verificar_multi_num():

        ultimos_dois_digitos = [numero % 100 for numero in Sorteio.sorteios_num]
        print("\nEsses foram os números sorteados: ", ", ".join(Sorteio.sorteios_num_formatado))
        if all(elemento in ultimos_dois_digitos for elemento in a.aposta):
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_milhar():

        print("\nEsses foram os números sorteados: ", ", ".join(Sorteio.sorteios_num_formatado))
        if a.duro_cerc == 0 and a.aposta in Sorteio.sorteios_num:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == 1 and a.aposta == Sorteio.sorteios_num[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_centena():

        ultimos_tres_digitos = [numero % 1000 for numero in Sorteio.sorteios_num]
        print("\nEsses foram os números sorteados: ", ", ".join(Sorteio.sorteios_num_formatado))
        if a.duro_cerc == 0 and a.aposta in ultimos_tres_digitos:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == 1 and a.aposta == ultimos_tres_digitos[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_dezena():
        
        ultimos_dois_digitos = [numero % 100 for numero in Sorteio.sorteios_num]
        print("\nEsses foram os números sorteados: ", ", ".join(Sorteio.sorteios_num_formatado))
        if a.duro_cerc == 0 and a.aposta in ultimos_dois_digitos:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == 1 and a.aposta == ultimos_dois_digitos[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_multi_grupo():
        
        Verificação.convert()
        print("\nEsses foram os animais sorteados: ", ", ".join(Sorteio.sorteios_ani))
        if all(elemento in Sorteio.sorteios_ani for elemento in Verificação.animais_aposta_conv):
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_grupo():
        
        Verificação.convert()
        print("\nEsses foram os animais sorteados: ", ", ".join(Sorteio.sorteios_ani))
        if a.duro_cerc == 0 and Verificação.animais_aposta_conv in Sorteio.sorteios_ani:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == 1 and Verificação.animais_aposta_conv == Sorteio.sorteios_ani[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

# Sorteios
class Sorteio:

    sorteios_ani = []
    sorteios_num = []
    sorteios_num_formatado = []

    @staticmethod
    def sort():

        Algoritmo.get_local()
        Algoritmo.get_previsao()

        numero = 0
        for num in Algoritmo.dds_alg:
            numero = (numero * 1497) + int(num)
        numero = numero % (10 ** 20)
        for _ in range(5):
            Sorteio.sorteios_num.append(numero % 10000)
            numero //= 10000
        Sorteio.sorteios_num.reverse()
        Sorteio.sorteios_num_formatado = [str(numero).zfill(4) for numero in Sorteio.sorteios_num]
        get_animal = [num % 100 for num in Sorteio.sorteios_num]
        for numero in get_animal:
            animais_encontrados = [animal for animal, numeros in ani.animais.items() if numero in numeros]
            Sorteio.sorteios_ani.extend(animais_encontrados)