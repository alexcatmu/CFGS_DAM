'''
.- Un programa té les següents entrades:
 un any determinat ( p.ex.2006 )‏
 el dia de la setmana en que va començar
 ( en format numèric, 1 pel dilluns, 2 per dimarts, etc. ) 
La sortida del programa serà un calendari per pantalla
que mostrarà una capçalera per a cada mes, i separarà
els dies per setmanes. Vegeu-ne un exemple a continuació
per l’any 2006, que ha començat en dilluns.
'''

#programa calendario

#variables


#codigo


print ("Introduce un año")
ano = int(input())
print ("Introduce en que dia empieza(Formato numérico)")
dia = int (input())

if ((ano %4 == 0 and ano %100 != 0) or (ano % 400 == 0)):
    dias = 365
else:
    dias = 366

mes = 1
while (mes <= 12):

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        dias = 31
        cont = 1
        print (mes)
        while (cont <= dias):
            
            if (dia == 1):
                print ("Dia", cont,"Lunes")
            if (dia == 2):
                print ("Dia", cont,"Martes")
            if (dia == 3):
                print ("Dia", cont,"Miercoles")
            if (dia == 4):
                print ("Dia", cont,"Jueves")
            if (dia == 5):
                print ("Dia", cont,"Viernes")
            if (dia == 6):
                print ("Dia", cont,"Sabado")
            if (dia == 7):
                print ("Dia", cont,"Domingo")
                dia = 0
            dia = dia + 1
            cont = cont + 1
    mes = mes + 1
    if (mes == 2):
        if ((ano %4 == 0 and ano %100 != 0) or (ano % 400 == 0)):
            dias = 29
        else:
            dias = 28

        cont = 1
        print (mes)
        while (cont <= dias):
            
            if (dia == 1):
                print ("Dia", cont,"Lunes")
            if (dia == 2):
                print ("Dia", cont,"Martes")
            if (dia == 3):
                print ("Dia", cont,"Miercoles")
            if (dia == 4):
                print ("Dia", cont,"Jueves")
            if (dia == 5):
                print ("Dia", cont,"Viernes")
            if (dia == 6):
                print ("Dia", cont,"Sabado")
            if (dia == 7):
                print ("Dia", cont,"Domingo")
                dia = 0
            dia = dia + 1
            cont = cont + 1
            
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        dias = 30
        cont = 1
         
        print (mes)
        while (cont <= dias):
            
            if (dia == 1):
                print ("Dia", cont,"Lunes")
            if (dia == 2):
                print ("Dia", cont,"Martes")
            if (dia == 3):
                print ("Dia", cont,"Miercoles")
            if (dia == 4):
                print ("Dia", cont,"Jueves")
            if (dia == 5):
                print ("Dia", cont,"Viernes")
            if (dia == 6):
                print ("Dia", cont,"Sabado")
            if (dia == 7):
                print ("Dia", cont,"Domingo")
                dia = 0
            dia = dia + 1
            cont = cont + 1

input()


























    

