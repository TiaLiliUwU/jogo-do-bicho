# Código para definir se a aposta será no duro ou no cercado
from cc import CustomConsole
cc = CustomConsole()

class DuroCercado:
    
    def __init__(self, tipo):
        self.tipo = tipo

    def duro_cerc(self):
        while True:
            cc.clear()
            print("Que tipo de aposta deseja fazer? \n\n1 - Duro\n2 - Cercado")
            duro_cercado = int(input("\nSelecione a alternativa: "))
            if duro_cercado == 1:
                self.tipo = True
                break
            elif duro_cercado == 2:
                self.tipo = False
                break
            else:
                cc.erro()


    
    