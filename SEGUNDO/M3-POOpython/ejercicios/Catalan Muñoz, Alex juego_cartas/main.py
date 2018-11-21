import os
from setYmig import setYmig
from excepciones import NumJugadores

jugar = setYmig()
valores_jugador = []
string_jugadores = []

valor_todos_jugadores = []
string_todos_jugadores = []
a = "\x1b["
b = "\x1b[0m"
array_colores = ["0;30;31m","0;30;32m","0;30;33m","0;30;34m","0;34;35m","0;30;36m","0;30;37m"]

correcto = False
while(not correcto):
    try:
        num_jugadores = int(input("Cuantos jugadores sois? 7 max, 1 min\n"))
        if(num_jugadores < 1 or num_jugadores > 7):
            raise NumJugadores(num_jugadores)
        correcto = True
    except:
        print("Valor incorrecto.\n")


while (not(isinstance(num_jugadores,int)) or num_jugadores < 1 or num_jugadores > 10):
    num_jugadores = input("Cuantos jugadores sois? 10 max, 1 min\n")

num_jugadores = int(num_jugadores)

num_color = 0
for i in range(num_jugadores):
    continuar = True
    print(a+array_colores[num_color]+"Adelante jugador "+str(i+1))
    string_jugadores = []
    valores_jugador = []
    puntuacion_acumulada = 0
    while(continuar):
        valor_carta = jugar.valorCarta()
        string_carta = jugar.Cartastring()
        valores_jugador.append(valor_carta)
        string_jugadores.append(string_carta)
        print(string_carta)
        puntuacion_acumulada += valor_carta
        print("Puntuación acumulada: "+str(puntuacion_acumulada))

        if(puntuacion_acumulada < 7.5):
            seguir = input("Quieres continuar?(s para continuar)")
        else:
            continuar = False
            print("No puedes pedir más cartas"+b)
        if(seguir != "s"):
            continuar = False

        if(continuar == False):
            num_color += 1
            if(num_color == len(array_colores)):
                num_color = 0
            print(b)
    valor_todos_jugadores.append(valores_jugador)
    string_todos_jugadores.append(string_jugadores)

stringo = ""
valor_final_jugadores = []
num_color = 0
for i in range(len(valor_todos_jugadores)):
    valor_final_jugador = 0
    stringo += a+array_colores[num_color]+"Jugador "+str(i+1)+"\n"
    for j in range(len(valor_todos_jugadores[i])):
        valor_final_jugador += valor_todos_jugadores[i][j]
        stringo += str(string_todos_jugadores[i][j])+" "+str(valor_todos_jugadores[i][j])+" puntos\n"

    valor_final_jugadores.append(valor_final_jugador)
    stringo += "Puntuacion total: "+str(valor_final_jugador)+"\n\n"+b

    num_color += 1
    if(num_color == len(array_colores)):
        num_color = 0
stringo += "\n"
print(stringo)

print(jugar.CartasDeBanca())
input("Presione intro para ver resultados")
os.system("cls")
print(jugar.GanaOpierde(valor_final_jugadores))
print()