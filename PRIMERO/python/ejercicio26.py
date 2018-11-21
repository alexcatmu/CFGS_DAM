#Volem fer un programa que ens mostri per pantalla el llistat
#dels números primers que hi ha entre el 1 i el 1000

#programa primos hasta 1000

#variables
i = 2
cont = 2
primo = True
#codigo

for i in range (2,1001):
    primo = True
    cont = 2
    while (i > cont):
        if (i % cont == 0):
            primo = False
        cont = cont + 1
    if (primo == True):
        print (i)
