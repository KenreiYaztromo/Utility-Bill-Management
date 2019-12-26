# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:35:56 2019

@author: raphl
"""

import unittest

from management import read_bills

class TestBillManagement(unittest.TestCase):
    
    def test_management(self):
        bills= read_bills() 
        self.assertEquals(20,len(bills))
        self.assertEquals('Electric Ireland',bills[0][0])
        self.assertEquals(' credit',bills[19][0])
        
if __name__== '__main__':
    unittest.main()
    

#def billmanagement:
        
