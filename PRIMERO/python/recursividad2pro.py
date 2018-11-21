def potencia(num,exp):

    if (exp == 0):
        return 1

    else:

        return num * (potencia(num,exp-1))




def potencia_opt(num,exp):


    if (exp == 0):
        return 1


    if (exp%2 == 0):

        return potencia(num,exp/2) * potencia(num,exp/2)

    elif (exp%2 == 1):

        return potencia(num,(exp-1)/2) * potencia(num,(exp-1)/2) * num




print(potencia(3,4))

print(potencia_opt(3,4))






















