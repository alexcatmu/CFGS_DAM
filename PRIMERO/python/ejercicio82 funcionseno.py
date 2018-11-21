import math
'''
2.5) Feu un procediment que, donat un angle, ens permeti saber el valor del
sinus, el cosinus i la tangent de l’angle subministrat. ( useu la llibreria
math ):
    void trigonomeitor( double angle, double  ref sin, double ref cos,
    double ref tan)‏

'''

#programa trigonometria

#funciones

def trigonomeitor(angle, sin, cos, tan):
    sin[0]=math.sin(angle)
    cos[0]=math.cos(angle)
    tan[0]=math.tan(angle)



#programa


angle = int(input('Introduce el angulo en radianes: '))
sin=[0]
cos = [0]
tan = [0]

print(angle, sin[0], cos[0], tan[0])
trigonomeitor(angle, sin, cos, tan)

print(angle, sin[0], cos[0], tan[0])









































