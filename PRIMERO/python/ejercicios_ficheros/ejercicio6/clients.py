'''
2.2) Desenvolupeu un programa que creï un arxiu “clients.txt” amb
noms de persona. Doneu valors de forma directa ( no cal que els
                                                 demaneu per teclat).
Cada nom de persona ocupa una línia, i separem el nom i els cognoms
amb un tabulador:
	Jose<tab>Gomez<tab>Santos<enter>
	Maria<tab>Sanz<tab>Trementina<enter>
	Jesus<tab>Gomez<tab>Soler<enter>

El programa a continuació demanarà a l’usuari primer cognom d’una
persona, i a continuació el buscarà dins de l’arxiu. Si el troba,
mostrarà el nom complet de cadascuna de les persones que tenen el
cognom indicat. 
Un cop mostrats els nom trobats, el programa tornarà a demanar un
altre cognom a l’usuari.

PISTA 1: llegir la linea i fer un Split(“\t”)
'''

def rellenaCampos():
    array = [['hola','pablo','mira'],['como','haces','adios'],\
             ['yep','pepep','polo'],['polo','polo','polo'],\
             ['polo','polo','polo'],\
             ['polo','polo','polo'],['polo','polo','polo']]
    
    fp_nombres = open('nombres.txt','w')

    for i in range(len(array)):
        for j in range (len(array[i])):
            if (j != 2):
                fp_nombres.write(array[i][j]+'\t')
            else:
                fp_nombres.write(array[i][j]+'\n')

        
    fp_nombres.close()

    
def muestraCampos(palabra):

    fp_personas = open('nombres.txt','r')
    EOF = False

    while (EOF == False):
        linea = fp_personas.readline().rstrip('\n')
        if (linea != ''):
            array_linea = linea.split('\t')
            #print(array_linea)
            #print(array_linea[1])
            if (array_linea[1] == palabra):
                print(linea)
        else:
            EOF = True

    fp_personas.close()







rellenaCampos()
continuar = ''
while (continuar != 's'):
        
    palabra = input('Introduce un apellido: ')
    muestraCampos(palabra)

    continuar = input('s para salir: ')














