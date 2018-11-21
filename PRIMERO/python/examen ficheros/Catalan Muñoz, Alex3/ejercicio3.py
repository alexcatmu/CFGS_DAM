import binascii
import struct

def leerBinario(fichero_bin, formato,v,p):

    fichero_bin.seek(0,2)
    limite = fichero_bin.tell()
    fichero_bin.seek(0,0)
    dato = fichero_bin.read(formato.size)
    matriz_bonsequips = []
    
    while(dato != b''):

        if (dato != b''):
            unpacked_data = formato.unpack(dato)


            if (unpacked_data[2] > v and unpacked_data[3] < p):

                unpacked_data = list(unpacked_data)
                unpacked_data[0]= unpacked_data[0].decode('utf-8').\
                                  replace('\x00','')

                unpacked_data[1]= unpacked_data[1].decode('utf-8').\
                                  replace('\x00','')
                matriz_bonsequips.append(unpacked_data)
                #print(unpacked_data)
                

        dato = fichero_bin.read(formato.size)

    #print(matriz_bonsequips)
    ordenaMatriz(matriz_bonsequips)


def ordenaMatriz(matriz):

    for i in range(len(matriz)):
        print(matriz[i])

    for i in range(len(matriz)):
        for j in range(len(matriz)):

            if(j+1 < len(matriz)):
                
                if (matriz[j+1][0] > matriz[j][0]):
                    print ('eee')
                    aux = matriz[j]
                    matriz[j] = matriz[j+1]
                    matriz[j+1] = aux



    print()
    print()
    print()
    
    for i in range(len(matriz)):
        print(matriz[i])
            

            




fp_open = open('NBA.bin','rb')

s = struct.Struct('25s10sBB')

victorias = 15

perdidas = 5

leerBinario(fp_open,s,victorias, perdidas)

fp_open.close()
