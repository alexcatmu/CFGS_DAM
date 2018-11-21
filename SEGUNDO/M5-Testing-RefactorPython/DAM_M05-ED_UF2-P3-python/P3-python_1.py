
#P3_1

import os

def Calculo(num):
    if num==0:
        return num
    if num==1:
        return num
    else:
        valor=1
        for i in range (1,num+1):
            valor=valor*i
        
        return valor



if __name__ == "__main__":

    nre=int(input())
    print("El factorial es: ",Calculo(nre))
    nre=int(input())
    print("El factorial es: ",Calculo(nre))
    
