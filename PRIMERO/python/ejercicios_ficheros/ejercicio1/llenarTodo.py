'''
1.2) Usant els arxius generats al problema anterior, feu un programa
que fusioni “parells.txt” i “senars.txt” en un tercer arxiu “1a100.txt”,
intercalant una línia de senars, i una dels parells.
'''

#funiones

def rellenarDOS():

    fp_lleno = open('intercala.txt','w')
    fp_par = open('par.txt','r')
    fp_senar = open('senar.txt','r')
    EOF = False
    cont = 0
    while (EOF == False):
        linea_par = fp_par.readline()
        linea_senar = fp_senar.readline()
        
        if (linea_par == '' and linea_senar == ''):
            EOF = True

        else:
            
            fp_lleno.write(linea_par)
            fp_lleno.write(linea_senar)
            print(linea_par,end="")
            print(linea_senar,end="")


    fp_lleno.close()
    fp_par.close()
    fp_senar.close()

#programa principal


rellenarDOS()






