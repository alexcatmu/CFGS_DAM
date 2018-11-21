from Persona import Persona
from ProfessorTitular import ProfessorTitular
from ProfessorInteri import ProfessorInteri
from LlistaProfessors import LlistaProfessors

prof = Persona("pepe", "antonio", 34)
print(prof)

print("")

profesorito = ProfessorTitular("manolo", "gonzalez", 34, 1000)#1296.0
print(profesorito)
print(profesorito.getIdProfessor())
print(profesorito.importNomina())

print("")

pro = ProfessorInteri("yee", "yuuu", 34, 123131)#1068.0
print(pro.importNomina())
print(pro)

pro2 = ProfessorInteri("ftgbf", "qweqq", 22, 111)#1068.0
pro3 = ProfessorTitular("perito", "paquete", 34, 1010)#1296.0
pro4 = ProfessorInteri("rtrtr", "yutytyu", 34, 343)#1068.0

arr_profes = [pro, profesorito, pro2, pro3, pro4]

list_prof = LlistaProfessors(arr_profes)
list_prof.inserirProfessor(profesorito)#1296.0
print(list_prof.llistarProfessorat())
