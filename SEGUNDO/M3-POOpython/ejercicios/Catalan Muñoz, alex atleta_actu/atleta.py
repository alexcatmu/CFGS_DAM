from data import data
from TempsProva import TempsProva
class atleta:
    def __init__(self, e_nombre, e_data=data(), e_llista_temps=[]):
        self.nombre = e_nombre
        self.data = e_data
        self.llista_temps = e_llista_temps


    def top3(self,codigo):
        array_codigo=[]

        for i in range(len(self.llista_temps)):
            if(self.llista_temps[i].codiProva == codigo):
                array_codigo.append(self.llista_temps[i])

        for i in range(1, len(array_codigo)):
            for j in range(len(array_codigo)-i):
                if array_codigo[j+1].tiempo < array_codigo[j].tiempo:
                    aux = array_codigo[j]
                    array_codigo[j] = array_codigo[j+1]
                    array_codigo[j+1] = aux

        array_top3=[]
        for i in range(3):
            array_top3.append(array_codigo[i].tiempo)

        return array_top3

    def afegirTemps(self,fecha_tiempo = data(), tiempo=0.0, codiProva=TempsProva().codiProva):
        self.llista_temps.append(TempsProva(fecha_tiempo,tiempo,codiProva))


    def afegirCTemps(self, afegir_llista_temps):
        for i in range(len(afegir_llista_temps)):
            self.llista_temps.append(afegir_llista_temps[i])

    def visualitza(self):
        stringo = "El atleta "+self.nombre+" se dio de alta el dia " + str(self.data.dia)+"-"+str(self.data.mes)+\
              "-"+str(self.data.any)+" y tiene los siguientes tiempos:\n"
        str_tiempos = ""

        for i in range(1,len(self.llista_temps)):
            for j in range(len(self.llista_temps)-i):
                if self.llista_temps[j+1].codiProva < self.llista_temps[j].codiProva:
                    aux = self.llista_temps[j]
                    self.llista_temps[j] = self.llista_temps[j+1]
                    self.llista_temps[j+1] = aux

        for i in range(1,len(self.llista_temps)):
            if(i == 1):
                str_tiempos += "\n"+str(self.llista_temps[0].codiProva)+"\n"
                str_tiempos += str(self.llista_temps[0].fecha_prueba.visualitza())+"\t"+\
                str(self.llista_temps[0].tiempo)+"\n"

            elif(self.llista_temps[i-1].codiProva != self.llista_temps[i].codiProva):
                str_tiempos += "\n"+str(self.llista_temps[i].codiProva)+"\n"

            str_tiempos += str(self.llista_temps[i].fecha_prueba.visualitza())+"\t"+\
                            str(self.llista_temps[i].tiempo)+"\n"

        stringo += str_tiempos

        return stringo





