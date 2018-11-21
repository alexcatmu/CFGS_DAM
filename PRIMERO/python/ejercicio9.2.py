'''
1.2) Dissenya un programa que, donat un nombre enter,
determini si aquest és el doble d'un nombre imparell.
(Exemple: 14 és el doble de 7, que és imparell.)
'''


#programa de dobes

#variables
res = "par"
mitad = 0
num = 0

#codigo

print ("Escribe un numero entero")
num = int (input())

res = "par"
mitad = num / 2

if (mitad % 2 != 0):
    res = "impar"
    
print (num, "es el doble de", mitad,"que es",res)
