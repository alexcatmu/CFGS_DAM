
from data import data
from atleta import atleta
from TempsProva import TempsProva

tiempos = []
tiempos.append(TempsProva(data(10,2,2016),5.3,"100m"))
tiempos.append(TempsProva(data(10,3,2016),4.3,"100m"))
tiempos.append(TempsProva(data(10,4,2016),1.9,"100m"))
tiempos.append(TempsProva(data(10,5,2016),11.3,"200m"))
tiempos.append(TempsProva(data(10,6,2016),12.3,"200m"))
tiempos.append(TempsProva(data(10,6,2016),1.3,"200m"))
tiempos.append(TempsProva(data(10,6,2016),1.6,"100m"))
tiempos.append(TempsProva(data(10,6,2016),1.8,"200m"))

atleta1 = atleta("Pablo",data(10,2,1992))
atleta1.afegirCTemps(tiempos)
print(atleta1.visualitza())
mejores_tiempos = atleta1.top3("200m")
print("Los mejores tiempos en 200m")
for i in range(len(mejores_tiempos)):
    print("Este es el tiempo %i: %s"%(i,mejores_tiempos[i]))