import struct
import binascii


fp_escribe = open('del1al0.bin','wb')

array = [1,2,3,4,5,6,7,8,9]

s = struct.Struct('i')

for i in range (len(array)):
    escribir = s.pack(array[i])
    fp_escribe.write(escribir)
    



fp_escribe.close()
