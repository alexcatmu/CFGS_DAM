'''
1.5) Creeu una funció “esDigit” que, donat un caràcter qualsevol,
ens digui si és numèric o no. La funció rep un paràmetre char,
i retorna un valor int ( 1 si el caràcter és un número, 0 si no ho és).
		int esDigit(char caracter)‏
'''


#programa caracter digito


#funciones

def esDigit(caracter=''):
    
    if (ord(caracter) >= 48 and ord(caracter) <= 57):
        binario = 1
    else:
        binario = 0

    return binario



#variables
caracter = ''
cont = 0
numerico = True


#codigo

caracter = input("Introduce un numero o caracter: ")


cont = 0
while (cont < len(caracter) and numerico == True):
    
    resultado = esDigit(caracter[cont])
    cont = cont +1
    if (resultado == 0):
        numerico = False

print (resultado)

































