lista_hello = ""
lista = "hola que tal hola hola"
array = list(lista)

for i in range (len(array)):
    if (array[i] == "h" and array[i+1] == "o" and array[i+2] == "l" and array[i+3] == "a"):
        array[i+1] = "e"
        array[i+2] = "ll"
        array[i+3] = "o"

for i in range (len(array)):
    lista_hello = lista_hello  + array[i]

print(lista_hello)
