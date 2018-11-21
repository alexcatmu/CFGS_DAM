from Compte import Compte
from compteProtegida import compteProtegida

cuentita = Compte("sdoicf23wcxwe", 1200.4)
print(cuentita)


cuentita = compteProtegida("dscerfr",1200.89,500)
print(cuentita.getSaldo())
cuentita._setSaldo(1400.78)
cuentita.ingresar(200)
print()
print()
print(cuentita)
print(cuentita.extreure(400))
print(cuentita.getSaldo())