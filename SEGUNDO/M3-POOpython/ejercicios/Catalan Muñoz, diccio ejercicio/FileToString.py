import string
class FileToString():
    def __init__(self, urlFile):
        self.urlFile = urlFile

    def ConvertToStringSimple(self):
        archivo = open(self.urlFile, "r")
        txt_archivo = archivo.readlines()
        stringo = ""
        for line in txt_archivo:
            stringo += line
        stringo = self.SanitizeString(stringo)
        return stringo

    def SanitizeString(self, stringo):

        stringo = stringo.replace("\n","")
        for i in string.punctuation:
            stringo = stringo.replace(i,"")
        return stringo
