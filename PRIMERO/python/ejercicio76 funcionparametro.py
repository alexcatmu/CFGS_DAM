'''

2.1) Programeu la funció 
	 int esPrimer( int numero )
	 que ens diu si numero és primer o no ( retorna un 1 si
	 ho és, 0 si no)‏

'''



#programa primo parametro

#funciones

def esPrimer(lista):

    for i in range(len(lista)):
        cont = 2
        primario = True
        print("aaaa")
        numero = lista[i]
        while (cont < numero and primario == True):
            if (numero % cont == 0):
                numero = 0
                primario = False
            cont = cont+1

        if (primario == True):
            numero=1
            
        lista[i]=numero


#programa


array_numeros = [2,3,8,123,54,3,7,23,9]

esPrimer(array_numeros)



print(array_numeros)






































