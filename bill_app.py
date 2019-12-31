# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 02:12:05 2019

@author: raphl
"""
import csv
import pandas as pd



def read_bills():
    return [[col.strip() for col in row.strip().split(',')]
             for row in open('bill.csv') if len(row) > 1]

def write_bills(bills):
    new_bill=[input("company: "),input("customer: "),input("year[YYYY]: "),input("month[MM]: "),input("day[DD]: "),input("amount[€XX.XX]: "),input("type[credit/debit]: ")]
    with open ('bill.csv','a') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(new_bill)
        
    
        

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit\n'

def display_menu():
    print(get_message())

def view_bills(bills):
    bills = read_bills()
    for bill in bills:
        print(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6])

def report_by_year():
    report=pd.read_csv('report.csv',index_col=0)
    totals_by_year = report.groupby(by=['year', 'note_type'])['amount'].sum().reset_index()
    print(totals_by_year)
    
def report_sorted_by_date():
    report=pd.read_csv('report.csv',index_col=0)
    sorted_by_date=report.sort_values(by=['year','month','day'])
    print(sorted_by_date)   
    
def highest_debit_and_credit():
    report=pd.read_csv('report.csv',index_col=0)
    highest_debit_and_credit=report.groupby(['note_type'])['amount'].max()
    print(highest_debit_and_credit)

def successfull_company():
    report=pd.read_csv('report.csv',index_col=0)
    print(report.groupby(['company']).size().reset_index(name='counts').sort_values(by='counts',ascending = False))
    
def popular_company():
    report=pd.read_csv('report.csv',index_col=0)
    popular_company=report.groupby('company')['company'].count().idxmax()
    print('The most popular company is {}'.format(popular_company))
    
def process_choice(bills):
    choice = input('Please enter an option:')
    while choice != '5':
        if choice == '1':
            view_bills(bills)
        elif choice =='2':
            write_bills(bills)
        elif choice =='3':
            data=pd.read_csv('bill.csv')
            data.columns=['company', 'customer', 'year', 'month', 'day', 'amount', 'note_type']
            data.to_csv('report.csv')
            print('\nChoose your report\n' + \
            '1: Report Total Debit and Credit by year\n2: The most popular' 
            'company\n3: report of bills sorted by date\n4: highest debit nd credit\n'
            '5: most successful companies\n8: Exit')
            sub_choice = input('Please enter an option:')
            while sub_choice != '8':
                if sub_choice =='1':
                    report_by_year()
                elif sub_choice =='2':
                    popular_company()
                elif sub_choice =='3':
                    report_sorted_by_date()
                elif sub_choice =='4':
                    highest_debit_and_credit()
                elif sub_choice =='5':
                    successfull_company()                    
                print('\nChoose your report\n' + \
                '1: Report Total Debit and Credit by year\n2: The most popular' 
                'company\n3: report of bills sorted by date\n4: highest debit nd credit\n'
                '5: most successful companies\n8: Exit')                    
                sub_choice= input('Please enter an option:')
                
        elif choice == '4':
            print('The terms of the billing management company')
            print('URL to paste where the terms have been uploaded')
        print('\n')
        display_menu()
        choice = input('Please enter an option:')

def main():
    #bills = read_bills()
    display_menu()
    process_choice(read_bills())
    #write_bills(bills)
    
if __name__ == '__main__':
    main()