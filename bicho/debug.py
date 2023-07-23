# Códigos malucos de debug
from cc import CustomConsole
cc = CustomConsole()
from aposta import Grupo, Apostas, Numero
a = Grupo()
ap = Apostas()
n = Numero()
from duro_cerc import DuroCercado
dc = DuroCercado(tipo=None)
from sorteio import Sorteio, Verificação
sort = Sorteio()
veri = Verificação()
from bichos import Animais
ani = Animais()

cc.clear()
n.terno_dezena()
print(ap.aposta)
sort.sortear_números()
veri.verificar_multi_num()
cc.enter()
cc.clear()