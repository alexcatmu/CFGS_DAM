#oivfn





def comprueba(num):

    repite = False

    auxiliar = num
    
    for i in range(num):

        ultimo_numero = auxiliar %10

        

        auxiliar = auxiliar / 10
        repite == False
        auxiliar2 = auxiliar
        ultimo_numero2 = auxiliar2 /10
        while (auxiliar2 > 9):
            print('hola')
            ultimo_numero2 = auxiliar2 % 10

            if (ultimo_numero == ultimo_numero2):

                repite = True
            auxiliar2 = auxiliar2/10

        

    return repite
    
def numeros():

    numeros = 22

    for i in range (numeros):

        repetir = comprueba(i)

        if (repetir == False):
            print(i)

print(1234%10)

numeros()










