class autobuses:
    sTarifa = 1.20
    def __init__(self, c_model = "",  c_capacidad = 0, c_ruta = ""):
        self.model = c_model
        self.capacidad = c_capacidad
        self.ruta = c_ruta

a = autobuses("mercedaco", 3000, "pol poblao")
print(a.sTarifa)
a.sTarifa = 300
print(a.sTarifa)
b = autobuses("citroen", 5, "viladecans")
autobuses.sTarifa = 400
print(autobuses.sTarifa)
print(a.sTarifa)
print(b.sTarifa)
