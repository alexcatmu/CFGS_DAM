'''
tupla=(2,3,4,5)

print(tupla)



tupla = tupla[:len(tupla)-1]

print(tupla)


tupla = (2,3,4,5)

tupla = tupla + (6,7)

print(tupla)

tupla = (2,3,4,5)


tupla = tupla[:len(tupla)-1]
tupla = tupla,(tupla)
print(tupla)


tupla = (2,3,4,5)

tupla2=list(tupla)
tupla2.append(tupla)
tupla=tuple(tupla2)
print(tupla)

tupla=(2,3,4,5)

tupla=tupla[:2],tupla[2:]
print(tupla)
'''


#proteina, lipidos carbohidratos

#0.5 lipidos y carbos 15
la = [('cigrons',18,5,61),('bou',21.3,7.4,0),('rap',17,2,0),\
      ('pera',0.4,0.4,14),('manzana', 0,0,0)]

print(la)

cont = 0
encontrado = False
while(cont < len(la) and encontrado == False):

    if(la[cont][2]<= 0.5 and la[cont][3]<=15):
        print(la[cont])
        encontrado = True
    cont +=1
























