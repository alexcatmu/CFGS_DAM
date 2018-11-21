'''
2.2) Usant la funció anterior, feu un programa que mostri 100 nombres
primers.
'''


#funciones

def primos100(lista):

    primos = 0
    cont1 = 2
    cont2 = 0
    primo = True
    #cont_ciclos = 0
    
    while (primos < 100 ):
        cont2 = 2
        primo = True

        while (cont2 <= cont1/2 and primo == True):
            if (cont1 % cont2 == 0):
                primo = False
                
            cont2 = cont2 +1
            #cont_ciclos +=1


        if (primo == True):
            lista.append(cont1)
            primos = primos +1
            
        cont1 = cont1 +1

    print(cont_ciclos)

#programa primos


lista_primo = []

primos100(lista_primo)

print(lista_primo)







































