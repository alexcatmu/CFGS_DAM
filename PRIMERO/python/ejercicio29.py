'''
Crear un programa que dibuixi una escala de números, o
cada pis comença per 1 i acaba pel número de la base,
li passem l’altura: ex: 5
'''

#programa piramide numerica

#variables
suma = ""
#codigo

altura = int (input())

for i in range (1, altura+1):
    suma = suma + str(i)
    print (suma)
