
numero = input('introduce el numero')

fp_loteria = open('loteria.txt','r')
fp_escribe = open('premios.txt','w')
EOF = False

while (EOF == False):
    leer_linea = fp_loteria.readline()
    if (leer_linea != ''):
        leer_linea = leer_linea.rstrip('\n')
        a_linea = leer_linea.split()
        #print(a_linea)
        cont = 0
        for i in range(len(a_linea)):
        
            if (i != 0):
            
                num_lot = a_linea[i][4]
                if (num_lot == numero and cont == 0):
                    print(a_linea[0],a_linea[i], 'es el premi', i)
                    a = a_linea[0]+' '+a_linea[i]+ ' es el premi '+ str(i)
                    print(a)
                    cont += 1
                    fp_escribe.write(a+'\n')
                    

    else:
        EOF = True


fp_escribe.close()
fp_loteria.close()
