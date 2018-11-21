class LlistaProfessors():
    def __init__(self, array_profe_e):
        self.arr_prof = array_profe_e

    def inserirProfessor(self, profe):
        self.arr_prof.append(profe)

    def llistarProfessorat(self):
        total_nominas = 0
        for i in range(len(self.arr_prof)):
            total_nominas += self.arr_prof[i].importNomina()
        return total_nominas