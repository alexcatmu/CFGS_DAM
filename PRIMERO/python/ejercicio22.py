#) Feu un programa que ens digui quants nombres divisibles per
#7 hi ha entre el 300 i el 400  ( ambdós inclosos )‏

#programa multiplos de 7

#variables
i = 0
cont = 0
#codigo


for i in range (300,401):
    if (i % 7 == 0):
        cont = cont + 1

print (cont)
