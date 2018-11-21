import os
import random
'''
4.3) Definiu un tipus de dades que permeti
emmagatzemar un article d’una ferreteria:
número de referència
nom d’article
preu
quantitat en magatzem
Creeu una llista de 5 articles,
i feu que el programa sigui capaç de llegir les dades de tots 5.
Tot seguit, el programa esborrarà la pantalla i mostrarà les
dades de tots els articles.
'''
#programa ferreteria


#variables

class ferreteria:
    def __init__(self, ref=0, nom="", preu=0, cuantitat=0):
        self.ref=ref
        self.nom=nom
        self.preu=preu
        self.cuantitat=cuantitat

i=0
ref=0
nom=""
preu=0
cuantitat=0
article=0
#codigo

l=[]
for i in range(5):
    ref=random.randint(0,120)
    nom=random.randint(0,120)
    preu = random.randint(0,120)
    cuantitat=random.randint(0,120)

         
    article=ferreteria(ref,nom,preu,cuantitat)

    l.append(article)



os.system('cls')

for i in range(5):
    
    print("Articulo",i+1,":",l[i].ref,l[i].nom,l[i].preu,l[i].cuantitat)







    























