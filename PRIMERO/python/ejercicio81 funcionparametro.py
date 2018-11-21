'''
2.3) Programeu un procediment “intercanvi”, que serveixi per a intercanviar
els valors de dos paràmetres sencers passats per referència.
'''



#programa intercambio


#funciones


def intercanvi(x,y):

    temp = x[0]

    x[0] = y[0]

    y[0] = temp


#programa

array_x = [7]

array_y = [10]

print(array_x,array_y)

intercanvi(array_x,array_y)

print(array_x,array_y)
    
















































