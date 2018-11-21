from carta import carta
from baralla import Baralla
from excepciones import GanaOpierdeExcept

class setYmig:
    def __init__(self):
        self.baralla7mig = Baralla(1,True)
        self.__cartaActual = None
        self.__puntos_totales_banca = 0

    def valorCarta(self):
        self.__cartaActual = self.baralla7mig.carta_robar()
        return self.__cartaActual.valor7iMig()

    def Cartastring(self):
        return self.__cartaActual

    def CartasDeBanca(self):
        continuar = True
        print("\n\n")
        array_cartas = []
        stringo = ""
        stringo = "La banca\n"
        while continuar:
            valor = self.valorCarta()

            self.__puntos_totales_banca += valor

            stringo += str(self.Cartastring())+"\n"
            if(self.__puntos_totales_banca >= 5.5):
                continuar = False
                stringo += "Puntos totales "+str(self.__puntos_totales_banca)

        return stringo

    #jugadores -> todos los jugadores de la partida!
    #valores -> los valores de cada jugador!
    def GanaOpierde(self,valores):
        if(not (isinstance(valores,list))):
            raise GanaOpierdeExcept(valores)
        array_ganadores = []
        array_perdedores = []
        stringo = ""


        for i in range(len(valores)):
            if(valores[i]> 7.5):
                array_perdedores.append(i+1)
            elif(valores[i] > self.__puntos_totales_banca or self.__puntos_totales_banca > 7.5):
                array_ganadores.append(i+1)
            elif(valores[i] <= self.__puntos_totales_banca):
                array_perdedores.append(i+1)

        if(len(array_ganadores) > 0):
            stringo += "\n\x1b[4;34;47m"+"Los siquientes jugadores han ganado a la banca:\n"
            for i in range(len(array_ganadores)):
                stringo += "Jugador "+str(array_ganadores[i])+"\n"
            stringo += "\x1b[0m"
        if(len(array_perdedores) > 0):
            stringo += "\n\x1b[4;31;47m"+"Los siguientes jugadores han perdido:\n"
            for i in range(len(array_perdedores)):
                stringo += "Jugador "+str(array_perdedores[i])+"\n"
            stringo += "\x1b[0m"

        return stringo

