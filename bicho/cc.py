# Código para gerenciar menus interativos que funcionam no terminal de qualquer sistema operacional
import os

class CustomConsole:
# Comando Clear
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

#  Comando aperte para continuar
    @staticmethod
    def enter():
        input('\nAperte enter para continuar...')
        CustomConsole.clear()

# # Comando de erro
    @staticmethod
    def erro():
        print('\nSelecione uma opção válida...')
        CustomConsole.enter()