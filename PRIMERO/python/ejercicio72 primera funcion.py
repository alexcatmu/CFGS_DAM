#programita funciones

'''
1.1) Definiu i programeu una funció que, donats un preu i
un percentatge de descompte, ens torni el preu amb el
descompte aplicat. La funció té dos paràmetres float: preu i
percentatge. Retorna el preu amb el descompte aplicat.
'''
#funciones
def descuento(precio=0, porcentaje=0):
    precio_final = precio - (precio*porcentaje/100)

    return precio_final



#variables
precio = 0
porcentaje = 0


#codigo


precio = float(input("Introduce el precio del articulo: "))

porcentaje = float(input("Introduce el porcentaje de descuento: "))

descuentos = descuento(precio,porcentaje)

print(descuentos)
