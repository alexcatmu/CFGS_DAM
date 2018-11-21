fp_mensaje = open('quijoteMensaje.txt','r')
fp_quijote = open('quijote.txt','r')

EOF = False
aux = 0
while(EOF == False):
    
        leido = fp_mensaje.readline()
        
        if(leido != ''):
            
            aux += int(leido)
            fp_quijote.seek(aux,0)
            escribe = fp_mensaje.readline()
            mensaje = fp_quijote.read(int(escribe))
            print(mensaje)
            
        else:
            EOF = True

fp_mensaje.close()
fp_quijote.close()
































