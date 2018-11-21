import binascii
import struct
'''
1.2) Usant els arxius generats al problema anterior, feu un programa
que fusioni “parells.txt” i “senars.txt” en un tercer arxiu “1a100.txt”,
intercalant una línia de senars, i una dels parells.
'''

def parells():

    fp_open=open('parellsBIN.bin','wb')
    array=['uno','dos','tres','cuatro','cinco','seis','siete','ocho',\
           'nueve','diez']

    s= struct.Struct('10si')
    
    for i in range(100):
        numAux = i
        
        if (numAux >= 10):
            numAux = i%10

        strin_num = array[numAux]
        datos = [strin_num.encode('utf-8'),i]
        packed_data = s.pack(*datos)
        
        fp_open.write(packed_data)

    fp_open.close()

    
def muestraParells():
    fp_open=open('parellsBIN.bin','rb')

    s=struct.Struct('10si')

    dato = fp_open.read(s.size)

    while (dato != b''):
        
        #print(dato)
        unpacked_data = s.unpack(dato)
        #print(unpacked_data)
        dato_real = [unpacked_data[0].decode('utf-8'),unpacked_data[1]]
        #print(dato_real)

        dato_real[0] =dato_real[0].replace('\x00','')
        print(dato_real)
        

        dato = fp_open.read(s.size)
        

def cambiaUno():
    fp_open= open('parellsBIN.bin','rb+')

    s = struct.Struct('10si')

    cambiador = struct.Struct('10s')
    
    fp_open.seek(0,2)
    tam = fp_open.tell()
    fp_open.seek(0,0)
    #print(fp_open.tell(),'',tam)
    while (fp_open.tell()<tam):#(dato != b''):
        #print(fp_open.tell(),'',tam)
        introduce = ['aaaaa'.encode('utf-8')]
        
        packed_introduce = cambiador.pack(*introduce)

        fp_open.write(packed_introduce)
        fp_open.seek(6,1)
       #dato=fp_open.read(s.size)
    

parells()

muestraParells()

cambiaUno()

muestraParells()





































