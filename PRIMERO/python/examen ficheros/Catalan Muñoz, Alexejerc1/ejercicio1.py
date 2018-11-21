def tratafichero():
    fp_leer1 = open('numerosSeguidos1.txt','r')
    fp_leer2 = open('numerosSeguidos2.txt','r')
    fp_leer3 = open('numerosSeguidos3.txt','r')
    
    fp_escribe = open('capicua.txt','w')
    
    fichero(fp_leer1,fp_escribe)
    fichero(fp_leer2,fp_escribe)
    fichero(fp_leer3,fp_escribe)

    fp_leer1.close()
    fp_leer2.close()
    fp_leer3.close()


def fichero(fp_leer1,fp_escribe):

    EOF = False
    while (EOF == False):

        if(EOF != ''):

            longitud = fp_leer1.read(2)
            #print(len(longitud))
            
            if (len(longitud) == 2):
            
                longitud = int(longitud)
                num_enter = fp_leer1.read(longitud)
                print(num_enter)
                print(longitud)
                num_enter = str(num_enter)
                cap_i_cua = comprueba_cap(num_enter)
                
                if (cap_i_cua == True):

                    fp_escribe.write(num_enter+'\n')
                    
            else:
                EOF = True
                
        else:
            EOF = True


def comprueba_cap(num_enter):

    longitud_m = len(num_enter) // 2
    primer_parte = num_enter[0:longitud_m]
    secon_parte = num_enter[longitud_m:]

    capi = True
    
    for i in range (len(primer_parte)):
        if (primer_parte[i] != secon_parte[len(secon_parte)-1-i]):

            capi = False

    print(capi)
    print()
    return capi






            

tratafichero()





















