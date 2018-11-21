class producte:#producte podemos poner el que queramos
    def __init__(self, nom="",preu=0):#self siempre y luego las variables y el tipo de variables
        self.nom = nom#declaramos el nombre de variables con self.nombredevariables
        self.preu = preu#declaramos el nombre de variable con self.nombredevariable

'''
proba = producte('oli',10.25)
print("producte",proba.nom,proba.preu)


proba.preu = 14.260

print("producte", proba.nom, proba.preu)


prodB = producte('pila',10.30)

print ("producte", prodB.nom,prodB.preu)



prodC = producte()
print ("Producte",prodC.nom,prodC.preu)
'''

prodA = producte('oli',10.25)
prodB = producte('lapiz',10.25)

prodA = prodB#ahora la variable prodA y probD ES LA MISMA VARIABLES 

print(prodA.nom)
print(prodB.nom)
prodA.nom = "Tomate"
print(prodA.nom)
print(prodB.nom)




