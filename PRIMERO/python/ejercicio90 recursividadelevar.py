#programa de elevar



#funciones

def elevar(base,exp):

    if (exp == 0):
        return 1

    return base * elevar( base, exp - 1)

#variables

#codigo



print(elevar(2,5))
