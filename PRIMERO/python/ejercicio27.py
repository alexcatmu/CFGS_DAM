'''
2) Volem fer un programa que ens mostri una
taula de multiplicar com per exemple la
que es mostra a continuació:
'''

#programa tabla multiplicar

#variables
tabla = " "

#codigo

for i in range (1,10):
    tabla = " "
    for cont in range (1,10):
        mult = cont * i
        tabla = tabla + str(mult) + " "
    print ("Tabla del",i,":",tabla)
