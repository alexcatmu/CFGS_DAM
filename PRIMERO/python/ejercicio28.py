#Crear un programa que dibuixi una escala d’asteriscos.
#Li passem l’altura de l’escala.
#Ex: 5

#programa asteriscos

#variables
aster = ""
cant = 0
i = 0
#codigo
cant = int (input())

for i in range (1,cant+1):
    aster = aster + "*"
    print (aster)

