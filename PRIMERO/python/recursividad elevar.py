#elevar a su propio numero recursividad


def elevar(base,exponente):

    if (exponente == 0):
        return 1
    


    return base*elevar(base, exponente -1)



print(elevar(2,4))

