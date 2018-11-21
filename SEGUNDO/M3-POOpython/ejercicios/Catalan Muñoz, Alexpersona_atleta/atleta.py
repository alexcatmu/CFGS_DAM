from data import data

class atleta:
    def __init__(self, e_nombre, e_data=data(), e_llista_temps=[]):
        self.nombre = e_nombre
        self.data = e_data
        self.llista_temps = e_llista_temps

    def top3(self):
        array_top3 = []
        for i in range(1, len(self.llista_temps)):
            for j in range(len(self.llista_temps)-i):
                if self.llista_temps[j+1] < self.llista_temps[j]:
                    aux = self.llista_temps[j]
                    self.llista_temps[j] = self.llista_temps[j+1]
                    self.llista_temps[j+1] = aux

        for i in range(3):
            array_top3.append(self.llista_temps[i])

        return array_top3

    def afegirTemps(self, tiempo=0.0):
        self.llista_temps.append(tiempo)

    def afegirCTemps(self, afegir_llista_temps=[]):
        for i in range (len(afegir_llista_temps)):
            self.llista_temps.append(afegir_llista_temps[i])

    def visualitza(self):
        stringo = "El atleta "+self.nombre+" se dio de alta el dia " + str(self.data.dia)+"-"+str(self.data.mes)+\
              "-"+str(self.data.any)+" y tiene los siguientes tiempos:\n"
        str_tiempos = ""
        for i in range(len(self.llista_temps)):
            str_tiempos += str(self.llista_temps[i])+"\n"

        stringo += str_tiempos

        return stringo





