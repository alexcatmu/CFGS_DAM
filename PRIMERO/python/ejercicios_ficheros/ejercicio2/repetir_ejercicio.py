'''
) Feu un programa que demani dades de vàries persones , i les vagi desant
a un arxiu “persones.txt”. Les dades de cada persona seran
(useu una estructura):
 nom
 cognoms 
 NIF
 edat
 alçada ( en metres, p.ex: 1.63 )‏
El procés s’atura quan l’usuari indica que no vol introduir més
persones. El programa tindrà com a mínim les funcions llegirPersona
i escriurePersonaADisc-
Podem eliminar el salt de línia de la línia llegida amb
“string”.rstrip("\n")
1.4) Escriviu un programa que llegeixi l’arxiu “persones.txt”
creat a l’exercici anterior, i mostri totes les dades de les persones
majors de 18 anys per pantalla
'''
#clases y funciones
class personas():
    def __init__(self, nom = '', cognoms = '', NIF = '', edat = '',\
                 altura=''):
        self.nom = nom
        self.cognoms = cognoms
        self.NIF = NIF
        self.altura = altura



def introduce_personas(personas):

    personas.nom = input('Nombre: ')
    personas.cognoms = input('Apellidos: ')
    personas.NIF = input('NIF: ')
    personas.edat = input('Edat: ')
    personas.altura = input('Altura(m): ')

def escribir_persona(pers, fp_personas):
    
    fp_personas.write(pers.nom+' ')
    fp_personas.write(pers.cognoms+' ')
    fp_personas.write(pers.NIF+' ')
    fp_personas.write(pers.edat+' ')
    fp_personas.write(pers.altura+'\n')

    



###programa principal
'''
parar = False
fp_personas = open('introduce_personas.txt','w')

rellena_persona = personas()

while (parar == False):

    introduce_personas(rellena_persona)
    print(rellena_persona.nom)
    escribir_persona(rellena_persona,fp_personas)
    salir = input('S para salir: ')
    if (salir == 'S' or salir == 's'):
        parar = True
        fp_personas.close()
   ' 
'''
    
fp_personas = (open('introduce_personas.txt','r'))

EOF = False
cont = 0
array_lineas = ['yy']
while (EOF == False):

    array_lineas[0] = fp_personas.readline()

    if (array_lineas[0] == ''):
        EOF = True
    cont = 0
    for i in range(len(array_lineas[0])):
        if (array_lineas[0][i] == ' '):
            cont += 1
            if (cont == 3):
                
                if (int(array_lineas[0][i+1]) < 2):
                    if (int(array_lineas[0][i+2]) >= 8):
                        print(array_lineas)

                if (int(array_lineas[0][i+1]) >= 2):
                        print(array_lineas)

fp_personas.close()











    






