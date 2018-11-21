'''
1.6) Farem un programa que treballi amb dos arxius d’entrada:
 Arxiu 1: Trieu qualsevol arxiu de codi Python (*.py)‏
 Arxiu 2: Un arxiu que contingui una llista de números de
 línia en ordre creixent ( el podeu crear manualment vosaltres
                           mateixos). Per exemple:
12
15
17
26

El vostre programa haurà d’obrir els dos arxius i
mostrar per la pantalla les línies de l’arxiu 1 que
s’indiquen a l’arxiu 2. Fixeu-vos en l’exemple:
'''



def leerLineas():
    fp_leer = open('leer.txt','r')
    EOF = False
    array_lineas = []
    while (EOF == False):
        linea = fp_leer.readline().rstrip('\n')
        
        if (linea != ''):
            array_lineas.append(linea)
        else:
            EOF = True
    fp_leer.close()
    return array_lineas


def muestraLineas(lineas):
    fp_muestra = open('prueba.py','r')
    EOF = False
    cont = 0
    i = 0
    while (EOF == False):
        linea = fp_muestra.readline()
        if (linea != ''):
            
            if (cont == int(lineas[i])):
                print(linea,end="")
                i += 1
            cont += 1
            
        else:
            EOF = True

    fp_muestra.close()
    print('El archivo leido tiene '+str(cont)+' lineas')


lineas_array = leerLineas()
print(lineas_array)
muestraLineas(lineas_array)



















