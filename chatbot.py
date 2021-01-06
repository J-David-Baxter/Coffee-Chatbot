from utils import print_message, get_size, order_latte, get_drink_type, order_mocha

# Coffee Bot function
def coffee_bot():
  print('Welcome to the cafe!')
  
  order_drink = 'y'
  drinks = []
  
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

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
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))


  



coffee_bot()