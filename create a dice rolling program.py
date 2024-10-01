#create a dice rolling program

import random
#unicode characters are required. Run the below print to have the characters needed 
#print ("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘ the unicode created

'┌─────────┐'
'│         │'
'│         │'
'│         │'
'└─────────┘'
#you need to format the dictionary to look like a dice though it looks like the below at first
# {3: ('┌─────────┐', '│         │', '│         │', '│         │', '└─────────┘'), 2: repeat ...} 

sam_dice = {
    1: ('┌─────────┐',
        '│         │',
        '│    ●    │',
        '│         │',
        '└─────────┘'),
    2: ('┌─────────┐',
        '│ ●       │',
        '│         │',
        '│       ● │',
        '└─────────┘'),
    3: ('┌─────────┐',
        '│ ●       │',
        '│    ●    │',
        '│       ● │',
        '└─────────┘'),
    4: ('┌─────────┐',
        '│ ●     ● │',
        '│         │',
        '│ ●     ● │',
        '└─────────┘'),
    5: ('┌─────────┐',
        '│ ●     ● │',
        '│    ●    │',
        '│ ●     ● │',
        '└─────────┘'),
    6: ('┌─────────┐',
        '│ ●     ● │',
        '│ ●     ● │',
        '│ ●     ● │',
        '└─────────┘')
        }
dice = []
total = 0
number_of_dice = int(input("how many dice are you using?"))

for die in range(number_of_dice): 
    dice.append(random.randint(1,6))

for die in range(number_of_dice):
    for x in sam_dice.get(dice[die]):
        print (x)

for die in dice:
    total+= die

print("total:", total)