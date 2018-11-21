'''
a) Farem un programa que llegeixi del teclat un número múltiple de 10.
No acceptarem el número fins que sigui múltiple de deu, si no ho és,
el tornem a demanar.
'''

#programa multiple de 10

#variables
num = 3
cont = 0
#codigo

while (num %10 != 0):
    print ("Escribe un número múltiplo de 10")
    num = float (input())

cont = 0
while (num > 100):
    num = num / 10
    cont = cont + 1
print (num, "por 10 elevado a:",cont)

