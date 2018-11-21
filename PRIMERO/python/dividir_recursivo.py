#division con recursividad


#funciones


def division_coma (dividendo,divisor):

    if (dividendo < divisor):
        return 0
    

    else:
        return division_coma(dividendo-divisor, divisor) + 0.1


def division(dividendo, divisor, coma):

    
    if (dividendo <divisor and dividendo == 0):

        return 0

    elif (dividendo < divisor):
        dividendo = dividendo * 10
        return division_coma(dividendo - divisor, divisor) + 0.1
        
    else:
        return division(dividendo-divisor, divisor, coma) + 1





print(division(14,8, 0))
