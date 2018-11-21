import struct
import binascii
'''
a = [1.0,2.2,3.1,4.8,5.0]

s = struct.Struct('f')
ficherito = open('segundo.bin','wb')
i = 0
while (i < len(a)):
    pdata=s.pack(a[i])
    ficherito.write(pdata)
    i += 1

ficherito.close()

'''

fp_leer = open('segundo.bin','rb+')
a = struct.Struct('f')
datosb = fp_leer.read(a.size)


while (datosb != b''):
    datos = a.unpack(datosb)
    print(datos[0])
    datosb = fp_leer.read(a.size)

fp_leer.seek(0,2)
len_fichero = fp_leer.tell()
sent = struct.Struct('f')#tipo de datos como se lee el archivo
fp_leer.seek(0,0)
datos_c = fp_leer.seek(a.size-sent.size,1)

while (fp_leer.tell()<len_fichero):
    print(fp_leer.tell())
    binario = sent.pack(78)
    fp_leer.write(binario)
    print('despues de modificar', fp_leer.tell())
    fp_leer.seek(a.size-sent.size,1)
    






fp_leer.close()
