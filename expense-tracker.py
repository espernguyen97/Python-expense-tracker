import numpy as np
import pandas as pd
from datetime import date

#Create empty lists

GOODS_OR_SERVICES = []
PRICES = []
DATES = []
EXPENSE_TYPE = []

def addExpense (good_or_service,price,date,expense_type):
    GOODS_OR_SERVICES.append(good_or_service)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPE.append(expense_type)

#Options for main program    

option = -1
while(option != 0):
    print('Welcome to the expense tracker!')
    print('1. Add Grocery Expense')
    print('2. Add Utility Expense')
    print('3. Add Transportation Expense')
    print('4. Show and Save The Expense Report')
    print('0. Exit')
    option = int(input('Choose an option:'))
    print()
    if option == 0:
        print('Exititng the program')
        break
    elif option == 1:
        print('Adding Grocery Expense')
        expense_type = 'FOOD'
    elif option == 2:
        print('Adding Utility Expense')
        expense_type = 'UTILITY'
    elif option == 3:
        print('Adding Transportation Expense')
        expense_type = 'TRANSPORTATION'
    elif option == 4:
        expense_report = pd.DataFrame()
        expense_report['GOODS_OR_SERVICE'] = GOODS_OR_SERVICES
        expense_report['PRICES'] = PRICES
        expense_report['DATES'] = DATES
        expense_report['EXPENSES_TYPE'] = EXPENSE_TYPE 
    
        expense_report.to_csv('expenses.csv')
    
        print(expense_report)
    else:
        print('Incorrect Option. Please Choose 0,1,2,3, or 4 ')
    
    if option == 1 or option == 2 or option == 3:
        good_or_service = input('Please enter the goods or services for the expense type' + expense_type +':'+'\n')
        price = float(input('Enter the price of the goods or services' + expense_type + ':' +'\n'))
        today = date.today()
        addExpense (good_or_service,price,today,expense_type)
        print()
    

    
