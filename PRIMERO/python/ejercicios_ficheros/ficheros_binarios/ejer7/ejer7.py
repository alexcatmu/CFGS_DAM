import binascii
import struct

def rellenabinario():

    fp_open = open('rellena.bin','wb')

    s=struct.Struct('10s10sii10s')

    array = [['hol','ados',1,2,'yp'],['hla','adis',15,20,'ep'],\
             ['hla','adis',4,3,'ye'],['ho','adio',11,32,'p'],\
             ['hla','adi',6,29,'ep'],['hol','adio',16,52,'tyep']]
    
    
    for i in range (len(array)):
        datos = []
        datos.append(array[i][0].encode('utf-8'))
        datos.append(array[i][1].encode('utf-8'))
        datos.append(array[i][2])
        datos.append(array[i][3])
        datos.append(array[i][4].encode('utf-8'))

        packed_data = s.pack(*datos)

        fp_open.write(packed_data)

    fp_open.close()

def muestrabinario():

    fp_open = open('rellena.bin','rb')

    s=struct.Struct('10s10sii10s')

    datos = fp_open.read(s.size)
    
    while (datos != b''):
        datos_fin = s.unpack(datos)
        
        datos_fin = list(datos_fin)
        
        for i in range (len(datos_fin)):

            if(isinstance(datos_fin[i],int)==False):
                datos_fin[i]=datos_fin[i].decode('utf-8').replace('\x00','')

        print(datos_fin)
        datos = fp_open.read(s.size)


def cambiaBinario():

    fp_open=open('rellena.bin','rb+')

    s=struct.Struct('10s10sii10s')
    fp_open.seek(0,2)
    long = fp_open.tell()
    fp_open.seek(0,0)
    mover = fp_open.read(s.size)
    while(mover!= b''):
        
        
        
        unpack_mover = s.unpack(mover)
        unpack_mover = list(unpack_mover)
        unpack_mover[0] = unpack_mover[0].decode('utf-8')\
                          .replace('\x00','')
        unpack_mover[1] = unpack_mover[1].decode('utf-8')\
                          .replace('\x00','')
        unpack_mover[4] = unpack_mover[4].decode('utf-8')\
                          .replace('\x00','')
        
        for i in range(len(unpack_mover)):
            if (unpack_mover[i]== 'adis'):
                unpack_mover[i]='adios'
                fp_open.seek(s.size*(-1),1)
                
                pack_escribir = []
                pack_escribir.append(unpack_mover[0].encode('utf-8'))
                pack_escribir.append(unpack_mover[1].encode('utf-8'))
                pack_escribir.append(unpack_mover[2])
                pack_escribir.append(unpack_mover[3])
                pack_escribir.append(unpack_mover[4].encode('utf-8'))

                packed_data = s.pack(*pack_escribir)

                fp_open.write(packed_data)

        mover = fp_open.read(s.size)
        
    fp_open.close()

    

rellenabinario()

muestrabinario()
cambiaBinario()

print()
print()
print()
muestrabinario()













