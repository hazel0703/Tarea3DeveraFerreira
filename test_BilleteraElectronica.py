'''
Created on 5/5/2015

@author: Usuario
'''
import unittest
from BilleteraElectronica import *
from datetime import datetime 


class Test(unittest.TestCase):

    #Caso para comprobar que la clase Billetera electronica existe
    def testClassBE(self):
        BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        
    
    #Caso para probar que existe el metodo recargar
    def testMetodRecargar(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 4, 21, 6, 15)
        BE.recargar(100, Fecha_recarga, id)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()