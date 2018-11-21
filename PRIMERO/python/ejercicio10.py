'''
2)  Un instal·lador de xarxa cobra segons hores treballades i
metres de cable instal·lats. Assumirem que el preu per hora són
30€ l’hora i el preu per metre del cable és 0,5€. Aquestes dues
quantitats són fixes (CONSTANTS).
El programa ens haurà de demanar:
 les hores treballades 
 el número de metres instal·lats
 i ens traurà per pantalla:
 el preu brut és .... 
 el preu amb IVA és ....
'''
#instalador de redes

#variables


#codigo


PREUHORA = 30
METROCABLE = 0.5
IVA = 0.21

print ("¿Cuantas horas has trabajado?")
hora = int (input())

print ("¿Cuantos metros has instalado?")
metros = float (input())

preciobruto = (hora * PREUHORA) + (metros * METROCABLE)
print ("El precio bruto es:",preciobruto)
precioiva = preciobruto + (preciobruto * IVA)
print ("El precio total con iva es:", precioiva)

