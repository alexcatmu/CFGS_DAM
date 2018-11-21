class Semaforo:
    def __init__(self, p_color="vermell"):
        self.color = p_color

    def posacolor(self, p_color):
        self.color = p_color

    def diguemcolor(self):
        return self.color

semaforA = Semaforo()
semaforB = Semaforo("verd")
print(semaforA.diguemcolor())
print(semaforB.diguemcolor())
semaforA.posacolor("groc")
print(semaforA.diguemcolor())
print(semaforB.diguemcolor())