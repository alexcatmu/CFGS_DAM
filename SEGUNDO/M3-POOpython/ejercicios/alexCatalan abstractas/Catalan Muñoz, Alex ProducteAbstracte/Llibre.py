'''
Llibre hereta Producte, ídem al cas Electrònica. No tenim subllibres.
Atributs: string editor, integer anyPublicacio
setEditor(string)
String getEditor()
setAnyPublicacio(integer)
Integer getAnyPublicacio()
Double calculaPreuOferta(), preuRegular*0.5
Sobrecarrega str
'''
from Producte import Producte
class Llibre(Producte):
    def __init__(self, Preu_c, editor_c, anyPublicacio):
        Producte.__init__(self, Preu_c)
        self.__editor = editor_c
        self.__anyPublicacio = anyPublicacio

    def setEditor(self, edi):
        self.__editor = edi

    def getEditor(self):
        return self.__editor

    def setAnyPublicacio(self, anyPu):
        self.__anyPublicacio = anyPu

    def getAnyPublicacio(self):
        return self.__anyPublicacio

    def calculaPreuOferta(self):
        return Producte.getPreuRegular(self) * 0.5

    def __str__(self):
        return "Aquest producte es una llibre\n" + \
            "Preu normal: "+str(Producte.getPreuRegular(self)) + \
            "Preu oferta: "+str(self.calculaPreuOferta())




