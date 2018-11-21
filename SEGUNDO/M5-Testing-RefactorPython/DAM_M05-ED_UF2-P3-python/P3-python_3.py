
#P3_3

import os

if __name__ == "__main__":

    print("Indica la edad: ",end='')
    edad=int(input())
    if (edad>=0 and edad<=14):
        cont=1
    elif(edad>=15 or edad<=64):
        cont=2
    elif(edad>=65 and edad<=200):
        cont=3
    
    if (cont==1):
        print("Indica el tipo de asiento: ",end='')
        asiento=str(input())
        if (asiento=='pl'):
            precio = 60*30/100
            print("El precio final es: "+str(precio)+" euros")
        elif (asiento=='lt'):
            precio = 50*30/100
            print("El precio final es: "+str(precio)+" euros")
        elif (asiento=='1p'):
            precio = 40*30/100
            print("El precio final es: "+str(precio)+" euros")
        else: #(asiento=='2p'):
            precio = 30*30/100
            print("El precio final es: "+str(precio)+ " euros")
    elif(cont==2):
        print("Indica el tipo de asiento: ",end='')
        asiento=str(input())
        if (asiento=='pl'):
            precio=60
            print("El precio final es: "+str(precio)+ " euros")
        elif (asiento=='lt'):
            precio=50
            print("El precio final es: "+str(precio)+ " euros")
        elif (asiento=='1p'):
            precio = 40
            print("El precio final es: "+str(precio)+ " euros")
        else: #(asiento=='2p'):
            precio = 30
            print("El precio final es: "+str(precio)+ " euros")
    elif(cont==3):
        print("Indica el tipo de asiento: ",end='')
        asiento=str(input())
        if (asiento=='pl'):
            precio = 60*50/100
            print("El precio final es: "+str(precio)+ " euros")
        elif (asiento=='lt'):
            precio = 50*50/100
            print("El precio final es: "+str(precio)+ " euros")
        elif (asiento=='1p'):
            precio = 40*50/100
            print("El precio final es: "+str(precio)+ " euros")
        else: #(asiento=='2p'):
            precio = 30*50/100
            print("El precio final es: "+str(precio)+ " euros")
    
        
		    
