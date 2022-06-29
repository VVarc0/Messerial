
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

#********************************************* DECLARATIONS *********************************************

maxTimes:int = 10 # max error times
timeSleep:float = 1.0 # scheduling time

defaultPort = "/dev/ttyACM0" # The port on which serial communication is to take place
defaultBoundrate = 9600 # bit/s

#********************************************************************************************************

#   If not identify a board

def boardNotFound():

    if maxTimes == 0:
        print("\nNO BOARD FOUND : exit().") #  If it not indentify a board for 'timeSleep' times
        time.sleep(timeSleep)
        exit()

    else:
        print("\n! ERROR: no board found \n  Searching board...")    #  If it can't indentify a board
        print()


#   If indentify a board

def connect(port = defaultPort, br = defaultBoundrate):

    board = serial.Serial(port, br)

    print("\n\n*******[BOARD FOUND]*******")

    while True:

        print(board.readline().decode())
        time.sleep(timeSleep)

#********************************************* START *********************************************

while True:
        
    #   Try to find a board
    try:

        connect()

    #   Exception in board searching
    except :

        #maxTimes' decrementation
        maxTimes -= 1

        #No board found
        boardNotFound()
        time.sleep(timeSleep)