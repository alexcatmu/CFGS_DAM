'''
Volem fer un programa que donades dues entrades numèriques per teclat:
 any  ( p.ex. 1998)‏
 mes (1-gener, 2 febrer, 3-març....) 
ens indiqui per pantalla quants dies té aquest mes en concret.
Nota: Tingueu en compte que pels anys de traspàs febrer té 29 dies.
 Com a recordatori:
'''



# cuantos días tiene el mes del año que indiquemos


#variables

ano = 0 #año que se introduce
mes = 0 #mes que se quiere saber los dias
dias = 0 #los dias que tiene el mes

#codigo

print ("Escribe un año")#pedimos que el usuario escriba un año por pantalla
ano = int (input())
print ("Escribe el numero del mes que quieres")# pedimos el mes 
mes = int (input())

if (mes < 1 or mes > 12): #miramos que sea un dato correcto
    print ("Has introducido un dato erroneo")
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12): # meses con 31 dias
    dias = 31
    print ("El mes ", mes , " del año ", ano, " tiene ", dias, " días")#Imprimimos el resultado
elif (mes == 2):#miramos del mes febrero si es bisiesto o no
    if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):#bisiesto
            dias = 29
            print ("El mes ", mes , " del año ", ano, " tiene ", dias, " días")#Imprimimos el resultado
    else:#no bisiesto
            dias = 28
            print ("El mes ", mes , " del año ", ano, " tiene ", dias, " días")#Imprimimos el resultado
else:#meses con 30 dias
    dias = 30
    print ("El mes ", mes , " del año ", ano, " tiene ", dias, " días")#Imprimimos el resultado




























