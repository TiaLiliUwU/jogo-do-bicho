# Códigos malucos de debug
from cc import CustomConsole
cc = CustomConsole()
from aposta import Grupo, Apostas
a = Grupo()
ap = Apostas()
from duro_cerc import DuroCercado
dc = DuroCercado(tipo=None)
from sorteio import Sorteio, Verificação
sort = Sorteio()
veri = Verificação()
from bichos import Animais
ani = Animais()

cc.clear()
a.terno_grupo()
print(ap.aposta)
sort.sortear_animais()
veri.verificar_multi_grupo()
cc.enter()
cc.clear()
