#This program can Only read and print the serial buffer's data.
#
#The software start from "" joins in "thereIsAboard()" and try to find a board.
#If it find a board it start reading. 
#If it doesen't find it join in "boardNotFound()" print an error.
#In "toString" method you can customize the output string.

import time 

try:

    import serial

except:

    print("Is required the installation of 'python3-serial' package")
    exit()

#-------------------------------------------------------------------------------------------------------------

maxTimes:int = 10 # max error times
timeSleep:float = 1.0 # scheduling time

#If not identify a board -------------------------------------------------------------------------------------------------------------

def boardNotFound():

    if maxTimes == 0:
        print("\nNO BOARD FOUND: exit.") #If it not indentify a board for 'timeSleep' times
        time.sleep(1.5)
        exit()

    else:
        print("\nERROR: no board found")    #If it can't indentify a board
        print("Searching board...")

    time.sleep(1.5)

#If indentify a board -------------------------------------------------------------------------------------------------------------

def thereIsAboard():

    board = serial.Serial("/dev/ttyACM0", 9600) #Detect if there is a board

    print("\n\n---[BOARD FOUND]---")
    time.sleep(1.5)

    while True:

        value = board.readline().decode()
        time.sleep(timeSleep)

        show(value)

#OUTPUT -------------------------------------------------------------------------------------------------------------

def toString(v):    #Customize the output

    return "\nOUTPUT:\t" + v

def show(v):
    
    print(toString(v))

#START -------------------------------------------------------------------------------------------------------------

while True:

    try:

        #Try to find a board
        thereIsAboard()

    #error
    except:

        #maxTimes' decrementation
        maxTimes -= 1

        #No board found
        boardNotFound()