# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments

#import makes_sales function from sales.py
from sales import Make_sales

#import set_currency, set_opening_stock, set_shop_name functions  from sales.py
from shopsettings import set_currency, set_opening_stock, set_shop_name

#import print_A_table, print_income_statement function  from reports.py
from reports import print_A_table, print_income_statement

#import make_purchase function  from purchaes.py
from purchases import make_purchase

#import  income, print_Income_table function  from income.py
from Income import record_income, print_Income_table

#import function print_Expenses_table, record_expense from Expenses.py
from Expenses import print_Expenses_table, record_expense

#import pyfiglet
import pyfiglet #This module enables logo styling 

# ask the user to enter the name. call set_shop_name function
business_name = set_shop_name() 

#Print the busniness name as a logo using pyfiglet
print(f"Welcome to\n{pyfiglet.figlet_format(business_name, font = 'digital' )}")


#Create empty list variables that will be used to store data from sales - reports
#Lines 31, 32,33,34,34 and 37 have empty lists used to store data(respective variable names)
sales_records = [] #stores sales data
purchases_records = [] #stores purchases data
income_records = [] # stores income data
opening_stock = [] # stores opening stock data
expenses_records = [] # stores expenses data
#store opening stock + purchases
available_stock = []

#Ask the user to select currency to trade in. call set_currency () function from shopsettings.py
currency = set_currency()

#Ask the user to set opening stock. call set_opening_stock() function from shopsettings.py
set_opening_stock(opening_stock)


#print("Opening Stock : " + currency + ". " +str(set_opening_stock(opening_stock)))
available_stock += opening_stock



def generate_reports():
    #print reports header
    print("-"*20 + "Reports Page" + "-"*20)
    #Print reports navigation options
    print('''
      1. Sales report.
      2. Purchases report.
      3. Expenses report.
      4. Income report
      5. Available_stock
      6. Profit and Loss
      7. Exit\n''')
    #Ask the user to choose one reports navigation option from 1-5
    choice1 = input("Enter a choice to navigate reports: ")
    if choice1 == "1":
    #if choice == sales, to print the sales report in a table call the print_A_table() function from reports.py
      print_A_table(sales_records)
    elif choice1 == "2":
    #if choice == purchases print the purchases report in a table using print_A_table() function from reports.py
      print_A_table(purchases_records)

    elif choice1 == "3":
    #if choice == reports print the expense report in a table using print_Expenses_table() from Expenses.py
      print_Expenses_table(expenses_records)
      
    elif choice1 == "4":
    #if choice == income print the purchases report in a table using print_Income_table from income.py
      print_Income_table(income_records)
    #if choice == income print the available stock report in a table using print_Income_table from income.py
    elif choice1 ==  "5":
      print_A_table(available_stock)
    elif choice1 == "6":
      #If choice is 6 print an income statement using print_income statement function from reports.py
      print("\n" + " "* 20 + business_name + "Income Statement" + " "* 20)
      print_income_statement(opening_stock, sales_records, purchases_records, income_records, expenses_records, currency)
    elif choice1 == "7":
      #If choice ==  7, do nothing
      return
    else:
      #If reports navigation choice not in 1-7 print message
      print("Option not available choose between 1-7!\n")

#Run the loop and only exit once the user enters 6



while True:
  #print main menu navigation options
  print(f'''
\n{'-'*30}Navigate Main Menu{'-'*30}\n
1. Sales
2. Purchases
3. Income
4. Expenses
5. Reports
6. Exit
''')
  #Ask the user to choose one of the navigation options 1-6. 6 exits
  choice1 = input("Enter a choice to navigate: ")
  #Check if choice == sales and call the sales function from sales.py
  if choice1  ==  "1" :
    #print message
    print("Sales of amount " +currency+". "+ str(Make_sales(sales_records, available_stock, currency)) +" was posted\n")
  #check if choice == 5 and call the report function
  elif choice1 == "5":
    while True:
      generate_reports()
    #Ask the user if the want to view other reports
      view_other_reports = input("View another report? [Y/N]: ")
      if view_other_reports in ["Yes", "yes", "y", "Y", "YES"]:
        generate_reports()
      else:
        break
  elif choice1 == "2":
    #If choice == 2,  call the make_purchase function() from purchases.py. print the amount of purchases posted
    print("Purchases of amount " + str(make_purchase(purchases_records)) +" was posted\n")
    #update the available goods by adding (opening_stock + purchases_records)
    available_stock += purchases_records
  elif choice1 == "3":
    #If choice ==  3. Call the record_income(function). Print amount of income posted
    print("Income worth " + currency +". "+str(record_income(income_records)) + " was posted\n")
  elif choice1 == "4":
    #If choice ==  3. Call the record_expense(function). Print amount of expense posted
    print("Expenses of amount " + currency+ ". " +  str(record_expense(expenses_records)) +" was posted\n")
  elif choice1 == "6":
    #If choice is 6 break
    break
  else:
    #If choice not in 1-6 print message
    print("Option not available! choose betwee 1-6!\n")