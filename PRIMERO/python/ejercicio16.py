#.- Feu un programa que mostri els 50 primers nombres múltiples de 5

#programa multiplos de 5

#variables

i = 0
mult = 0
#codigo
'''
for i in range (51 * 5):
    if (mult % 5 == 0):
        print (mult)
    else:
        i = i-1
    mult = mult +1
'''

for i in range (51):
    print(i*5)

contador = 0
for i in range (51):
    print(contador)
    contador +=5
