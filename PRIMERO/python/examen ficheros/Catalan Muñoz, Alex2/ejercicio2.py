import binascii
import struct

def leerBinario(fichero_bin, formato):

    altura = fichero_bin.read(formato.size)
    unpacked_data = formato.unpack(altura)
    files = unpacked_data[0]
    print(files)

    
    
    ancho = fichero_bin.read(formato.size)
    unpacked_data = formato.unpack(ancho)
    columnes = unpacked_data[0]
    print(columnes)    

    datos = fichero_bin.read(formato.size)
    cont = 1
    while (datos != b''):
        

        unpacked_data = formato.unpack(datos)

        if (cont == files):
            print(unpacked_data[0],end='\n')
            cont = 1
        else:
            print(unpacked_data[0],end='\t')
            cont +=1
        
        datos = fichero_bin.read(formato.size)
        



def modificaBinario(fichero_bin, formato,numero):
    
    altura = fichero_bin.read(formato.size)
    unpacked_data = formato.unpack(altura)
    files = unpacked_data[0]
    print(files)

    
    
    ancho = fichero_bin.read(formato.size)
    unpacked_data = formato.unpack(ancho)
    columnes = unpacked_data[0]
    print(columnes)    

    datos = fichero_bin.read(formato.size)
    cont = 1
    while (datos != b''):
        

        unpacked_data = formato.unpack(datos)
        if (unpacked_data[0]<numero):

            fichero_bin.seek(formato.size*(-1),1)
            unpacked_data = list(unpacked_data)
            unpacked_data[0] = 1

            packed_data = formato.pack(unpacked_data[0])
            fichero_bin.write(packed_data)

            
        if (cont == files):
            print(unpacked_data[0],end='\n')
            cont = 1
        else:
            print(unpacked_data[0],end='\t')
            cont +=1
            
        datos = fichero_bin.read(formato.size)
       



fp_open = open('matBin.bin','rb')

s = struct.Struct('i')

leerBinario(fp_open,s)

fp_open.close()




fp_open = open('matBincopia.bin','rb+')
numero = 150

modificaBinario(fp_open,s,numero)

fp_open.close()






















