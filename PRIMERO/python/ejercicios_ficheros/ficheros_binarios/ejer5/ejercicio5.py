import struct
import binascii
'''
3.2) Una empresa de compra-venda necessita fer  una base de dades de
cotxes. Cada cotxe té les següent característiques:
identificador
model
marca
matricula
km
preu
estat ( de 0 a 10)‏
Quan el programa engega :
Feu un programa amb un menu principal que permeti fer les següents
operacions:
introduir cotxes ( es desaran a disc )‏
llistar els cotxes ( es llegiran de disc )‏
Cercar cotxes per identificador i matricula  ( podeu crear índex per a
cadascuna si voleu fer cerques més ràpides)‏
Editar les dades dels cotxes trobats, i desar-les de nou al disc.
'''

class coche:
    def __init__(self, ident = 0, model = '', marca = '', matr = '',\
                 km = 0.0, preu = 0.0, estat = 0):

        self.ident = ident
        self.model = model
        self.marca = marca
        self.matr = matr
        self.km = km
        self.preu = preu
        self.estat = estat


def escribeTodo():
    fp_escribeCoche = open('cocheBinario.bin','wb')

    array = []
    array.append(coche(12,'se','iunh','b3gfvb45', 23.0, 23.26, 4))
    array.append(coche(13,'sm','itgeh','b34ertv5', 523.0, 323.2, 8))
    array.append(coche(14,'si','iumh','b34vsd5', 235.0, 235.2, 6))
    array.append(coche(15,'su','iuklh','b3y5', 23.05, 234.2, 3))
    array.append(coche(16,'sy','iueu','b34y', 23.03, 23.42, 2))
    array.append(coche(17,'st','iuergfh','y345', 23.50, 523.2, 1))

    s= struct.Struct('i20s20s20sffi')

    datos = []

    for i in range (len(array)):
        datos = []

        datos.append(array[i].ident)
        datos.append((array[i].model).encode('utf-8'))
        datos.append((array[i].marca).encode('utf-8'))
        datos.append((array[i].matr).encode('utf-8'))
        datos.append(array[i].km)
        datos.append(array[i].preu)
        datos.append(array[i].estat)
        datos_binario = s.pack(*datos)

        fp_escribeCoche.write(datos_binario)
        



    fp_escribeCoche.close()

def leerbinario():

    fp_leeCoche = open('cocheBinario.bin','rb')
    s= struct.Struct('i20s20s20sffi')
    binari = fp_leeCoche.read(s.size)

    while (binari != b''):
        
        datos = s.unpack(binari)
        datos = list(datos)
            
        for i in range (7):
            
            if (isinstance(datos[i],int) == False and\
                isinstance(datos[i],float) == False):
                datos[i] = datos[i].decode('utf-8')

                datos[i] = datos[i].replace('\x00','')

            print(datos[i])
        
        binari = fp_leeCoche.read(s.size)
        print()
        print()

    fp_leeCoche.close()


def buscaCoches(identificado, matricula):
    fp_leeCoche = open('cocheBinario.bin','rb')
    s= struct.Struct('i20s20s20sffi')
    binari = fp_leeCoche.read(s.size)

    while (binari != b''):
        
        datos = s.unpack(binari)
        datos = list(datos)
        encontrado = False
        for i in range (7):
                
            if (isinstance(datos[i],int) == False and\
                isinstance(datos[i],float) == False):
                datos[i] = datos[i].decode('utf-8')

                datos[i] = datos[i].replace('\x00','')

            if (datos[i] == identificado or datos[i] == matricula):
                encontrado = True
        if (encontrado == True):
            print(datos)
        
        binari = fp_leeCoche.read(s.size)
        #print()
        #print()

    fp_leeCoche.close()


def buscaCoches(identificado, matricula):
    fp_leeCoche = open('cocheBinario.bin','rb+')
    s= struct.Struct('i20s20s20sffi')
    binari = fp_leeCoche.read(s.size)

    while (binari != b''):
        
        datos = s.unpack(binari)
        datos = list(datos)
        encontrado = False
        for i in range (7):
                
            if (isinstance(datos[i],int) == False and\
                isinstance(datos[i],float) == False):
                datos[i] = datos[i].decode('utf-8')

                datos[i] = datos[i].replace('\x00','')

            if (datos[i] == identificado or datos[i] == matricula):
                encontrado = True
                fp_leeCoche.seek(s.size*(-1),1)
                

                coche.ident= 9
                coche.ident = 'erfngieu'encode('utf-8'))
                datos.append((array[i].marca).encode('utf-8'))
                datos.append((array[i].matr).encode('utf-8'))
                datos.append(array[i].km)
                datos.append(array[i].preu)
                datos.append(array[i].estat)
                datos_binario = s.pack(*datos)

                
        if (encontrado == True):
            print(datos)
        
        binari = fp_leeCoche.read(s.size)
        #print()
        #print()

    fp_leeCoche.close()



escribeTodo()

#leerbinario()

ident_coche = 14
matricula = 'b3gfvb45'

buscaCoches(ident_coche, matricula)

modificaCoches(ident_coche,matricula)












