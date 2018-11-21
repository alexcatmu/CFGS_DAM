'''
Un fitxer seqüencial de text de nom persones.txt conté una
línia per cada persona. La informació que es guarda d’una
persona és: DNI i data de naixement. Per exemple:
33268858 25 3 1995
60985496 9 12 1979
89050083 17 12 1953
Dissenya una funció que llegeixi la informació del fitxer
Media:persones.txt i escrigui al fitxer filtrat.txt els DNIs
ordenats de petit a gran de les persones nascudes entre anyInici
i anyFi (ambdós anys inclosos).
def filtreDni (anyInici, anyFi):
	"""
	>>> filtreEdat(1999,2005)
	>>> f1=open('filtrat.txt','r')
	>>> llista =f1.read().split()
	>>> llista == ['10005903', '14999875', '21160449',
	'28281002', '30927410', '47491163', '66230500', '83459619',
	'99176324']
	True
	"""
'''


def Creapersonas():
    fp_personas = open('personas.txt','w')
    array = [[33268858, 25, 3, 1995],[60985496,9, 12, 1979]\
             ,[89050083, 17, 12, 1953]]

    for i in range (len(array)):
        for j in range (len(array[i])):
            if (j == len(array[i])-1):
                fp_personas.write(str(array[i][j]))
            else:
                fp_personas.write(str(array[i][j])+'\t')
            
        fp_personas.write('\n')
        
    fp_personas.close()
    
def comparapersonas(num1,num2):

    fp_personas = open('persones.txt','r')
    EOF = False
    cont = 0
    while (EOF == False):
        linea = fp_personas.readline()
        if (linea != ''):
            linea = linea.rstrip('\n')
            
            linea = linea.split(' ')
            #print(linea)
            if (int(linea[3]) >= num1 and int(linea[3]) <= num2):
                print(linea)
            cont += 1
        else:
            EOF = True













#Creapersonas()
comparapersonas(1975,1980)




