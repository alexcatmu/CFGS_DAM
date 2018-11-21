#Crear un programa que dibuixi una piràmide de * donat una altura.
#Ex:5 fixeu-vos la base.

#programa arbol navidá

#variables
i = 0 #primer contador para altura
espa = 0 #espacios que debe tener cada linea (numerico)
espacio= ""#espacios y asteriscos que hay en cada línea
aster = 1#contador de asteriscos que hay en cada línea
j=0#contador para espacios
k=0#contador para asteriscos

#codigo

total = int (input())
i = 0
espa = total-1
espacio= ""
aster = 1

while (i < total):
    j = 0
    espacio = ""
    
    while (j < espa):
        espacio = espacio + " "
        j = j + 1

    k=1
    
    while (k <= aster):
        espacio = espacio + "*"
        k = k + 1
        
    aster = aster +2
    i = i + 1
    espa = espa -1
    print (espacio)
