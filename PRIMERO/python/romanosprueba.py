#programa numeros romanos

#variables
#romano = ""
num_rom = 0
num_fin = 0
aux = 0
cont_v = 0
cont_l = 0
cont_d = 0
cont_inicio = 1
#codigo

romano = input()


while (romano != "G"):

    
    if (romano == "I" or romano == "V" or romano == "X" or romano == "L" or romano == "C" or romano == "D" or romano == "M"):
        
        if (romano == "I"):
            num_rom = 1
    
        elif (romano == "V" and cont_v < 1):
            num_rom = 5
            cont_v = cont_v + 1

        elif (romano == "X"):
            num_rom = 10
        
        elif (romano == "L" and cont_l < 1):
            num_rom = 50
            cont_l = cont_l + 1
            
        elif (romano == "C"):
            num_rom = 100
            
        elif (romano == "D" and cont_d < 1):
            num_rom = 500
            cont_d = cont_d + 1
        
        elif (romano == "M"):
            num_rom = 1000

        if (cont_inicio == 1):
            aux = num_rom
            cont_inicio = cont_inicio + 1

        if (num_rom > aux):
            if (aux == 1 or aux == 10 or aux == 100 or aux == 1000):
                num_fin = num_rom - num_fin

        elif (num_rom <= aux):
            num_fin = num_fin + num_rom
                
        aux = num_rom
    romano = input()
    print (num_fin)
    
print (num_fin)
























