#programa atleta

#estructuras
class atleta:
    def __init__(self, nombre='', fecha='',lista=[]):
        self.nombre = nombre
        self.fecha = fecha
        self.lista= lista

class fecha:
    def __init__(self, dia=0,mes=0,ano=0):
        self.dia=dia
        self.mes=mes
        self.ano=ano

#variables

atletas = atleta()
seguir = True

#codigo


atletas = atleta()
fechas = fecha()
seguir = True
while (seguir == True):
    nombre = input("Introduce el nombre del atleta: ")
    dia = input("Introduce el dia de nacimiento: ")
    mes = input("Introduce el mes de nacimiento: ")
    ano = input("Introduce año de nacimiento: ")

    lista=[]
    for i in range(3):
        tiempos = input("Introduce el tiempo del atleta: ")
        lista.append(tiempos)

    seguir = input("Desea introducir otro atleta? ")
    if (seguir == 'si'):
        seguir = False

    atletas = atleta(nombre,fecha(dia,mes,ano),lista)

    print(atletas.nombre, atletas.fecha.dia,atletas.fecha.mes,\
          atletas.fecha.ano, atletas.lista)
        





































