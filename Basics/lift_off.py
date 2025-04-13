# SIMPLE FORM: ⬇️

#for i in range(10):  #sets up a loop that run 10 times with i, taking values from 0 to 9
   # print(10 - i, end=' ') # inside the loop the code print 10-i and prints it
#print("Liftoff🚀") # this will print liftoff after the countdown

# ADVANCED FORM: ⬇️

import time    # this import time module for delay

# Asks the user if they are ready!
response = input("Are you ready for Launch? (yes/no):").strip().lower()

if response == 'yes':
    print("\nStarting Countdown...\n")
    for i in range(10):
        print(10-i, end=' ', flush = True) # end is used for horizontal diplay, and flush is used for delays that is used
        time.sleep(1) # 1 sec delay in countdown between numbers
    print("Liftoff🚀")

else:
    print("Launch aborted. Maybe next time!") # if the user input is not yes it will print this

