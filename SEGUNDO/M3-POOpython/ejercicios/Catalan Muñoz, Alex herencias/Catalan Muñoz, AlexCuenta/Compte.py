from datetime import datetime
from Excepciones import saldoReal
from Excepciones import ingresoError
class Compte():
    def __init__(self, e_numCompte, e_saldo):

        self.__errorSaldo(e_saldo)

        self.__saldo = float(e_saldo)

        self.__numCompte = str(e_numCompte)
        self.__data = str(datetime.today())

    def __str__(self):
        return "N cuenta: "+str(self.__numCompte) +"\nSaldo: "+str(self.__saldo)+"\nFecha acceso: "+str(self.__data)

    def ingresar(self, ingreso):
        if((not(isinstance(ingreso,int)) and not(isinstance(ingreso,float))) or ingreso <= 0):
            raise ingresoError(ingreso)
        else:
            self.__saldo += ingreso

    def extreure(self, dinero):
        self.__errorSaldo(self, dinero)
        if(self.__saldo >= dinero and dinero >= 0):
            self.__saldo -= dinero
            return True
        else:
            return False

    def __setSaldo(self, saldo):
        self.__saldo = saldo

    def _setSaldo(self,saldo):
        self.__errorSaldo(saldo)
        self.__setSaldo(saldo)

    def getSaldo(self):
        return self.__saldo

    def getData(self):
        return self.__data

    def setData(self):
        self.__data = str(datetime.today())

    def getData(self):
        return self.__data

    def setnumCompte(self,n_compte):
        self.__numCompte = str(n_compte)

    def getnumCompte(self):
        return self.__numCompte

    def __errorSaldo(self, saldo):
        if(not(isinstance(saldo, float)) and not(isinstance(saldo,int))):
            raise saldoReal(saldo)
        else:
            pass

