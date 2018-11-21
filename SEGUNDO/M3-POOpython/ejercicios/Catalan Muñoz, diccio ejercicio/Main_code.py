from Diccionario import Diccionario
from FileToString import FileToString

fts = FileToString("romeo.txt")
stringo = fts.ConvertToStringSimple()
#print(stringo)
dic = Diccionario(stringo)
print(dic.cuentaPalabrasRepetidas())

fts.urlFile="romeoPuntuacion.txt"
stringo_complejo = fts.ConvertToStringSimple()
#print(stringo)
dic = Diccionario(stringo_complejo)
print(dic.cuentaPalabrasRepetidas())
