import struct

from Byte import Byte
from operator import attrgetter
import codecs
from Nodo import Nodo
import sys
class Huffman():

    def __init__(self, fichero, fichero_destino, fichero_claves, modo):
        if(isinstance(fichero,str) == False or (modo != "C" and modo != "D")):
            raise NotImplementedError

        self.__fichero = fichero
        self.fichero_destino = fichero_destino
        self.fichero_claves = fichero_claves
        self.__modo = modo
        self.__totalFichero = 0
        self.listaEstadistica = []
        self.arbol_recorrido = None
        self.arbol_auxiliar = None

        if(self.__modo == "C"):
            self.fichero_claves
            self.estadisticaLectura()
        if(self.__modo == "D"):
            self.descomprime()

    def estadisticaLectura(self):
        fp_readStadistica = open(self.__fichero,"rb")
        fp_readStadistica.seek(0,2)
        tamanoFile = fp_readStadistica.tell()
        self.__totalFichero = tamanoFile
        fp_readStadistica.seek(0,0)

        array_Bytes = []
        while (fp_readStadistica.tell() < tamanoFile):
            byteFile = fp_readStadistica.read(1)  # leo un solo byte
            dato = Byte(ord(byteFile))
            existe = False
            for i in range(len(array_Bytes)):
                if(array_Bytes[i].byte == dato.byte):
                    array_Bytes[i].cantidad += 1
                    existe = True

            if(not existe):
                dato.cantidad = 1
                array_Bytes.append(dato)

        total = 0
        for i in range(len(array_Bytes)):
            array_Bytes[i].porcentaje = array_Bytes[i].cantidad / tamanoFile
            total += array_Bytes[i].porcentaje
            array_Bytes[i].totalBytes = tamanoFile

        self.listaEstadistica = array_Bytes
        self.__ordenarMin()
        self.__generarArbolHuff()
        self.escribirClaves()

    def __ordenarMin(self):
        self.listaEstadistica = sorted(self.listaEstadistica,key = attrgetter('cantidad'), reverse= False)

    def __generarArbolHuff(self):
        self.__insertar()

    def __insertar(self):
        if(len(self.listaEstadistica) > 1):
            nodoNuevo = Nodo(self.listaEstadistica[0].cantidad + self.listaEstadistica[1].cantidad)
            nodoNuevo.nodoIzquierda = self.listaEstadistica[0]
            nodoNuevo.nodoDerecha = self.listaEstadistica[1]

            self.listaEstadistica.pop(0)
            self.listaEstadistica[0] = nodoNuevo
            self.__ordenarMin()
            self.__insertar()

    def escribirClaves(self):
        keyFile = open(self.fichero_claves, 'w')
        keyFile.write(str(self.__totalFichero))
        keyFile.close()
        # print(self.__totalFichero)
        self.__recorreArbol()
        keyFile.close()

    def __recorreArbol(self):
        nodoAux = self.listaEstadistica[0]
        keyFile = open(self.fichero_claves, 'a')
        self.__inorder(nodoAux, "", keyFile)
        keyFile.close()
        keyFile = open(self.fichero_claves, 'r')
        self.__generarComprimido(keyFile)
        keyFile.close()

    def __inorder(self, nodoAux, recorrido, keyFile):
        if type(nodoAux) == Nodo:
            self.__inorder(nodoAux.nodoIzquierda, recorrido+"0", keyFile)
            self.__inorder(nodoAux.nodoDerecha, recorrido+"1", keyFile)
        else:
            keyFile.write("\n"+str(nodoAux.cantidad)+"\t"+str(nodoAux.byte)+"\t"+str(recorrido))

    def __tamanoFile(self, File):
        File.seek(0,2)
        tamanoFile = File.tell()
        File.seek(0,0)
        return tamanoFile

    def __diccionarioKeyFile(self, File, tamanoFile):
        File.readline()
        diccioKeyFile = {}
        while (File.tell() < tamanoFile):
            linea = File.readline().replace("\n", "")
            linea_datos_keys = linea.split("\t")
            #linea_datos_keys[1] === valor del ascii
            #linea_datos_keys[2] === camino del ascii
            diccioKeyFile[linea_datos_keys[1]] = linea_datos_keys[2]
        return diccioKeyFile


    def __generarComprimido(self, keyFile):
        fp_readOriginal = open(self.__fichero,"rb")
        fp_writeCompres = open(self.fichero_destino, "wb")

        tamanoFile = self.__tamanoFile(keyFile)
        keyFile.close()
        self.leerFicheroClaves(keyFile.name)
        keyFile = open(keyFile.name, "r")
        self.diccionario_recorrido = {}
        self.generar_diccionario_recorrido_a_partir_del_arbol(self.listaEstadistica[0], "", "")
        diccioKeyFile = self.diccionario_recorrido
        tamanoFile = self.__tamanoFile(fp_readOriginal)
        cadena = ""
        while (fp_readOriginal.tell() < tamanoFile):
            byteFile = fp_readOriginal.read(1)  # leo un solo byte
            dato = ord(byteFile)

            for valorOrd,direccionDato in diccioKeyFile.items():
                if(int(dato) == int(valorOrd)):
                    cadena += direccionDato
                    while(len(cadena) >= 8):
                        aux = cadena[:8]
                        cadena = cadena[8:]
                        valorEnt = int(aux, 2)
                        s = struct.Struct("B")
                        dataBytes= s.pack(valorEnt)
                        fp_writeCompres.write(dataBytes)
                        #fp_writeCompres.write(bytes(int(aux,2).to_bytes(1,"little")))

        if(cadena != ""):
            cadena += (8 - len(cadena)) * '0'
            valorEnt = int(cadena, 2)
            s = struct.Struct("B")
            dataBytes= s.pack(valorEnt)
            fp_writeCompres.write(dataBytes)
            #fp_writeCompres.write(bytes(int(cadena,2).to_bytes(1,"little")))

    def descomprime(self):
        self.leerFicheroClaves(self.fichero_claves)

        self.__generarFicheroDescomprimido()

    def leerFicheroClaves(self, File):
        File = open(File,"r")
        File.seek(0,2)
        tamanoFile = File.tell()
        File.seek(0,0)

        File.readline()
        self.listaEstadistica = []
        while (File.tell() < tamanoFile):
            linea = File.readline().replace("\n", "")
            linea_datos_keys = linea.split("\t")
            bite = Byte(int(linea_datos_keys[1]))
            bite.cantidad = int(linea_datos_keys[0])
            #linea_datos_keys[1] === valor del ascii
            #linea_datos_keys[2] === camino del ascii
            self.listaEstadistica.append(bite)

        self.__ordenarMin()
        self.__generarArbolHuff()

    def __generarFicheroDescomprimido(self):
        fp_readOriginal = open(self.__fichero,"rb")
        fp_writeCompres = open(self.fichero_destino, "wb")
        tamanoFile = self.__tamanoFile(fp_readOriginal)
        cadena = ""
        self.arbol_recorrido = self.listaEstadistica[0]
        self.arbol_auxiliar = self.listaEstadistica[0]
        tamanoFile = self.arbol_auxiliar.cantidad
        contador = 0
        while (contador < tamanoFile):
            byteFile = fp_readOriginal.read(1)  # leo un solo byte
            recorrido_binario = (bin(ord(byteFile))[2:].zfill(8))
            while (len(recorrido_binario) > 0):
                if(isinstance(self.arbol_auxiliar, Byte)):
                    valorEnt = int(self.arbol_auxiliar.byte)
                    # print(valorEnt)
                    s = struct.Struct("B")
                    dataBytes= s.pack(valorEnt)
                    if(contador < tamanoFile):
                        fp_writeCompres.write(dataBytes)
                    contador += 1
                    # print(str(contador)+"contador")
                    # print(str(tamanoFile)+"tamanofile")
                    self.arbol_auxiliar = self.listaEstadistica[0]
                else:
                    if(recorrido_binario[0] == "0"):
                        self.arbol_auxiliar = self.arbol_auxiliar.nodoIzquierda
                    if(recorrido_binario[0] == "1"):
                        self.arbol_auxiliar = self.arbol_auxiliar.nodoDerecha
                    recorrido_binario = recorrido_binario[1:]
        fp_readOriginal.close()
        fp_writeCompres.close()

    def generar_diccionario_recorrido_a_partir_del_arbol(self, nodo, contador, stringo = ""):
        if (isinstance(nodo, Nodo)):
            stringo += self.generar_diccionario_recorrido_a_partir_del_arbol(nodo.nodoIzquierda, contador + "0")
            stringo += self.generar_diccionario_recorrido_a_partir_del_arbol(nodo.nodoDerecha, contador + "1")
        elif (isinstance(nodo, Byte)):
            self.diccionario_recorrido[str(nodo.byte)] = contador
        return stringo
