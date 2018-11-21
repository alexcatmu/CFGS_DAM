'''
1.8) Feu un programa que demani una llista de notes
( fins que l’usuari entri una nota negativa ), 
Un cop entrades, mostrarà les notes en ordre invers al d’entrada. 
mostrarà la nota mitja 
mostrarà la variància, que es calcula amb la següent fórmula

		x = mitja de tots els nombres
		xi = i-èssim número de la llista
		n = mida de la llista

	d) finalment el programa mostrarà la
	desviació típica( ):  = (variancia)‏
	Podeu usar la funció sqrt(num) de la llibreria math,
	fer un “import math” a l’inici del codi.

Exemple: 2, 3, 6, 8, 11.
-> (2+3+6+8+11)/5 media -> (2^2+3^3+6^6+8^8+11^11) – media^2 = desviació típìca -> Varianza =  Arrel quadradada(desviació típica)
'''


#programa complicaete arrays

#variables

nota = 0
array1 = []
array2 = []
longitud = 0
suma = 0
media = 0
numero = 0
cont = 0
total_exp = 0
suma_expNot = 0
desvia_tipica = 0
varianza = 0
aux = 0
tot_vari = 0
#codigo

print ("Introduce una lista de notas")
nota = int (input())

while (nota >= 0):#comprobamos que creamos un array hasta que la nota sea negativa
    array1.append(nota)#vamos añadiendo los datos al array
    nota = int(input())#pedimos las notas al usuario
print (array1)#imprimos el array para comprobar que hemos cogido bien las notas

longitud = len(array1) -1 #declaramos la longitud del segundo array(para darle la vuelta al array)
for i in range (len(array1)):#recorremos el array1 que es el creado al inicio
    array2.append(array1[longitud])#creamos el segundo array dandole la vuelta
    longitud = longitud -1#la longitud es para empezar por el ultimo dato del array1 y le vamos restando uno a longitud
#imprimimos el array del reves
print (array2)

for i in range (len(array1)):#hacemos la media
    suma = suma + array1[i]#sumamos los datos del array en sus posiciones

media = suma / len(array1)#calculamos la media

print ("La media de las notas es:",media)

#estp es para la varianza
for i in range (len(array1)):
    numero = array1[i]#cogemos cada numero del array le restamos la media y lo multiplicamos por él mismo(cuadrado)
    cont = 1
    vari = numero - media
    tot_vari = tot_vari + (vari*vari)
varianza = tot_vari / len(array1)#dividimos la suma por la cantidad de notas


print ("Esto es la varianza:",varianza)

#varianza = 9

desvia_tipica = varianza
aux = 0
while (aux != desvia_tipica):#esto es la raiz cuadrada de la varianza que es la desviacion tipica
    aux = desvia_tipica
    desvia_tipica = (varianza/desvia_tipica + desvia_tipica) / 2

print ("Esta es la desvia_tipica:",desvia_tipica)














    


