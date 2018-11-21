'''
6)  En una empresa necessiten un petit programa que permeti
calcular l’import que han de pagar als treballadors. Els pagaments es
fan de forma setmanal.
 Per a cada assalariat es recullen via teclat les següents dades:
 Número d’hores setmanals treballades a la setmana
 Preu per hora ( és diferent per a cada treballador )‏
Es considera que un treballador comença a fer hores extres a partir
de la hora 36 (la 35 és part de l’horari setmanal). Les hores extres
es paguen un 50% més que les hores normals.

El programa ha d’imprimir per pantalla l’import final, tenint en compte el preu
hora indicat i si hi ha hores extres o no.
'''




#Dinero que tienen que cobrar los trabajadores


#variables

limite = 35 # Las horas que contamos como normales
horas = 0 # Horas de trabajo realizadas a la semana
Phora = 0 # Precio de la hora realizada

#codigo



print ("Número de horas trabajadas a la semana")
horas = int (input())
print ("Precio por hora")
Phora = float (input())

if (horas < 0): 
    print ("No vas a cobrar ná porque no has currao vago")
    sueldo = 0
    
elif (horas < limite): #Aqui no hay horas extras realizadas
    sueldo = horas * Phora
    print ("No has hecho horas extra")
elif (horas >= limite): #Aqui se han realizado horas extras
    sueldo = limite * Phora # se aplica el sueldo a las horas que no son extras
    horas = horas - limite # Se calculan las horas extras que se realizan
    sueldo = sueldo + (Phora * 1.5 * horas) #Se suma las horas no extras
    print ("Has hecho horas extra")         # y se calcula el sueldo de las  
                                            # horas extra y se suma
print (sueldo) #Aqui imprimimos el sueldo






