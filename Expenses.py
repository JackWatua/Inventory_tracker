#Import table align_ment finctions from shopsettings
from shopsettings import align_text, align_header, align_quantity_or_amount


def record_expense(expense_records):
    print("\n", "-" * 20 + "Manage Expenses", "-" * 20, "\n")# print header
    # While True ask the user to input an expense, break when the user types exit
    while True:
      expense = input("Enter expense, amount eg(Motor, 100) type exit to exit: ")    
      if expense in ["Exit", "exit", "EXIT"]: #Break if input == Exit
        break
      elif len(expense.split(",")) !=  2: #if len of data separated with commas greater than 2 print message
        print("Wrong Input. Check and try again")
      else:
        if expense.split(",")[1].isalpha() or expense.split(",")[1].isalnum() : # Check if amount entered is alphabetical or alphanumeric
          print("Operation not possible! Expenses must be numerical") #print message
        else:
          #if there are no existing_expense in the expense records add the newly entered expense
          if len(expense_records) < 1:
              expense_records.append({"Expense": expense.split(",")[0].lower(), "Amount" : int(expense.split(",")[1])})
          #else if the expense record is not empty check if the expense being entered already exits and add the value of the newly entered expense to the existing
          else:
            #make a list of exixsting expenses from the expense_records
            existing_expense = [expense_records[i]["Expense"].lower() for i in range(len(expense_records))]
            #check if the newly entered expense exists in the expenses records
            if expense.split(",")[0].lower() in existing_expense:
              #get the position of the expense input in the expense records
              key = existing_expense.index(expense.split(",")[0].lower())
              #adjust expense value in the existing expense records
              expense_records[key]["Amount"] += int(expense.split(",")[1])
            
            else:
              #if the expense item does not exist, add the newly entered expense to the expense records
              expense_records.append({"Expense": expense.split(",")[0].lower(), "Amount" : int(expense.split(",")[1])})
    return total_expenses(expense_records)





  

#A function that calculates total expenses
def total_expenses(expenses_records):
  #Returns sum of all elements with key Amount inside expenses records
  return sum([expenses_records[i]["Amount"] for i in range(len(expenses_records))])

#Print expense report as a table
  '''
def print_Expenses_table(list):
    column1 = [list[i]["Expense"] for i in range(len(list))] #make a list of all Expenses
    column2 = [list[i]["Amount"] for i in range(len(list))] # make a list of all amounts
    print("ID" + "\t" +"Details" + "\t" * 3   + "Amount") # Print table head
    print("-" * 50)
    for i in range(len(column1)):
        print(str(i+1) + '\t' + column1[i].title() + "\t" * 4 + str(column2[i])) #print expenses and amounts as rows
    print("-" * 50)
    print("Total\t\t\t\t", str(sum(column2))) # print total expenses
    print("-" * 50 + "\n")
'''
  
def print_Expenses_table(list): #Accepts one arguement a list with dictionaries as its elements
    column1 = [list[i]["Expense"] for i in range(len(list))] #make a list of all list elememts with income key
    align_text(column1)
    column2 = [str(list[i]["Amount"]) for i in range(len(list))] # make a list of all amounts from the list of dicts
    align_quantity_or_amount(column1, "Amount")
    table_header = ["ID", "Expense", "Amount"]
    align_header(column1, table_header, "Expense")
    print(table_header[0] + "\t" + table_header[1] + "\t" * 3   + table_header[2]) # print table header
    print("-" * 50)
    for i in range(len(column1)):
        print(str(i+1) + '\t' + column1[i].title() + "\t" * 3 + column2[i]) # Print Expense and amount as rows
    print("-" * 50)
    print("Total\t\t\t\t", str(total_expenses(list)))
    print("-" * 50)