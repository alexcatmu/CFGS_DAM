'''
2.3) Programeu un procediment “intercanvi”,
que serveixi per a intercanviar els valors de dos
paràmetres sencers passats per referència.
'''

#programa intercanvi



#funcions

def intercanvi(dos_enteros):
    temp= dos_enteros[0]

    dos_enteros[0] = dos_enteros[1]

    dos_enteros[1] = temp




#programa

lista=[2,7]

print(lista)

intercanvi(lista)

print(lista)













































