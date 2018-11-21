lista = "casa gabc"
tabla = list(lista)
i = 0
i2 = 0
letra_encontrada = False
print (lista)
while (i < len(tabla)):
    if (tabla[i] == "a"):
        letra_encontrada = True
        for i2 in range (i, len(tabla)):
            if (i2 + 1 < len(tabla)):
                tabla[i2] = tabla[i2 + 1]
                
    if (letra_encontrada == True):
        tabla[len(tabla)-1] = " "
        letra_encontrada = False
    i = i + 1
print (tabla)
