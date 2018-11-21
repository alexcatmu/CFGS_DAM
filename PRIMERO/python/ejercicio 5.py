
'''
Donada una entrada per teclat corresponent a la nota numèrica d’un examen,
el programa ens imprimirà per pantalla la qualificació textual corresponent:
Menor de 5 : 		Insuficient
De 5 a 6(no inclòs): 		Suficient
De 6 a 7(no inclòs) 		Bé
De 7 a 8’5(no inclòs) 	Notable
De 8’5 a 10(no inclòs) 	Excel·lent
10 			Matricula d’honor
'''

#programa de notas

#variables

nota = 0
res = "a"



#codigo

print ("Introduce la nota del alumno")
nota = float(input())

if (nota < 0):
    res = "Nota mal introducida. Mínimo 0"
elif (nota < 5):
    res = "Insuficiente"
elif (nota < 6):
    res = "Suficiente"
elif (nota < 7):
    res = "Bé"
elif (nota < 8.5):
    res = "Notable"
elif (nota < 10):
    res = "Excelente"
elif (nota == 10):
    res = "Matricula de honor"
else:
    res = "Nota mal introducida. Máximo 10"
print (res)










