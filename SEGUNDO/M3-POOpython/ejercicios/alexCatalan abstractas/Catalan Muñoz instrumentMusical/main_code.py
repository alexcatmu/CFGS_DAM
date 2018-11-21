from trompeta import trompeta
from flauta import flauta

t = trompeta("metal")
f = flauta("pequeña")

print(t.tipusInstrument())
t.setFamilia("Metal")
f.setFamilia("plastico")

t.setBoquilla("Cuenco")
f.setFibra("Plastico")

print(t.tocar())
print(f.tocar())