import time



tiempo = time.strftime("%c")

print (tiempo)
tiempo2 = time.strftime("%c")

while (tiempo == tiempo2):
    tiempo2 = time.strftime("%c")


cont = 0
tiempo = time.strftime("%c")
print(tiempo)
while (cont < 30):
    tiempo2 = time.strftime("%c")
    if (tiempo != tiempo2):
        tiempo = tiempo2
        cont = cont +1
    
print(tiempo)
print(cont)
print(tiempo2)
'''
while (True):
    
    tiempo = time.strftime("%c")
    
    print (tiempo)
    cont = cont +1
    print (cont)
    '''
    
