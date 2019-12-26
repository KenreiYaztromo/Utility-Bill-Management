# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:34:56 2019

@author: raphl
"""

from datetime import datetime

def read_bills():    
    pre=datetime.now()
    #bills=[line.strip().split(',')for line in open('bills.csv) if len(line>1)]    
    bills=[]
    bills_file=open('bill.csv')
    for line in bills_file:
            if len(line)>1:
                bills.append(line.strip().split(','))
                bills[-1][-1]=bills[-1][-1].strip()
    print(datetime.now()-pre)
    return bills


def display_menu():
    print('Hello, Welcome to the Bill maanagement Company')
    print('1: View Bills|n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit')    


def view_bills(bills):
    for bill in bills:
        print(bills[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6])


def process_choice(bills):
    choice= input('Please enter an option:')
    while choice != '5':
        if choice=='1':
            view_bills(bills)
        elif choice=='4':
            print('The terms of the billing management company')           
        choice= input('Please enter an option:')

def write_bills(bills):
    bill_file= open('bills.csv','w')
    for bill in bills:
        bill_file.write(', '.join(bill)+'\n')
        
        
def main():
    bills=read_bills()
    display_menu()
    process_choice(bills)
    write_bills(bills)

    
if __name__== '__main__':
    main()
    