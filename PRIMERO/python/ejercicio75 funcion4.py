'''
1.4) Creeu una funció “lecturaInterval” que faci una lectura
d’una xifra dins d’un interval. A la funció li passarem el
valor mínim del rang, el valor màxim, i ens tornarà un valor
llegit del teclat que estigui dins d’aquest rang. Com a l’exercici
anterior, fins que el nombre no estigui dins l’interval, la funció
continuarà demanat el nombre a l’usuari.
		double lecturaInterval(double minim , double maxim)‏

'''



#programa intervalos


#funciones

def lecturaInterval(minimo = 0, maximo = 0):

    numero = float(input("Introduce un numero dentro del intervalo: "))
    while (numero < minimo or numero > maximo):
        numero = float(input("Introduce un numero dentro del intervalo: "))

    return numero


#variables
minimo = 0
maximo = 3
resultado = 0

#codigo

resultado = lecturaInterval(minimo,maximo)

print(resultado)
