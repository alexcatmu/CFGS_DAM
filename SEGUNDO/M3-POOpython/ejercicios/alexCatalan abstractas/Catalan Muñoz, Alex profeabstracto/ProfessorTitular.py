'''
Realitzar la classe ProfessorTitular,
Definir el mètode real importNomina() = 30*43.2
Sobrecàrrega del mètode string de l’objecte, diferenciant que és professor titular
'''
from Professor import Professor
class ProfessorTitular(Professor):
    def __init__(self, nom_c, cognom_c, edat_c, id_c):
        Professor.__init__(self, nom_c, cognom_c, edat_c, id_c)

    def importNomina(self):
        return 30*43.2

    def __str__(self):
        return Professor.__str__(self)+"\n"\
                "Profesor: Titular"

