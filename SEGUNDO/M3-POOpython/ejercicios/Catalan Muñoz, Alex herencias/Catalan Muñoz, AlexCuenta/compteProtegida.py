from Compte import Compte
class compteProtegida(Compte):
    def __init__(self,e_numCompte, e_saldo, e_maxDescobert):
        Compte.__init__(self, e_numCompte, e_saldo)
        self.__maxDescobert = e_maxDescobert

    def extreure(self, dinero):
        if(self.__comprobaExtreure(dinero)== False):
            return False
        if(self.getSaldo() >= dinero and dinero <= self.__maxDescobert):
            self._setSaldo(self.getSaldo()-dinero)
            return True
        else:
            return False

    def __comprobaExtreure(self,dinero):
        if((not(isinstance(dinero, int)) and not(isinstance(dinero, float))) or dinero <= 0):
            return False
        else:
            return True