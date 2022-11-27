def make_purchase(purchases_records):
    print(f'''
    \n{'-' * 20} Manage Purchases {'-' * 20} \n
    1. Add a new purchase
    2. Exit
    \n''')
    choice1 = input("Enter a choice eg. 1,2 to navigate: ")
    if choice1 == "1":
        print("Record a new purchase. Enter \'exit\' to exit.")
        #Asking the user to enter a new sale i.e. item, quantity/ number of items, cost per item
        #Inputs seperated using commas
        while True:
          new_purchase = input("Enter item, quantinty, cost per item eg (Gucci shoes, 3, 250 ):  ")
        #finding the total amount of purchases by multiplying number of items * cost per item
          if new_purchase in ["Exit", "exit", "EXIT"]:
            break
          elif len(new_purchase.split(",")) != 3:
            print("Wrong Input. Check and try again")        
          else:
            try:
              # the section inside the try block will run the code as long as the quantity and price entered are numerical. If not, The program will execute the except block see line 

              #if there are no existing_purchases in the purchases records add the newly entered purchases
              if len(purchases_records) < 1:
                purchases_records.append({"Item": new_purchase.split(",")[0].lower(), "Quantity" : int(new_purchase.split(",")[1]), "Amount" : int(new_purchase.split(",")[2])})
              #else if the purchases record is not empty check if the purchases being entered already exits and add the value of the newly entered purchases to the existing
              else:
              #make a list of exixsting purchases from the purchases recordsd
                existing_purchases = [purchases_records[i]["Item"].lower() for i in range(len(purchases_records))]
                #if newly entered purchases in existing purchases
                if new_purchase.split(",")[0].lower() in existing_purchases:
                #get the position of the purchases input in the purchases records
                  key = existing_purchases.index(new_purchase.split(",")[0].lower())
                #adjust the exisiting purchases with the newly entered value if the price is equal to the existing purchase
                  if purchases_records[key]["Amount"] == int(new_purchase.split(",")[2]):
                    purchases_records[key]["Quantity"] += int(new_purchase.split(",")[1])
                  else:
                    #if new purchase exists but has a different price alert the user
                    print("You cannot enter same commodity with different prices. Rename Item and try again.")
                    #Ask the user if the want to update the price of the existing item
                    reprice_option = input("Do you wish to update the price for the item? Y/N: ")
                    #If yes update the price of the comodity
                    if reprice_option in ["Y", "Yes", "yes", "y"]:
                      purchases_records[key]["Quantity"] += int(new_purchase.split(",")[1])
                      purchases_records[key]["Amount"] = int(new_purchase.split(",")[2])
                    else:
                      #Else ask the user to rename the purchase item and try again
                      print("Rename Item and try again.")
                else:
                #if the purchases item does not exist, add the newly entered purchases to the purchases records. Append a dict with keys: purchases and ammount
                  purchases_records.append({"Item": new_purchase.split(",")[0].lower(), "Quantity" : int(new_purchase.split(",")[1]), "Amount" : int(new_purchase.split(",")[2])})       
            except ValueError:
              print("Items prices and quantities must be numerical")
    elif choice1 == "2":
      #If choice is 2. Exit the purchase function
      return
    else:
      #if choice not between 1-2 exit the purchase function
        print("Option not available choose 1 Or 2!")
        return 
    return total_purchases(purchases_records)




#Add a function that calculates the total purchases from purchases_records
def total_purchases(purchases_records):
  Value = 0
  Quantity = [purchases_records[i]["Quantity"] for i in range(len(purchases_records))]
  Price = [purchases_records[i]["Amount"] for i in range (len(purchases_records))]
  for i in range(len(Quantity)):
    Value += (Quantity[i] * Price[i])
  return Value


