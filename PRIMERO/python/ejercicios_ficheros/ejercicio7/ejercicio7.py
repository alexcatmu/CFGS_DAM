'''
Farem un programa que treballi amb dos arxius d’entrada:
 Arxiu_1: Trieu qualsevol arxiu de codi Python (*.py)‏
 Arxiu_2: Un arxiu que sigui una llista de números de línia en
 qualsevol ordre. Per exemple:



a) El vostre programa haurà de mostrar per la pantalla les línies
de programa del arxiu_1 que estan indicades a l’arxiu_2.
'''



def leerLineas():
    fp_leer = open('leer.txt','r')
    EOF = False
    while (EOF == False):
        linea = fp_leer.readline().rstrip('\n')
        
        if (linea != ''):
            muestraLineas(linea)
        else:
            EOF = True
    fp_leer.close()


def muestraLineas(lineas):
    fp_muestra = open('prueba.py','r')
    fp_com_line = open('comienza_linea.txt','a')
    EOF = False
    cont = 0
    while (EOF == False):
        linea = fp_muestra.readline()
        if (linea != ''):
            if (cont == int(lineas)):
                print(linea,end="")
                posicion = fp_muestra.seek(fp_muestra.tell())
                fp_com_line.write(str(posicion)+'\n')
                #fp_muestra.seek me da la posicion donde se encuentra el
                #fichero
                ##fp_muestra.tell me da el valor NUMERICO de la posicion
                ##en bytes  
                print(str(posicion))
                EOF = True
            cont += 1
            
        else:
            EOF = True
            print('#########################\nFuera de rango\nLineas'+\
                  ' totales del archivo:'+str(cont)\
                  +'\nLinea del archivo a leer:'+lineas+\
                  '\n#########################')

    fp_muestra.close()


leerLineas()
#print(lineas_array)
#muestraLineas(5)


