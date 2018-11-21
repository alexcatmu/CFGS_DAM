class Diccionario():
    def __init__(self, frase):
        self.__frase = frase
        self.__listaFrase = []
        self.__DiccionarioRepetidas = {}

    def cuentaPalabrasRepetidas(self):
        self.__listaFrase = self.__frase.split(" ")
        array_limpio = self.__ListaLimpia()
        self.__ListaRepetidas(array_limpio)
        return self.__DiccionarioRepetidas

    def __ListaRepetidas(self, array_letras):
        for i in range(len(array_letras)):
            cont = 0
            for j in range (len(self.__listaFrase)):
                if(self.__listaFrase[j] == array_letras[i]):
                    cont += 1

            self.__DiccionarioRepetidas[array_letras[i]] = cont



    def __ListaLimpia(self):
        lista_limpia = []
        for i in self.__listaFrase:
            if i not in lista_limpia:
                lista_limpia.append(i)
        return lista_limpia