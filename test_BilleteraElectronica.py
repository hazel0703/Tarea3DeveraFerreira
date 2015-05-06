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
        BE.recargar(100, Fecha_recarga, "id")
        
    #Caso para probar que existe el metodo saldo
    def testMetodSaldo(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        BE.saldo()
        
    #Caso para probar si el metodo recargar realmente recarga el saldo
    def testRecargarsaldo(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 5, 5, 6, 15)
        BE.recargar(100, Fecha_recarga, "id")
        self.assertEqual(BE.saldo(), 100, "El saldo no es el correcto")
    
    #Caso para probar si el metodo consumir existe    
    def testMetodconsumir(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 5, 5, 6, 15)
        BE.recargar(100, Fecha_recarga, "id")
        Fecha_consumir = datetime(2015, 5, 5, 6, 15)
        BE.consumir(100, Fecha_consumir, "id", 4321)
     
    #Caso para probar si el metodo consumir realmente consume el saldo
    def testConsumirSaldo(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 5, 5, 6, 15)
        BE.recargar(100, Fecha_recarga, "id")
        Fecha_consumir = datetime(2015, 5, 7, 6, 15)
        BE.consumir(50, Fecha_consumir, "id", 4321)
        self.assertEqual(BE.saldo(), 50, "El saldo no es el correcto")
        
    #Caso para probar que al consumir el pin sea el mismo de la billetera
    def testVerificacionPIN(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 5, 5, 6, 15)
        BE.recargar(100, Fecha_recarga, "id")
        Fecha_consumir = datetime(2015, 5, 7, 6, 15)
        BE.consumir(50, Fecha_consumir, "id", 4321)
        self.assertEqual(BE.PIN, 4321, "PIN diferente al esperado")
    
    #Caso para probar el caso en que el PIN sea diferente   
    def testPINdiferente(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 5, 5, 6, 15)
        BE.recargar(100, Fecha_recarga, "id")
        Fecha_consumir = datetime(2015, 5, 7, 6, 15)
        self.assertRaises(Exception, BE.consumir ,50 , Fecha_consumir, "id", 321)
        
    #Caso para probar el caso en que al hacer un retiro el saldo quede negativo
    def testSaldoNegativo(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_consumir = datetime(2015, 5, 7, 6, 15)
        self.assertRaises(Exception, BE.consumir ,50 , Fecha_consumir, "id", 4321)
        
    def testRecargaNegativa(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)
        Fecha_recarga = datetime(2015, 5, 5, 6, 15)
        self.assertRaises(Exception, BE.recargar, -1, Fecha_recarga, "id")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()