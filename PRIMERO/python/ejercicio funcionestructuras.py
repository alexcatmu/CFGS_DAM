'''
2.12) Treball amb estructures/classes com a paràmetres de funcions
a) Declareu una estructura+typedef amb el nom Factura que tingui els
següents camps:
número de referència ( p.ex. 3423 )‏
nom del client
import total
nom del producte
referència del producte ( p.ex. 234AFRD2 )‏
unitats del producte ( nombre sencer )‏
preu de la unitat ( € )‏
b) Creeu dins del main un array de Factura, de longitud 5.
c) Creeu dues funcions:
	1) una funció que demani a l’usuari les dades i ompli la
	informació d’una factura:
			void omplirFactura( Factura f )‏

	2) una funció per a mostrar per pantalla totes les dades d’una
	factura:
			void mostrarFactura(Factura f)‏
d) Proveu les funcions anteriors des del main, donant valor a totes les
factures de l’array i mostrant-les posteriorment per pantalla.
e) feu una funció que busqui una factura dins d’un array de factures,
donat un número de refèrencia. Proveu-la en el main.
		int buscaFactura( Factura llista[ ], int 					numeroRefBuscat )‏

La funció retorna la posició de l’array on ha trobat la factura amb
el numero de referència especificat, o bé -1 si no n’ha trobada cap.  
'''
#estructuras
class factura:
    def __init__(self, num_ref=0, nom_cli='', import_total=0, \
                 nom_prod='', ref_prod='', unitats=0, preu_unit=0):

        self.num_ref=num_ref
        self.nom_cli = nom_cli
        self.import_total = import_total
        self.nom_prod = nom_prod
        self.ref_prod = ref_prod
        self.unitats = unitats
        self.preu_unit = preu_unit

#funciones


def omplirFactura(fac):
    fac.num_ref = int(input('num_ref: '))
    fac.nom_cli = input('nom_cli: ')
    fac.import_total = float(input('import_total: '))
    fac.nom_prod = input('nom_prod: ')
    fac.ref_prod = input('ref_prod: ')
    fac.unitats = int(input('unitats: '))
    fac.preu_unit = float(input('preu_unit: '))
    


    #fac = factura(num_ref,nom_cli,import_total,nom_prod,\
                             # ref_prod, unitats, preu_unit)
    
    #array_factura.append(factura_cliente)

def mostrarFactura(factura):


    print(factura.num_ref, factura.nom_cli, \
          factura.import_total, factura.nom_prod,\
          factura.ref_prod, factura.unitats,\
          factura.preu_unit)
    

def buscaFactura(array_factura, num_referencia):

    encontrada = False
    for i in range (len(array_factura)):

        if (array_factura[i].num_ref == num_referencia):

            devolver = i
            encontrada = True

    if (encontrada == False):
        devolver = -1

    return devolver

#programa principal
        
array_factura = []

for i in range (5):
    array_factura.append(factura())
    omplirFactura(array_factura[i])
    
    mostrarFactura(array_factura[i])



numero_referencia = int(input('numero_referencia: '))

x=(buscaFactura(array_factura,numero_referencia))#variable con el numero
                                                #en la posicion del array

if (x == -1):
    print('El numero de referencia proporcionado no es válido')

else:

    print(array_factura[x].num_ref,array_factura[x].nom_cli,\
          array_factura[x].import_total,array_factura[x].nom_prod,\
          array_factura[x].ref_prod,array_factura[x].unitats,\
          array_factura[x].preu_unit)























