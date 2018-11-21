import struct
import binascii


s = struct.Struct('10s40s20si')
ficherito = open('alumnes.dat','rb')
#binari = ficherito.read(s.size)
'''
datos = s.unpack(binari)
#print(datos)

datos = list(datos)
datos[0]=datos[0].decode('utf-8')
datos[1]=datos[1].decode('utf-8')
datos[2]=datos[2].decode('utf-8')

print(datos)

datos[0] = datos[0].replace('\x00','')
datos[1] = datos[1].replace('\x00','')
datos[2] = datos[2].replace('\x00','')

print(datos)

ficherito.close()
'''

#datos = s.unpack(binari)

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




'''


fp_leer = open('segundo.bin','rb')
a = struct.Struct('f')
datosb = fp_leer.read(a.size)


while (datosb != b''):
    datos = a.unpack(datosb)
    print(datos[0])
    datosb = fp_leer.read(a.size)

fp_leer.close()
'''
