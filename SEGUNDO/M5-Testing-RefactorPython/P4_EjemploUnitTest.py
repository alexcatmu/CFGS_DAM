
import os
import unittest

def P4_ejercicio2(a,b):
    while (a<0):
        if (a==b):
            a=a+1
        else:
            b=b-1
    c=a+b
    return c

def main():
    print("a:",end='')
    A=int(input())
    print("b:",end='')
    B=int(input())
    print (P4_ejercicio2(A,B),end='')

#pruebas unitarias (cobertura)
"""
* comenzar los casos con la palabar test

* en def test_Caso1(self):
        self.assertEqual(26,P4_ejercicio2(20,6))

traducen cada caso de prueba, en este caso seria: DIME-SI-SON-IGUALES(ElValorEsperado,P4_ejercicio2(Dato1Prueba1,Dato1Prueba1))

"""
class TestP4_ejercicio2(unittest.TestCase):
    def test_Caso1(self):
        self.assertEqual(26,P4_ejercicio2(20,6))
    def test_Caso2(self):
        self.assertEqual(38,P4_ejercicio2(19,19))
    def test_Caso3(self):
        self.assertEqual(27,P4_ejercicio2(19,8))

if __name__ == "__main__":
    #main()
    unittest.main()

