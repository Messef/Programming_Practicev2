'''
For an upcoming holiday, Jiho plans on making a prix fixe menu for the restaurant. Customers at the restaurant will be able to choose the following:

1 Appetizer
2 Entrees
1 Side dish
2 Scoops of different ice cream flavors for dessert.

To accomplish all these choices, we are going to utilize the different types of 
arguments that we have learned so far. Now that we’ve set up our 
goals, hit “Run” to move on to the next step.'''
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
  }
  },
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def single_prixe_fixe_order(table_number,appetizer, *entrees, side_dish, **scoops):
    scoops=scoops.get('scoops')
    tables[table_number]['order']['food_items']=appetizer, entrees, side_dish,scoops
    print(tables)
single_prixe_fixe_order(2,'garlic bread', 'Omelette', 'Steak', side_dish='Fires', scoops=['Chocolate', 'Butterscotch'])

