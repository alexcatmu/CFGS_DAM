import random
import os
'''
4.4) Definiu una estructura de dades anomenada DNI que serveixi per
a desar totes les dades que hi ha dins d’un Document nacional d’identitat
( mireu el vostre DNI per a saber els camps necessaris )‏

Creeu una estructura auxiliar Data que us ajudarà a fer la l’estructura
DNI més senzilla.

Creeu una variable del tipus DNI,  i feu un programa que permeti
llegir del teclat les dades necessàries per a omplir l’estructura
que heu creat

Un cop llegides les dades, el programa esborrarà la pantalla i
mostrarà un resum de tota la informació llegida

Podeu intentar llegir la data format AAAA/MM/DD i fer un split,
per fer una llista de 3 arguments numerics ... (en aquest cas
                                                podeu fer-ho servir)
'''


#programa dni

#variables
class fecha:
    def __init__(self, dia=0, mes=0, ano=0):
        self.dia = dia
        self.mes=mes
        self.ano=ano
    

class DNI:
    def __init__(self, apellido1="", apellido2="",nombre="",\
                 sexo="",nacionalidad="", fecha_nac=fecha(),\
                 idesp="", fecha_cad=fecha()):
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.nombre=nombre
        self.sexo=sexo
        self.nacionalidad=nacionalidad
        self.fecha_nac=fecha_nac
        self.idesp=idesp
        self.fecha_cad=fecha_cad





nombres = ["pepe","jose","pablo"]
apellidos=["Castaño","catalan","gonza","gil","nuñez"]

sexos = ["masculino","femenino"]
nacionalidades=["España","Marruecos","Inglaterra"]
continuar = True
#codigo



print("Se ha generado una persona")

personas=[]

while (continuar==True):
    apellido1=random.choice(apellidos)
    apellido2=random.choice(apellidos)
    nombre= random.choice(nombres)
    sexo=random.choice(sexos)
    nacionalidad= random.choice(nacionalidades)
    diaN= random.randint(1,21)
    mesN= random.randint(1,12)
    anoN= random.randint(1933,2015)

    idesp= random.randint(1,234231424)
    diaC= random.randint(1,21)
    mesC= random.randint(1,12)
    anoC= random.randint(1933,2015)
   
    persona = DNI(apellido1,apellido2,nombre,sexo,nacionalidad,\
                  fecha(diaN,mesN,anoN),idesp,fecha(diaC,mesC,anoC))


    personas.append(persona)



    continuar = input("Quieres generar nueva persona(s)")
    if (continuar != 's'):
        continuar = False
    else:
        continuar =True

print("\n\n")

os.system('cls')
for i in range(len(personas)):
    print("Apellidos y nombre:",personas[i].apellido1,\
          personas[i].apellido2,",",personas[i].nombre,\
          "\nSexo:",personas[i].sexo, "\nNacionalidad:",\
          personas[i].nacionalidad, \
          "\nFecha de nacimiento:",personas[i].fecha_nac.dia,\
          personas[i].fecha_nac.mes,personas[i].fecha_nac.ano,\
          "\nIdesp:",personas[i].idesp,"\nFecha de caducidad:", \
          personas[i].fecha_cad.dia,personas[i].fecha_cad.mes,\
          personas[i].fecha_cad.ano,"\n\n")











        








