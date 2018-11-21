from Llibre import Llibre
from TV import TV
from reproductorMP3 import reproductorMP3

llista = []
precioRegular = 0.0
precioDescuento = 0.0

llista.append(TV(1000, "Samsung", 30))
llista.append(reproductorMP3(250, "Apple", "blue"))
llista.append(Llibre(34, "Sun press", 1992))
llista.append(Llibre(15, "Korea press", 1986))

for i in range(len(llista)):
    precioRegular = precioRegular + llista[i].getPreuRegular()
    precioDescuento = precioDescuento + llista[i].calculaPreuOferta()
    print(str(llista[i]))

print()
print("Precio regular: " + str(precioRegular))
print("Precio descuento: " + str(precioDescuento))
