from utils import print_message, get_size, order_latte, get_drink_type, order_mocha, order_brewed_coffee, order_tea, cup_holder, ice

# Coffee Bot function
def coffee_bot():
  print('Welcome to the cafe!')
  
  order_drink = 'y'
  drinks = []
  
  while order_drink == 'y':  
    drink_type = get_drink_type()
    size = get_size()
    ice_option = ice()

    if ice_option == 'y':
      drink_type = 'iced ' + drink_type
    elif ice_option == 'n':
      drink_type = drink_type
    else:
      print_message()
      ice()
    
    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    
    while True:
      order_drink = input("Would you like to order another drink? (y/n) \n> ")
      if order_drink in ['y', 'n']:
        break
  
  print("Okay, so I have:")
  for drink in drinks:
    print("-", drink)
  
  if len(drinks) > 1:
    cup_holder_status = cup_holder()
    print(cup_holder_status)
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))


coffee_bot()