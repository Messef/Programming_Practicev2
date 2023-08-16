'''
PROBLEM: 
Jiho needs a way to assign new customers to the existing tables as they come in for their reservations. Define a new function called assign_table that will take three arguments (in this exact order):

table_number
name
vip_status
Our function assign_table should then use the following arguments to assign a new customer to a table in our dictionary tables. Use the table_number as the key and a list containing name and vip_status as the value.
'''
tables = {
  1: ['Jiho', False],
  2: [],
  3: ['C2', False],
  4: [None, True],
  5: [None, False],
  6: [None, True],
  7: [None, False],
}
'''MY CODE'''
def assign_table(table_number, name, vip_status):
  
     if tables[table_number]==[]: 
        tables[table_number].append(name)
        tables[table_number].append(vip_status)
     else: print("table is taken")
     print(tables[table_number])
     print(tables)
assign_table(2, 'C2', True)

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
#PROPER SOLUTION
print(tables)

# Checkpoint 2 & 5
def assign_table(table_number, name, vip_status=False): 
  tables[table_number] =  [name, vip_status]

# Checkpoint 3
assign_table(6, 'Yoni', False)
print(tables)

# Checkpoint 4
assign_table(table_number=3, name='Martha', vip_status=True)
print(tables)

# Checkpoint 6
assign_table(4, 'Karla')
print(tables)