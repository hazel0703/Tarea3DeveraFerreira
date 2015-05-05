'''
Created on 5/5/2015

@author: Usuario
'''
import unittest
from BilleteraElectronica import * 


class Test(unittest.TestCase):


    def testClassBE(self):
        BilleteraElectronica(5,"Antonio", "Perez", 12345678, 4321)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()