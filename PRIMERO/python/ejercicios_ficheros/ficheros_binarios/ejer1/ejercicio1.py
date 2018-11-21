import struct
import binascii

frase = 'hola'
num = 23

s= struct.Struct(str(len(frase))+'si')
pdata=s.pack(frase.encode('utf-8'),num)

print(binascii.hexlify(pdata))
print('############')

a=struct.Struct('4si')
udata=a.unpack(pdata)

print(udata)
print(udata[0].decode('utf-8,'),udata[1])

print('###################')


fp_open = open('primer_binario.bin','wb')
fp_open.write(pdata)
fp_open.close()


fp_read = open('primer_binario.bin','rb')
udata = fp_read.read(a.size)
datos = a.unpack(udata)

print(datos[0].decode('utf-8'),datos[1])
print('##############')

fp_read.close()
