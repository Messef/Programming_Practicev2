'''Jiho is having a lot of success with our restaurant application. Unfortunately, our original design did not
 account for storing orders for each specific table. Jiho asked us to adjust our application to be able to store the orders that come in for each specific table and also be able to print out the order for the kitchen staff.

Take some time to review the adjusted structure of the program we created earlier. 
Note that tables is now dictionary with the table numbers as the keys. It also accounts for a new property called order. 
The assign_table function has also been adjusted to account for the changes.

Run the code to move onto the next checkpoint.
'''
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)
orders=[]
def take_order(*food):
  global orders
  for order in food:
    orders.append(food)
    order+=1

def assign_table(table_number, name, vip_status=False): 
  global orders
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = orders
