#Import table align_ment finctions from shopsettings
from shopsettings import align_text, align_header, align_quantity_or_amount


def record_income(income_records):
    print("\n", "-" * 20 + "Manage Income", "-" * 20, "\n")# print header
    while True:
      #ask the user to input an Income, break when the user types exit
      income = input("Enter Income, amount eg(AHF ltd , 100) type exit to exit: ")    # Ask for input
      if income in ["Exit", "exit", "EXIT"]: # Break if income input is exit 
        break
      elif len(income.split(",")) != 2: # Break if split(",")  is greater than 2 
        print("Wrong Input. Check and try again")        
      else:
        try:
          #if there are no existing_income in the income records add the newly entered Income
          if len(income_records) < 1:
              income_records.append({"Income": income.split(",")[0].lower(), "Amount" : int(income.split(",")[1])})
          #else if the income record is not empty check if the income being entered already exits and add the value of the newly entered income to the existing
          else:
            #make a list of exixsting income from the income recordsd
            existing_income = [income_records[i]["Income"].lower() for i in range(len(income_records))]
            #if newly entered income in existing income
            if income.split(",")[0].lower() in existing_income:
              #get the position of the income input in the income records
              key = existing_income.index(income.split(",")[0].lower())
              #adjust the exisitind income with the newly entered value 
              income_records[key]["Amount"] += int(income.split(",")[1])
            else:
              #if the income item does not exist, add the newly entered income to the income records. Append a dict with keys: Income and ammount
              income_records.append({"Income": income.split(",")[0].lower(), "Amount" : int(income.split(",")[1])})
        except ValueError:
          print("Operation not possible!Income must be numerical")
    return total_income(income_records)


def total_income(income_records):
  #Return total income from income record. 
  return sum([income_records[i]["Amount"] for i in range(len(income_records))])



def print_Income_table(list): #Accepts one arguement a list with dictionaries as its elements
    column1 = [list[i]["Income"] for i in range(len(list))] #make a list of all list elememts with income key
    align_text(column1)
    column2 = [str(list[i]["Amount"]) for i in range(len(list))] # make a list of all amounts from the list of dicts
    align_quantity_or_amount(column1, "Amount")
    table_header = ["ID", "Income", "Amount"]
    align_header(column1, table_header, "Income")
    print(table_header[0] + "\t" + table_header[1] + "\t" * 3   + table_header[2]) # print table header
    print("-" * 50)
    for i in range(len(column1)):
        print(str(i+1) + '\t' + column1[i].title() + "\t" * 3 + column2[i]) # Print Income and amount as rows
    print("-" * 50)
    print("Total\t\t\t\t", str(total_income(list)))
    print("-" * 50)