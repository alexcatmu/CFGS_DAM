import gc

def hacerciclo():
    l=[0]
    l[0]=l

recolector = gc.collect()
print("colectado %d"%recolector)
for i in range(10):
    hacerciclo()

recolector = gc.collect()
print("colectado %d"%recolector)