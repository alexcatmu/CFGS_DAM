'''
Les classificacions de la lliga de bàsquet de la NBA s'emmagatzemen en
un fitxer on a cada línia hi ha l'informació d'un equip formada pel
nom de l'equip, el nom de la divisió on juga i el nombre de partits
guanyats i perduts, tot separat amb un blanc, dos punts i un blanc.
El nombre de partits guanyats i perduts està separat per un guió. Per
exemple:
Boston Celtics : Atlantic : 11-9
Indiana Pacers : Central : 9-11
Utah Jazz : Northwest : 13-10
Portland Trail Blazers : Northwest : 12-11
Dissenya la funció bonsequips que donat el nom d'un fitxer com
l'indicat i un enter v, retorni una llista amb els noms dels equips
que han guanyat més de v partits ordenats alfabèticament de forma
ascendent. Per exemple, per un fitxer amb les dades anteriors i valor
de v d'11, el resultat seria
['Portland Trail Blazers', 'Utah Jazz']
'''


def bonsequips(fichero, v):
    fp_open = open(fichero,'r')
    EOF = False
    array_linea = []
    array_victorias = []
    resultados = 0
    array_final =[]

    while (EOF == False):
        linea_b = fp_open.readline()
        
        if (linea_b != ''):
            linea_b = linea_b.rstrip('\n')
            array_linea = linea_b.split(' : ')
            #print(array_linea)
            resultados = array_linea[2]
            
            array_victorias = resultados.split('-')
           
            victorias = int(array_victorias[0])
          
           
            if (victorias > v):
                array_final.append(array_linea[0])
            
            

        else:
            EOF = True
    return array_final
    fp_open.close()
    

def ordena_equips(array_equipos):
    continuar = True
    
    for i in range (len(array_equipos)):
        cont = 0
        continuar = True

        if (i+1 < len(array_equipos)):
            while (continuar == True):
                
                      
                if (ord(array_equipos[i][cont]) < ord(array_equipos[i+1][cont])):
                    continuar = False

                elif(ord(array_equipos[i][cont]) == ord(array_equipos[i+1][cont])):
                    cont += 1
                    
                else:
                    auxiliar = array_equipos[i+1]
                    array_equipos[i+1] = array_equipos[i]
                    array_equipos[i] = auxiliar
                    continuar = False
                    
                
    return array_equipos 

            
        






fichero = 'basquet.txt'
v = 11

array_victorias = []

array_victorias = bonsequips(fichero,v)
print(array_victorias)

print(ordena_equips(array_victorias))



























































