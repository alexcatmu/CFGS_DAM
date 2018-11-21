class data:
    def __init__(self, c_dia = 0, c_mes = 0, c_any = 0):
        self.dia = c_dia
        self.mes = c_mes
        self.any = c_any

    def setDIA(self, set_dia):
        self.dia = set_dia

    def setMES(self,set_mes):
        self.mes = set_mes

    def setANY(self, set_any):
        self.any = set_any

    def getDIA(self):
        return self.dia

    def getMES(self):
        return self.mes

    def getANY(self):
        return self.any

    def visualitza(self):
        str_data = "("+str(self.getDIA())+","+str(self.getMES())+\
                   ","+str(self.getANY())+")"

        return str_data