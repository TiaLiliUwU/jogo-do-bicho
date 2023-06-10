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

# função duro ou cercado
def duro_cerc():
    clear()
    print("Que tipo de aposta deseja fazer? \n\n1 - Duro\n2 - Cercado")
    duro_cercado = int(input("\nSelecione a alternativa: "))
    tipo = True
    if duro_cercado == 1:
        tipo = True
    elif duro_cercado == 2:
        tipo = False
    else:
        erro()
        enter()
        return duro_cerc()
    return tipo

# Função para realizar o sorteio
def sortear():
    sorteios_ani = []
    while len(sorteios_ani) < 5:
        animal = random.choice(list(animais.keys()))  # Escolhe um animal aleatoriamente
        if animal not in sorteios_ani:
            sorteios_ani.append(animal)
    sorteios_num = []
    while len(sorteios_num) < 5:
        numero = random.choice(range(0, 9999))  # Escolhe um número aleatoriamente para o animal escolhido
        numero_formatado = str(numero).zfill(4)
        if numero_formatado not in sorteios_num:
            sorteios_num.append(numero_formatado)
    
    return sorteios_ani, sorteios_num

# Função "Aposta no grupo"
def grupo():
    tipo_aposta = duro_cerc()
    clear()
    print("Em qual grupo deseja apostar? \n")
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
    return animal_escolhido, tipo_aposta

# Função "Aposta no duque do grupo"
def duque_grupo():
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
    if animal_escolhido_2 in range(len(animais)):
        pass
    else:
        erro()
        enter()
        clear()
        return grupo()
    return animal_escolhido_1, animal_escolhido_2

# Função "Aposta no terno do grupo"
def terno_grupo():
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
    if animal_escolhido_2 in range(len(animais)):
        pass
    else:
        erro()
        enter()
        clear()
        return grupo()
    animal_escolhido_3 = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
    if animal_escolhido_3 in range(len(animais)):
        pass
    else:
        erro()
        enter()
        clear()
        return grupo()
    return animal_escolhido_1, animal_escolhido_2, animal_escolhido_3


# Função para solicitar a aposta do jogador
def fazer_aposta():
    print("Qual aposta você quer realizar? \n\n1 - Grupo \n2 - Duque de grupo \n3 - Terno de grupo\n")
    tipo_aposta = int(input("Selecione a opção desejada: "))
    if tipo_aposta == 1:
        fezes = grupo()
        verific_tipo_aposta = 0
    elif tipo_aposta == 2:
        fezes = duque_grupo()
        verific_tipo_aposta = 1
    elif tipo_aposta == 3:
        verific_tipo_aposta = 2
        fezes = terno_grupo()
    else:
        erro()
    return fezes, verific_tipo_aposta
    #for indice, animal in enumerate(animais, start=1):
    #    print(f"{indice}. {animal}")
    #animal_escolhido = int(input("\nDigite o número correspondente ao animal desejado: ")) - 1
    #if animal_escolhido in range(len(animais)):
    #    range_animal = list(animais.values())[animal_escolhido]
    #else:
    #    erro()
    #    enter()
    #    clear()
    #    return fazer_aposta()
    #valor_aposta = float(input("\nDigite o valor da aposta: "))
    #if valor_aposta in range_animal:
    #    pass
    #else:
    #    erro()
    #    enter()
    #    clear()
    #    return fazer_aposta()
    #return animal_escolhido, valor_aposta

# Função para verificar aposta no duro/grupo
def duro_grupo(animal_apostado, animal_sorteado, numero_sorteado):
    if animal_sorteado[0] == animal_apostado:
        print("Parabéns! Você ganhou!")
        print(f"O animal sorteado foi {animal_sorteado} e o número sorteado foi {numero_sorteado}.")
    else:
        print("Que pena! Você perdeu.")
        print(f"O animal sorteado foi {animal_sorteado} e o número sorteado foi {numero_sorteado}.")

# Função para verificar aposta cercado/grupo
def cerc_grupo(animal_apostado, animal_sorteado, numero_sorteado):
    if any(item in animal_apostado for item in animal_sorteado):
        print("Parabéns! Você ganhou!")
        print(f"O animal sorteado foi {animal_sorteado} e o número sorteado foi {numero_sorteado}.")
    else:
        print("Que pena! Você perdeu.")
        print(f"O animal sorteado foi {animal_sorteado} e o número sorteado foi {numero_sorteado}.")

# Função para verificar aposta no duque do grupo
def duque_gp():
    pass

# Função para verificar se o jogador ganhou ou perdeu
def verificar_resultado(aposta, resultado):
    dds, verific_tipo_aposta = aposta
    if dds[1] == True:
        a1, a2 = dds 
    elif dds[1] == False:
        a1, a2 = dds 
    elif len(dds) == 3:
        a1, a2, a3 = dds 
    animal_sorteado, numero_sorteado = resultado
    if verific_tipo_aposta == 0: # No grupo
        animal_apostado = list(animais.keys())[a1]
        if a2 == True: # aposta no duro
            duro_grupo(animal_apostado, animal_sorteado,numero_sorteado)
        elif a2 == False: # aposta no cercado
            cerc_grupo(animal_apostado, animal_sorteado, numero_sorteado)
    elif verific_tipo_aposta == 1: # No duque de grupo
        animal_apostado = []
        animal_apostado_temp = list(animais.keys())[a1]
        animal_apostado.append(animal_apostado_temp)
        animal_apostado_temp = list(animais.keys())[a2]
        animal_apostado.append(animal_apostado_temp)
        print(animal_apostado) #debug
        enter() #debug
        duque_gp()

# Função principal do jogo
def jogar_jogo_do_bicho():
    print("Bem-vindo ao Jogo do Bicho! \n")
    aposta = fazer_aposta()
    print(aposta) #debug
    enter() #debug
    resultado = sortear()
    print(resultado) #debug
    enter() #debug
    verificar_resultado(aposta, resultado)

# ______Execução do jogo______

clear()
print('Estamos em teste alpha, nem sabemos oq vai funcionar ou não. Paciência')
jogar_jogo_do_bicho()
enter()
clear()