'''
2.8) Feu un programa que llegeixi una frase, i després la mostri eliminant
les lletres ‘a’ ( penseu que eliminar un caràcter representa
que la resta de la frase es desplaci a l’esquerra en el punt de
            l’eliminació, com si aprestéssiu a “suprimir” !)‏
'''



#programa suprimir

#variables

frase = ""
letra = ""
vector = []
cont = 0
frase_supr = ""

#codigo

frase = str(input())
vector = list(frase)
letra = "a"


for i in range (len(vector)):
    if (vector[i] == letra):
        cont = i
        while (cont < len(vector)):
            if (cont == len(vector)-1):
                vector[cont] = ""
            else:
                vector [cont] = vector[cont+1]
            cont = cont + 1


for i in range (len(vector)):
    frase_supr = frase_supr + vector[i]
    
print (frase_supr)

