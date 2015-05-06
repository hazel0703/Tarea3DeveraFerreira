'''
Created on 5/5/2015

@author: Adriana Devera  09-11286
         Carlos Ferreira 11-10323
'''

# -*- coding: utf-8 -*-

class BilleteraElectronica:
    def __init__(self, ID, Nombres, Apellidos, CI, PIN):
        self.ID = ID
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = []
        self.monto = 0
        self.debitos = []
        
        
    def recargar(self,monto,fecha,idEstablecimiento):
        if monto <= 0:
            raise Exception("Monto de la recarga no puede ser negativo")
        self.monto += monto
        self.creditos.append((monto,fecha,idEstablecimiento))
        
    def saldo(self):
        return self.monto
    
    def consumir(self, monto, fecha, idEstablecimiento, PIN):
        if monto <= 0:
            raise Exception("Monto del consumo no puede ser negativo")
        if self.PIN != PIN:
            raise Exception("PIN incorrecto")
        elif self.monto - monto < 0:
            raise Exception("Insuficiente creditos para la realizacion de la operacion")
            
        self.debitos.append((monto, fecha, idEstablecimiento))
        self.monto -= monto
       
            

if __name__ == '__main__':
    pass