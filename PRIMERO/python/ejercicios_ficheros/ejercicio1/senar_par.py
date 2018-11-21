'''
1.1) Feu un programa que escrigui a l’arxiu “parells.txt” els nombres
parells de l’1 al 100, i en “senars.txt” els senars de l’1 al 100.
'''

#funiones

def ParellSenar(limite):

    
    fp_par = open('par.txt','w')
    fp_senar = open('senar.txt','w')
    
    for i in range (limite):
        if (i % 2 == 0):
            introduce = str(i) + "\n"
            fp_par.write(introduce)
           
        else:
            
            introduce = str(i) + "\n"
            fp_senar.write(introduce)
            
    fp_senar.close()
    fp_par.close()
#programa principal

limit = 100

ParellSenar(limit)




