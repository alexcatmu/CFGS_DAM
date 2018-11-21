from amfibi import amfibi
from excepciones import boolVeneno
class granota(amfibi):
    def __init__(self,color = "", sexe = 0, c_venenosa = False):
        if(not(isinstance(c_venenosa,bool))):
            raise boolVeneno
        self.__venenosa = c_venenosa
        if (self.__venenosa):
            self.__strVenenosa = "venenosa"
        else:
            self.__strVenenosa = "no es venenosa"
        #super().__init__(color, sexe)
        #super(granota,self).__init__(color, sexe)
        amfibi.__init__(self,color, sexe)
    def __str__(self):
        return amfibi.__str__(self) + " " + str(self.__strVenenosa)





