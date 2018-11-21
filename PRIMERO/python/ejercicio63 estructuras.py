#programa clases

#variables




class data:
    def __init__(self, dia=0, mes=0, ano=0):
        self.dia=dia
        self.mes=mes
        self.ano=ano


class fitxa:
    def __init__(self, idLlibre=0, titol="", autors="",editorial="",\
                 edicio=0, ano_edicio=0, num_pag=0, data_pub=data()\
                 ,data_imp=data()):
        
        self.idLlibre=idLlibre
        self.titol=titol
        self.autors=autors
        self.editorial=editorial
        self.edicio=edicio
        self.ano_edicio=ano_edicio
        self.num_pag=num_pag
        self.data_pub=data_pub
        self.data_imp=data_imp

#codigo
'''

ficha = fitxa()

ficha.idLlibre=int(input("Introduce el id del libro: "))

ficha.titol = input("Introduce el titulo del libro: ")

ficha.autors = input("Introduce el nombre de los autores: ")

ficha.editorial=input("Introduce la editorial: ")

ficha.edicio=int(input("Introduce el numero de edicion: "))

ficha.ano_edicio = int(input("Introduce el año de edicion: "))

ficha.num_pag = int(input("Introduce el numero de paginas: "))

ficha.data_pub.dia= int(input("Introduce el dia de publicacion: "))

ficha.data_pub.mes = int(input("Introduce el mes de publicacion: "))

ficha.data_pub.ano = int(input("Introduce el año de publicacion: "))

ficha.data_imp.dia= int(input("Introduce el dia de impresion: "))

ficha.data_imp.mes = int(input("Introduce el mes de impresion: "))

ficha.data_imp.ano = int(input("Introduce el año de impresion: "))



print("ID del libro: ",ficha.idLlibre)
print("Titulo: ",ficha.titol)
print("Autores: ", ficha.autors)
print("Editorial: ",ficha.editorial)
print("Numero de edición: ", ficha.edicio)
print("Año de edicion: ",ficha.ano_edicio)
print("Numero de paginas: ",ficha.num_pag)
print("Esta es la fecha de publicacion: ",ficha.data_pub.dia,"-",\
      ficha.data_pub.mes,"-", ficha.data_pub.ano)
print("Esta es la fecha de impresión: ", ficha.data_imp.dia,"-", \
      ficha.data_imp.mes, "-", ficha.data_imp.ano)
'''

ficha = fitxa(123,"el nombre ","jaime","vox",3,1967,\
              1231,data(1,2,2013),data(2,4,2015))

print("ID del libro: ",ficha.idLlibre)
print("Titulo: ",ficha.titol)
print("Autores: ", ficha.autors)
print("Editorial: ",ficha.editorial)
print("Numero de edición: ", ficha.edicio)
print("Año de edicion: ",ficha.ano_edicio)
print("Numero de paginas: ",ficha.num_pag)
print("Esta es la fecha de publicacion: ",ficha.data_pub.dia,"-",\
      ficha.data_pub.mes,"-", ficha.data_pub.ano)
print("Esta es la fecha de impresión: ", ficha.data_imp.dia,"-", \
      ficha.data_imp.mes, "-", ficha.data_imp.ano)













    
