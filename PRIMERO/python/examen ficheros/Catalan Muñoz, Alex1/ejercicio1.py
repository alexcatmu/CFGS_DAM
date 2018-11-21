import struct
import binascii

def calcularLetras(cadena):
    contador_voc = 0
    for i in range(len(cadena)):

        if (cadena[i] == 'a' or cadena[i] == 'e' or cadena[i] == 'i' or \
            cadena[i] == 'o' or cadena[i] == 'u' or cadena[i] == 'A' or \
            cadena[i] == 'E' or cadena[i] == 'I' or cadena[i] == 'O' or \
            cadena[i] == 'U'):

                contador_voc += 1

    return contador_voc


def generarIndices(ficheroEntrada, ficheroSalida, formato):

    
    #print(datos)
    datos = ''
    primero = True
    while(datos != b'' or primero == True):
        primero = False
        
        print(ficheroEntrada.tell())
        puntero = ficheroEntrada.tell()
        datos = ficheroEntrada.read(formato.size)
        if (datos != b''):
            unpacked_data = formato.unpack(datos)
            unpacked_data = list(unpacked_data)
            unpacked_data[1] = unpacked_data[1].decode('utf-8').\
                               replace('\x00','')


            print(unpacked_data[1])
            cantidad_vocales = calcularLetras(unpacked_data[1])
            print(cantidad_vocales)


            if (cantidad_vocales > 25):
                ficheroSalida.write(str(puntero)+'\t')
                
                ficheroSalida.write(str(unpacked_data[0])+'\t')
                #print(unpacked_data[0])
                
                ficheroSalida.write(str(cantidad_vocales)+'\n')
                #print(cantidad_vocales)

                
                
                print()
                print()
            
        

def leerIndices(FicheroIndices, FicheroDatosBinarios, formato):

    indices_l = FicheroIndices.readline()

    while (indices_l != ''):
        arr_indices = indices_l.split('\t')

        vocales = arr_indices[2].replace('\n','')
        #print (arr_indices)
        indice = int(arr_indices[0])

        FicheroDatosBinarios.seek(indice,0)
        datos = FicheroDatosBinarios.read(formato.size)
        unpacked_data = formato.unpack(datos)
        unpacked_data = list(unpacked_data)
        unpacked_data[1] = unpacked_data[1].decode('utf-8').\
                           replace('\x00','')
        print('El codigo de letras '+str(unpacked_data[0])+' tiene '\
              +str(vocales)+' letras')
        print(unpacked_data[1])
        
        indices_l = FicheroIndices.readline()

        print()
        print()
    

    
'''
fp_open_bin= open('datosB.bin','rb')

fp_open_txt= open('indices.txt','w')

s=struct.Struct('i200s')

generarIndices(fp_open_bin, fp_open_txt, s)



fp_open_bin.close()
fp_open_txt.close()

'''

s=struct.Struct('i200s')

fp_open_bin = open('datosB.bin','rb')
fp_open_ind = open('indices.txt','r')

leerIndices(fp_open_ind,fp_open_bin, s)


fp_open_bin.close()
fp_open_ind.close()

























