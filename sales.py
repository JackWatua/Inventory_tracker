from shopsettings import align_text, align_quantity_or_amount, align_header

'''Create a sales function that accetpts three args (list1, list2, list3). The function checks if (a) a new sales is in the availbale stock, (b) the qunatity in the available stock records >= sales quantity and (c) price in the available stock record is <= to the sales price, proceed with sales(update sales record). If quantity and price entered is  numeric and alphanumeric, alert the user. If sales item not in available stock, ask the user if they want to check the available stock'''
def Make_sales(sales_record, available_stock, currency):
    print("\n", "-" * 20 + "Manage Sales", "-" * 20, "\n")
    print('''
    1. Make a new sale
    2. Exit
    ''')
    choice1 = input("Enter a choice eg. 1,2 to navigate: ")
    if choice1 == "1":
      while True:
      #ask the user to input an expense, break when the user types exit
        sale = input("Enter item, quantity, amount(eg. Handbags, 20, 100) type exit to exit: ")  
        if sale in ["Exit", "exit", "EXIT"]:
          break
        #print message in case of a wrong input
        elif len(sale.split(",")) <= 1 or len(sale.split(",")) > 3 or len(sale.split(",")) == 2 :
          print("Wrong Input. Check and try again")      
        else:
            #create a list of the existing incomes
            items = [available_stock[i]["Item"].lower() for i in range(len(available_stock))]
            #check if income item entered exists in the list above and adjust its new value
            if sale.split(",")[0].lower() in items:
              try:
                #the lines inside this try block will only run as long as the user does not enter an alphabetical or alphanumeric data as quantity and or price
                key = items.index(sale.split(",")[0].lower())
                if available_stock[key]["Item"].lower() == sale.split(",")[0].lower() and available_stock[key]["Quantity"] >= int(sale.split(",")[1]) and available_stock[key]["Amount"] <= int(sale.split(",")[2]):
                    if available_stock[key]["Quantity"] > int(sale.split(",")[1]): #if available quantity exceeds the sales quantity update available record with the new quantity
                        sales_record.append({"Item": sale.split(",")[0].lower(), "Quantity" : int(sale.split(",")[1]) , "Amount" : int(sale.split(",")[2]), "initial_cost": available_stock[key]["Amount"]})      
                        available_stock[key]["Quantity"] -= int(sale.split(",")[1])
                    else: #If item is sold out, remove it from the list of available items
                        sales_record.append({"Item": sale.split(",")[0].lower(), "Quantity" : int(sale.split(",")[1]) , "Amount" : int(sale.split(",")[2]), "initial_cost": available_stock[key]["Amount"]})
                        available_stock.pop(key)
                        print(f"{sale.split(',')[0].lower()} sold out!")
                else:
                    if available_stock[key]["Quantity"] < int(sale.split(",")[1]) or available_stock[key]["Amount"] > int(sale.split(",")[2]):
                        if available_stock[key]["Quantity"] < int(sale.split(",")[1]):
                            print(f"Check quantity and try again! .Only {available_stock[key]['Quantity']} {sale.split(',')[0].lower()} available")
                        else:
                            print(f"Check price and try again!. You are about to sale {sale.split(',')[0].lower()} below the acquisition price ( {currency} {available_stock[key]['Amount']} )")
              except ValueError:
                print("Qunatity and sales Price must be numeric!")
                
            else:
              #if not append the newly entered income in the income records
              print("Item not available\n")
              #The code might get bigger and the user may forget the available items. 
              #Ask the user whether they'd like to see what they already have whenever a wrong item message is printed
              view_available_stock = input("Would you like to view available items [Y/N]? ")
              if view_available_stock in ["Y", "Yes", "yes", "y"]:
                print_Available_stock(available_stock)
                print("\n")
              else:
                continue   
    elif choice1 == "2":
      return
    else:
      print("Option not available! choose 1 or 2!")
    #return item quantity *  item price
    return total_sales(sales_record)

#The function below calculates the total sales from sales_records
      
def total_sales(sales_records): #accepts one arguement a list 
  Value = 0
  Quantity = [sales_records[i]["Quantity"] for i in range(len(sales_records))]
  Price = [sales_records[i]["Amount"] for i in range (len(sales_records))]
  for i in range(len(Quantity)):
    Value += (Quantity[i] * Price[i])
  return Value


def cost_of_sales(record):
    cost = 0
    for i in range(len(record)):
        cost += record[i]["Quantity"] * record[i]["initial_cost"]
    return cost



#This function prints sales or purchase records as tables
def print_Available_stock(list):
  column1 = [list[i]["Item"] for i in range(len(list))]
  align_text(column1)
#make a list of items
  column2 = [str(list[i]["Quantity"]) for i in range(len(list))]
  align_quantity_or_amount(column2, "Quantity")
# make a list of quantities
  column3 = [list[i]["Amount"] for i in range(len(list))]
  table_header = ["ID", "Item", "Quantity", "Price"]
  align_header(column1, table_header, "Item")
  print(table_header[0] + "\t" + table_header[1] + "\t" * 3 + table_header[2]+ "\t" * 3+ table_header[3])
# print table header
  print("-" * 80)
  for i in range(len(column1)): #traverse lists and print them out as columns and rows
    print(str(i+1) + '\t' + column1[i].capitalize() + "\t" * 3 + str(column2[i]).capitalize() + "\t" * 3 + str(column3[i]).capitalize())
  print("-" * 80)
  print("Total"+ "\t" * 12 + str(total_available_stock(list)))# sum up purchase or sale
  print("-" * 80 + "\n")

def total_available_stock(available_stock_records): #accepts one arguement a list of dicts
  Value = 0
  Quantity = [available_stock_records[i]["Quantity"] for i in range(len(available_stock_records))]
  Price = [available_stock_records[i]["Amount"] for i in range (len(available_stock_records))]
  for i in range(len(Quantity)):
    Value += (Quantity[i] * Price[i])
  return Value