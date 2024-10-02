#simple code to get correct user name until 

name = str(input ('enter your desired username'))
x = len(name)
while x <= 8:
    print ('your username cannot be less than 8 characters')
    name = input ('enter your desired username')
print ('username ok')