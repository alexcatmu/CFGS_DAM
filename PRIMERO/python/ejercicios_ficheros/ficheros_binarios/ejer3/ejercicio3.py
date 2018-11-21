import struct
import binascii


s = struct.Struct('10s40s20si')
ficherito = open('alumnes.dat','rb')
binari = ficherito.read(s.size)

while (binari != b''):
    
    datos = s.unpack(binari)
    datos = list(datos)
        
    for i in range (3):
        datos[i] = datos[i].decode('utf-8')

        datos[i] = datos[i].replace('\x00','')

    print(datos)
    
    binari = ficherito.read(s.size)



ficherito.close()


fp_leer = open('alumnes.dat','rb+')

fp_leer.seek(0,2)
len_fichero = fp_leer.tell()
sent = struct.Struct('i')#tipo de datos como se lee el archivo
fp_leer.seek(0,0)
datos_c = fp_leer.seek(s.size-sent.size,1)

while (fp_leer.tell()<len_fichero):
    print(fp_leer.tell())
    binario = sent.pack(-4)
    fp_leer.write(binario)
    print('despues de modificar', fp_leer.tell())
    fp_leer.seek(s.size-sent.size,1)
    
fp_leer.close()





