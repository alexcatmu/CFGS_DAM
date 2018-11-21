'''
2.13) Treball amb estructures com a paràmetres de funcions
a) Definiu una estructura Data ( dia/mes/any)‏
b) Creeu un procediment per a mostrar una data per pantalla. 
	void mostraData( Data d, int format )‏
El paràmetre “format” tindrà el següent efecte:
c) Creeu un procediment que permeti omplir per teclat una variable
de tipus data passada com a paràmetre:	 void omplirData( Data d)‏
d) Definiu una funció que, donades dues variables Data, ens torni
la diferència entre elles en dies.
e) Feu un programa que llegeixi una data de naixement del teclat.
Després llegirà per teclat la data actual. Posteriorment, el programa
ens dirà respecte a la data actual, quants dies queden per l’aniversari
de la persona en qüestió. Useu les funcions que heu anat creant fins ara.
'''

class Data:

    def __init__(self, dia=0, mes = 0, ano = 0):

        self.dia = dia
        self.mes = mes
        self.ano = ano


def omplirData(fecha):

    fecha.dia = int(input())
    fecha.mes = int(input())
    fecha.ano = int(input())


def mostraData(fecha):

    print("fecha(dd-mm-año):",fecha.dia, end='-')
    print(fecha.mes, end='-')
    print(fecha.ano)



def diferenciaData(fechaI, fechaF):

    diaI = fechaI.dia
    diaF = fechaF.dia
    

    dias_de_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    mesI = fechaI.mes
    mesF = fechaF.mes


    total_dias = 0
    dias = 0
    if (diaI < dias_de_mes[mesI-1] and (mesI != mesF)):

        dias = diaI - dias_de_mes[mesI-1]

    if (diaF < dias_de_mes[mesI-1] and (mesI != mesF)):

        dias += diaF

    if (mesI == mesF):

        if (diaI < diaF):
            dias = diaF - diaI

        elif (diaI > diaF):
            dias = dias + dias_de_mes[mesI -1] + (diaF-diaI)
            mesI += 1

    if (mesI > mesF):

        dias += dias_de_mes[mesI-1]

    if ((fechaF.ano % 100 != 0 and fechaF.ano %4 == 0) or\
        (fechaF.ano % 400 == 0)):

        dias_de_mes[1] = 29

        
    while (mesI != mesF):

        total_dias= total_dias + dias_de_mes[mesI-1]

        #print(total_dias)
        if (mesI == 12):
            mesI = 0
        
        mesI += 1

    

    total_dias = total_dias + dias

    return total_dias
    
#programa

fechaN = Data()
omplirData(fechaN)

mostraData(fechaN)

fechaHoy = Data()

omplirData(fechaHoy)

mostraData(fechaHoy)

print(diferenciaData(fechaN, fechaHoy))






















