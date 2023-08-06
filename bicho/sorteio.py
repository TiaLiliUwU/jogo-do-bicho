# Código para sortear e verificar
import random
from bichos import Animais
ani = Animais()
from aposta import Apostas
a = Apostas()
from algoritmo import Algoritmo
from cc import CustomConsole
cc = CustomConsole()

# Verificação
class Verificação():

    animais_aposta_conv = []

    @staticmethod
    def vizualizer_num():

        cc.clear()
        print("Sua aposta: ")
        if isinstance(a.aposta, list):
            print(">>", ", ".join(a.aposta), "\n")
        else:
            print(f">> {a.aposta}\n")

        print("Esses foram os números sorteados: ")
        print(">>", ", ".join(Sorteio.sorteios_num_formatado))

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
        Verificação.vizualizer_num()
        if all(elemento in ultimos_dois_digitos for elemento in a.aposta):
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")
    
    @staticmethod
    def verificar_mono_num(selec):

        if selec == 1:
            verific = [numero % 100 for numero in Sorteio.sorteios_num]
        elif selec == 2:
            verific = [numero % 1000 for numero in Sorteio.sorteios_num]
        elif selec == 3:
            verific = Sorteio.sorteios_num
        
        Verificação.vizualizer_num()
        if a.duro_cerc == 0 and a.aposta in verific:
            print("\nParabéns, você ganhou!")
        elif a.duro_cerc == 1 and a.aposta == verific[0]:
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def vizualizer_ani():

        print("Sua aposta: ")
        if isinstance(Verificação.animais_aposta_conv, list):
            print(">>", ", ".join(Verificação.animais_aposta_conv), "\n")
        else:
            print(f">> {Verificação.animais_aposta_conv}\n")

        print("Esses foram os animais sorteados: ")
        print(">>", ", ".join(Sorteio.sorteios_ani))

    @staticmethod
    def verificar_multi_grupo():
        
        Verificação.convert()
        Verificação.vizualizer_ani()
        if all(elemento in Sorteio.sorteios_ani for elemento in Verificação.animais_aposta_conv):
            print("\nParabéns, você ganhou!")
        else:
            print("\nVocê perdeu... Tente novamente!")

    @staticmethod
    def verificar_grupo():
        
        Verificação.convert()
        Verificação.vizualizer_ani()
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