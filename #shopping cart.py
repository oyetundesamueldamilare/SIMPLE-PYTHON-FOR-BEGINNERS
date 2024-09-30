#shopping cart

items = []
prices = []
total = 0

while True:
   item = input( 'enter the item you want to purcahse: press q to quit')
   if item == "q":
      break
   else:
      price = float(input(f"enter the price of the {item}: $"))
      items.append(item)
      prices.append(price)
print ('---ITEMS IN YOUR CART BELOW---')
for item in items:
   print (item, end=' ')

for price in prices:
   total+=price
print (f'your total is: {total}')
   



