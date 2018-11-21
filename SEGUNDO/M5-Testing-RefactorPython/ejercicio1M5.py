'''

Se desea elaborar un algoritmo para transformar una cantidad de euros al número
mínimo de billetes y monedas necesarios para representarla. La cantidad siempre será
positiva y sin decimales.
Entrada
El algoritmo recibirá números enteros positivos. El algoritmo terminará la
transformación cuando reciba una cantidad de 0 euros. 

'''

def tipos_billetes():
    
    array_billetes=[500,200,100,50,20,10,5,2,1]#aqui van los billetes de mayor a menos
    return array_billetes

def cantidad_billetes(dinero):
    
    array_billetes_monedas= billetes(dinero)
    print(array_billetes_monedas)
    
def billetes(dinero):
    array_billetes = tipos_billetes()
    array_cont_billetes = [0,0,0,0,0,0,0,0,0]#la cantidad de billetes debe coincidir la longitud con array_billetes
    cantidad_billetes = 0
    i = 0
    continuar = True
    while (i < len(array_billetes)):
        print(dinero)
        if(dinero >= array_billetes[i]):
            dinero -= array_billetes[i]
            cantidad_billetes += 1
            
        else:
            array_cont_billetes[i] = cantidad_billetes
            cantidad_billetes = 0
            i += 1
    if(dinero == 0):
        return array_cont_billetes
    else:
        array_cont_billetes.append(dinero)

    return array_cont_billetes

    




dinero = int(input('Introduce la cantidad de dinero'))


array_resultado = cantidad_billetes(dinero)

input()

























