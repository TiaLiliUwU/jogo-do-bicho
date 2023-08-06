# Código para definir se a aposta será no duro ou no cercado
from cc import CustomConsole
cc = CustomConsole()
import questionary # tem que instalar

class DuroCercado:
    
    def __init__(self, tipo):
        self.tipo = tipo

    def duro_cerc(self):

        opcoes = [
            {"name": "Duro", "value": "opcao1"},
            {"name": "Cercado", "value": "opcao2"},
        ]

        cc.clear()
        duro_cercado = questionary.select("Que tipo de aposta deseja fazer?\n", choices=opcoes, instruction=' ', qmark='*').ask()
        if duro_cercado == 'opcao1':
            self.tipo = 1
        elif duro_cercado == 'opcao2':
            self.tipo = 0


    
    