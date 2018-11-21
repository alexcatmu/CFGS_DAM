import math
'''
2.11) Treball amb arrays com a paràmetres de funcions
 Un punt a l’espai tridimensional es pot representar com un
 array de double’s de 3 posicions, on cada posició conté la coordenada
 x,y i z respectivament.
L’objectiu de l’exercici és construir una sèrie de funcions que ens
permetin treballar amb punts a un espai tridimensional.

a) Fer una funció que retorni la distància entre dos punts a l’espai. 
	Punt inicial (x1, y1, z1), Punt final (x2, y2, z2)‏
	Distància =   (x1-x2)2 + ( y1-y2 )2 +( z1-z2 )2 
	
	double distancia( int inici[3], int fi[3] )‏

	
b) Fer un procediment que retorni el punt intermedi entre dos punts passats com a paràmetre. En aquest cas, com hem de retornar un array, ho farem a través d’un tercer paràmetre.
	Punt inicial (x1, y1, z1), Punt final (x2, y2, z2)‏
	Punt Intermedi   (xm, ym, zm) =  ( x1+x2,  y1+y2,  z1+z2 )‏

	void  puntMig( int inici[3], int fi[3], int mig[3] )‏
import math 	math.sqrt(x)

'''


#programa de distancias



#funciones
def distancia(inicio, fin):

    distancia = 0
    
    x = inicio[0] - fin[0]
    x = x*x
    y = inicio[1] - fin[1]
    y = y*y
    z = inicio[2] - fin[2]
    z = z*z
    distancia = math.sqrt(x + y + z) 
    return distancia

def PuntMig (inicio,fin,PuntIntermedi):

    for i in range(3):
        
        PuntIntermedi[i] = (inicio[i] + fin[i])/2
        
    

    
#programa


inicio = [0,0,0]

final = [3,3,3]

intermedio = [0,0,0]

print(distancia(inicio,final))

PuntMig(inicio,final,intermedio)
print(intermedio)

























