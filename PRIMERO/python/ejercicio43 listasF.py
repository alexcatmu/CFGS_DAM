'''
hasta que no F seguir con - \ | /
'''

#programa F

#variables

array = ["-","\ ","|","/"]
valor = ""
cont = 0

#codigo

while (valor != "F"):
    print (array[cont])
    #array_final.append(array[cont])
    cont = cont + 1
    if (cont > 3):
        cont = 0
        
    valor = input()


#print (array_final)
