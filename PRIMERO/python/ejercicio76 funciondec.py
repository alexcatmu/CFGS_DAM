'''
1.11)  Ara que ja sabem fer un “llegirXifraSencera”, el repte és ara
escriure la funció “llegirXifraReal”. Considereu els següents aspectes:
El separador decimal ( punt o coma ) serà configurable, ens el passaran
com paràmetre char.
Haureu de controlar quantes vegades ens posen el separador decimal.
Només el podeu admetre una vegada. 
'''




#funciones

def llegirXifraSencera():
    dec = input("Indica el tipus de separador decimal: ")
    num = input()
    totalint = 0
    totaldec = 0
    numdec = 0
    contdec = 0
    total = 0.0

        
    while ((ord(num)>= 48 and ord(num) <= 57) or \
           (contdec <= 0 and num == dec )):

        if (num == dec):
            numdec = input()
            while (ord(numdec) >= 48 and ord(numdec) <= 57):
                numdec = int(numdec)
                totaldec = (totaldec * 10) + numdec
                
                numdec = input()
                contdec = contdec + 1

        else:
            num = int(num)
            totalint = (totalint * 10) + num
            num = input()

    
    for i in range (contdec):
        totalint = totalint * 10

    

    totalint = totalint + totaldec

    for i in range(contdec):
        totalint = totalint / 10


    
    return totalint




#programa


total = llegirXifraSencera()


print(total)







