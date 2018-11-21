
from persona import persona

from data import data
from atleta import atleta

fecha = data(12, 20, 1967)
print(fecha.visualitza())
persona1 = persona("345354", "vdfvdfv", fecha)
persona2 = persona("345354", "vdfvdfv", fecha)
persona3 = persona("345354", "vdfvdfv", fecha)
print(persona1.getPoblacion())
print(persona1.visualitza())
'''
tiempos = [1.232, 2.342, 2342.23, 234.232, 12.2231, 12.1231]
atleta1 = atleta("Pablo", data(12, 5, 1967))

atleta1.afegirCTemps(tiempos)

print(atleta1.top3())
print(atleta1.visualitza())
'''