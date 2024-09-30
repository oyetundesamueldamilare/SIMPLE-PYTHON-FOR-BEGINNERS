#this is a timer

import time #import time from the time lib

my_time = int((input('enter time in seconds'))) #input the required time in seconds

for x in reversed(range (0, my_time, 1)): #reversed will start the count down
    seconds = x % 60                       # % shows that at every count to 60, it goes back to 1
    minutes = int(x/60) % 60                # 60 seconds make a minute
    hours = int (x/3600) % 60               #3600 seconds make an hour
    print (f'{hours:02}:{minutes:02}:{seconds:02}') #the :02 gives the shape the timer should take, with 0 saying it 00 not 0 and 2 reinstating the numbers allowable

    time.sleep(1)       #time.sleep(1) is a counter with an increment of 1
    