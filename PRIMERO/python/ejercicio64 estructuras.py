import math
#programa coordenadas


#variables
class coordenada:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y



#codigo

        #manera para empezar a hacerlo
'''
ini=coordenada()

ini.x=int(input("Introduce la coordenada iniciar X: "))
ini.y=int(input("Introduce la coordenada a iniciar Y: "))


fin=coordenada()

fin.x=int(input("Introduce la coordenada fin X: "))
fin.y=int(input("Introduce la coordenada fin Y: "))

print("X inicial:",ini.x,"\t","X final:",ini.y)
print("Y inicial:", fin.x, "\t","Y final:",fin.y)



puntX=(fin.x-ini.x)
puntX = puntX * puntX

puntY=(fin.y-ini.y)
puntY = puntY*puntY

print(math.sqrt(puntY+puntX))
'''

#otra manera mas correcta de hacerlo

x=int(input("Introduce la coordenada iniciar X: "))
y=int(input("Introduce la coordenada a iniciar Y: "))
ini=coordenada(x,y)


x=int(input("Introduce la coordenada fin X: "))
y=int(input("Introduce la coordenada fin Y: "))
fin=coordenada(x,y)


print("X inicial:",ini.x,"\t","X final:",ini.y)
print("Y inicial:", fin.x, "\t","Y final:",fin.y)



puntX=(fin.x-ini.x)
puntX = puntX * puntX

puntY=(fin.y-ini.y)
puntY = puntY*puntY

print(math.sqrt(puntY+puntX))







        
