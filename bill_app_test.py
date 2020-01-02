# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:55:49 2020

@author: raphl
"""

import unittest
#import bill_app
from bill_app import *

bills = read_bills()

class TestBillApp(unittest.TestCase):
    def test_read_bills(self):
        self.assertTrue(type(read_bills()==list))
        
    def test_get_message(self):
        self.assertTrue(len(get_message())==104)
        
    def test_write_bills(self):
        self.assertTrue(type(view_bills(bills)==list))
        
    def test_popular_company(self):
        data=pd.read_csv('bill.csv',header=None )
        data.columns=['company', 'customer', 'year', 'month', 'day', 'amount', 'note_type']
        data.to_csv('report.csv')
        self.assertIs(popular_company(bills),None)
        
        
        
        
if __name__ == '__main__':
    unittest.main()