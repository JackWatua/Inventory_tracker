from sales import total_sales
from Expenses import total_expenses
from Income import total_income
from sales import cost_of_sales
from shopsettings import align_text, align_quantity_or_amount, align_header



#This function prints sales or purchase records as tables
def print_A_table(list):
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
  print("Total"+ "\t" * 12 + str(total_sale_or_purchase(list)))# sum up purchase or sale
  print("-" * 80 + "\n")


  
#The function below calculates total sale or puchase
def total_sale_or_purchase(list):
  Sum = 0
  for i in range (len([list[i]["Amount"] for i in range(len(list))])):
    Sum += int(list[i]["Amount"]) * int(list[i]["Quantity"]) #quantity * price
  return Sum

#print income statement
def print_income_statement(opening_Stock, sales, purchases, income, expenses, currency):
  Sales = total_sales(sales)
  cost_of_Sales = cost_of_sales(sales)
  gross_profit_or_loss = int(Sales) - int(cost_of_Sales)
  post_income = gross_profit_or_loss + total_income(income)
  net_profit_or_loss = post_income - total_expenses(expenses)
  print(f'''
  Details                                 {currency}
  {'-'*60}
  Sales                                   {Sales}
  less: Cost of Sales                                  
  Cost of Sale                           ({cost_of_Sales})
                                        ----------------------
  GROSS PROFIT OR LOSS                    {gross_profit_or_loss}
  
  Add: Income
  Total Income                            {total_income(income)}
                                        -----------------------
                                          {post_income}
  less: Expenseses
  Total Expenses                          {total_expenses(expenses)}
                                          ------------------------
  NET PROFIT OR LOSS                      {net_profit_or_loss}
                                                                  
  
  ''')