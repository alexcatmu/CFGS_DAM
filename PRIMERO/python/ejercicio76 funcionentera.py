'''
1.9) Programeu una funció “llegirXifraSencera”, que permeti llegir
un número sencer pel teclat i el retorni al programa.
			int llegirXifraSencera()‏
La funció llegirà el número usant repetidament input()
(tecla a tecla). Per a cada caràcter llegit verifiquem si és
un número ( ‘0’, ‘1’,....’9’ ). En aquest cas es mostra per
pantalla (print) i el guardem dins d’una array/llista. Si la
tecla apretada no és numèrica ( p.ex. ‘K’ ) ignorem a l’usuari i sortim.

En aquest moment, la funció ha de convertir els char que té a
l’array en un número sencer ( un int ), que és el que la funció retorna:
'''



#programa enteros

#funciones

def llegirXifraSencera():
    num = input()
    total = 0

    while (ord(num)>= 48 and ord(num) <= 57):
        num = int(num)
        total = (total * 10) + num

        
        num = input()



    return total




#programa


total = llegirXifraSencera()


print(total)













