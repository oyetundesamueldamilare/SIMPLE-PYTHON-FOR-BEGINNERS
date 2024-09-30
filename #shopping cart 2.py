#shopping cart 2

menu = {'rice': 20, 'beans': 30, 'chicken': 50, 'plantain': 20, 'fish': 50, 'potato': 30, 'meat': 50}

#x = menu.keys()
#print (x)
#for y in menu.keys():
#    print (y)

cart = []
total = 0

print ('----------MENU-----------')
for key, value in menu.items():
    print (f'{key:10}: ${value:.2f}')
print ('--------------------------')

while True:
    food =input('select an item on the list or q to quit').lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print ()
#print (cart)

for food in cart:
    total += menu.get(food)
    print (food)
print()
print ('--------------------')
print (f'your bill is: ${total:.2f}')
