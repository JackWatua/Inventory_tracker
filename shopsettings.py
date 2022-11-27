def set_currency():
  currency  = input("Choose a currency eg. $, £ , sh, NGN, Yen e.t.c: ")
  return currency



def set_opening_stock(opening_stock):
  print("\nPlease enter the items you have in the order, item, quantity, price. To exit, Enter 'exit'. if you have no opening stock, enter exit.\n")
  while True:
    items = input("Enter item, quantity, price eg. shoes, 10, 100:  ")
    if items in ["Exit", "exit"]:
      break
    elif len(items.split(",")) != 3:
      print("Wrong Input. Check and try again")        
      continue
    else:
      try:
        opening_stock.append({"Item": items.split(',')[0] , "Quantity" : int(items.split(',')[1]), "Amount": int(items.split(",")[2])})
      except ValueError:
        print("Item Quantity and price must be numerical!")
  return opening_stock


def total_opening_stock(list): #accepts one arguement a list 
  Value = 0
  Quantity = [list[i]["Quantity"] for i in range(len(list))]
  Price = [list[i]["Amount"] for i in range (len(list))]
  for i in range(len(Quantity)):
    Value += (Quantity[i] * Price[i])
  return Value
  
def set_shop_name():
  name = input("Enter the name of your business: ")
  return name

  
#Create a function align_text, accepts one arguement
def align_text(list): 
  if len(list) < 1:
    print("No records available")
  else:
    for i in range(len(list)):
      max_length= max([len(i) for i in list]) #Find the maximum str length/ longest string lenght
      if len(list[i]) == max_length: #if list item's lenght is equal to the longest string do nothing
        continue
      else:
        list[i] +=" " * (max_length - len(list[i])) # If list item's lenght is less than the longest string length, add empty spaces to equal the longest str length
  return list

def align_quantity_or_amount(list, key):
  for i in range(len(list)):
    list[i] += " " * (len(key) - len(list[i]))#Add empty spaces to figures 
  return list

def align_header(list, header, key):
  if len(list) <1:
    return
  else:
    max_len = max(len(i) for i in list)
    for i in range(len(header)):
      if header[i] == key:
        header[i] += " " * (max_len - len(header[1]))
      else:
        continue
    return header

