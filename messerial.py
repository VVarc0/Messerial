
#! /usr/bin/python3

#-------------------------------------------------------------------------------------------------------------
#   This program can Only read and print the serial buffer's data.
#
#   The software start from "" joins in "thereIsAboard()" and try to find a board.
#   If it find a board it start reading. 
#   If it doesen't find it join in "boardNotFound()" print an error.
#   In "toString" method you can customize the output string.
#   
#   If you need read from more board you need to add more ports.
#-------------------------------------------------------------------------------------------------------------

import time 

try:    
    
    import serial

except:

    print("Is required the installation of 'python3-serial' package")
    exit()

#-------------------------------------------------------------------------------------------------------------
#   DECLARATIONS
#-------------------------------------------------------------------------------------------------------------

maxTimes:int = 10 # max error times
timeSleep:float = 1.0 # scheduling time

port1 = "/dev/ttyACM0" # The port on which serial communication is to take place
output = "" #   Customize the python3 script output (This not customize the arduino's output)

#-------------------------------------------------------------------------------------------------------------

#   If not identify a board

def boardNotFound():

    if maxTimes == 0:
        print("\nNO BOARD FOUND on ",port1,": exit.") #  If it not indentify a board for 'timeSleep' times
        time.sleep(1.5)
        exit()

    else:
        print("\nERROR: no board found on ",port1)    #  If it can't indentify a board
        print("Searching board...")

    time.sleep(1.5)

#   If indentify a board

def connectToBoard():

    board = serial.Serial(port1, 9600) # Detect if there is a board

    print("\n\n---[BOARD FOUND]---")
    time.sleep(1.5)

    while True:

        value = board.readline().decode()
        time.sleep(timeSleep)

        show(value)

#-------------------------------------------------------------------------------------------------------------
#   OUTPUT
#-------------------------------------------------------------------------------------------------------------

def toString(val):    
    return output, val #    The script's output string

def show(val):    
    print(toString(val))

#-------------------------------------------------------------------------------------------------------------
#   START
#-------------------------------------------------------------------------------------------------------------
while True:
        
    #   Try to find a board
    try:

        connectToBoard()

    #   Exception in board searching
    except:

        #maxTimes' decrementation
        maxTimes -= 1

        #No board found
        boardNotFound()
