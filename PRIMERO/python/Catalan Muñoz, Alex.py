#examen rapido


def leerNumeroStr():

    numero_S = '1020004'

    numero = numero_S

    return numero


def eliminarNumDer(numero):


    num_borra = ''
    for i in range(len(numero)-1):
        num_borra = num_borra + numero[i]



    return num_borra


def esDivisible(numero,div):

    numero = int(numero)
    if (numero % div == 0):
        return True

    else:
        return False



def esPolidivisible(numero):

    numero_con = True
    numero = int(numero)

    while (numero_con and int(numero) > 10):

        numero_con = esDivisible(numero,len(str(numero)))
        #print('hh')
        if (numero_con):
            numero = eliminarNumDer(str(numero))


        else:

            resul = 'No'

    if (numero_con):
        resul= 'Polidivisible'

    else:
        resul = 'NO'


    return resul
#programa

numero = leerNumeroStr()

print(esPolidivisible(numero))



    










