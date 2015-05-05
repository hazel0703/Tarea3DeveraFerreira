'''
Created on 5/5/2015

@author: Adriana Devera  09-11286
         Carlos Ferreira 11-10323
'''

class BilleteraElectronica:
    def __init__(self, ID, Nombres, Apellidos, CI, PIN, creditos = []):
        self.ID = ID
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = creditos
        
    def recargar(self,monto,fecha,idEstablecimiento):
        self.creditos.append((monto,fecha,idEstablecimiento))

if __name__ == '__main__':
    pass