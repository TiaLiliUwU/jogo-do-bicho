# Codado por Yosemite

# Precisa ser feito: sistema com todos os tipos de apostas; tabela completa dos bichos
###################################################

import random, os

# Comando Clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#
# Aperte enter para continuar
def enter():
    input('\nAperte enter para continuar...')
    clear()
#
# Mensagem de erro
def erro():
    print('\nSelecione uma opção válida...')
    enter()
#

# Definição dos animais e seus respectivos números
animais = {
    "Avestruz": range(1, 4),
    "Águia": range(5, 8),
    "Burro": range(9, 12),
    "Borboleta": range(13, 16),
    "Cachorro": range(17, 20),
    "Cabra": range(21, 24),
    "Carneiro": range(25, 28),
    "Camelo": range(29, 32),
    "Cobra": range(33, 36),
    "Coelho": range(37, 40),
    "Cavalo": range(41, 44),
    "Elefante": range(45, 48),
    "Galo": range(49, 52),
    "Gato": range(53, 56),
    "Jacaré": range(57, 60),
    "Leão": range(61, 64),
    "Macaco": range(65, 68),
    "Porco": range(69, 72),
    "Pavão": range(73, 76),
    "Peru": range(77, 80),
    "Touro": range(81, 84),
    "Tigre": range(85, 88),
    "Urso": range(89, 92),
    "Veado":range(93, 96),
    "Vaca": range(97, 100),
}

# Função para realizar o sorteio
def sortear():
    animal = random.choice(list(animais.keys()))  # Escolhe um animal aleatoriamente
    numero = random.choice(animais[animal])  # Escolhe um número aleatoriamente para o animal escolhido
    return animal, numero

#Função para verificar se o animal está dentro da tabela
#def verific_animal():
    while True:
        if verific_ani in range(len(animais)):
            break
        else:
            erro()
            enter()
            clear()
            print("\nOpção inválida. Tente novamente.")

# Função "Aposta no grupo"
def grupo():
    print("\nEm qual grupo deseja apostar? \n")
    for indice, animal in enumerate(animais, start=1):
        print(f"{indice}. {animal}")
    animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
    if animal_escolhido in range(len(animais)):
        pass
    else:
        erro()
        enter()
        clear()
        return grupo()
    return animal_escolhido

# Função "Aposta no duque grupo"
def grupo():
    print("\nEm quais grupos deseja apostar? \n")
    for indice, animal in enumerate(animais, start=1):
        print(f"{indice}. {animal}")
    animal_escolhido_1 = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
    if animal_escolhido_1 in range(len(animais)):
        pass
    else:
        erro()
        enter()
        clear()
        return grupo()
    animal_escolhido_2 = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
    return animal_escolhido_1, animal_escolhido_2


# Função para solicitar a aposta do jogador
def fazer_aposta():
    print("Animais disponíveis: \n")
    for indice, animal in enumerate(animais, start=1):
        print(f"{indice}. {animal}")
    animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
    if animal_escolhido in range(len(animais)):
        range_animal = list(animais.values())[animal_escolhido]
    else:
        erro()
        enter()
        clear()
        return fazer_aposta()
    valor_aposta = float(input("\nDigite o valor da aposta: "))
    if valor_aposta in range_animal:
        pass
    else:
        erro()
        enter()
        clear()
        return fazer_aposta()
    return animal_escolhido, valor_aposta

# Função para verificar se o jogador ganhou ou perdeu
def verificar_resultado(aposta, resultado):
    animal_apostado_num, _ = aposta # Isso tá errado de acordo com a lógica do jogo, tem que refazer.
    animal_apostado = list(animais.keys())[animal_apostado_num]
    animal_sorteado, numero_sorteado = resultado
    if animal_apostado.lower() == animal_sorteado.lower():
        print("Parabéns! Você ganhou!")
        print(f"O animal sorteado foi {animal_sorteado} e o número sorteado foi {numero_sorteado}.")
    else:
        print("Que pena! Você perdeu.")
        print(f"O animal sorteado foi {animal_sorteado} e o número sorteado foi {numero_sorteado}.")

# Função principal do jogo
def jogar_jogo_do_bicho():
    print("Bem-vindo ao Jogo do Bicho! \n")
    aposta = fazer_aposta()
    resultado = sortear()
    verificar_resultado(aposta, resultado)

# ______Execução do jogo______

clear()
jogar_jogo_do_bicho()
enter()
clear()