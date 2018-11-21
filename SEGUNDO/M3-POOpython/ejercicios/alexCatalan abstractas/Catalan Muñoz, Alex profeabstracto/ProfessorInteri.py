from Professor import Professor
from datetime import datetime

class ProfessorInteri(Professor):
    def __init__(self, nom_c, cognom_c, edat_c, id_c):
        Professor.__init__(self, nom_c, cognom_c, edat_c, id_c)

        now = datetime.today() # timezone-aware datetime.utcnow()
        self.dia = now.day
        self.mes = now.month
        self.ano = now.year
        self.fecha_ini_str = str(self.dia)+"/"+str(self.mes)+"/"+str(self.ano)

    def importNomina(self):
        return 30*35.6

    def __str__(self):
        return Professor.__str__(self)+"\n"\
                "Profesor: Interi\n"\
                "Data incorporació: "+str(self.fecha_ini_str)
