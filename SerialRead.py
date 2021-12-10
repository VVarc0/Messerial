import serial
import time 

t_attesa_max = 10

#####################################################################################################

#If not indentify a board for 10 times
def endBoardNotFound():
    
    print("\nNO BOARD FOUND: exit the program") #Quando dopo 10 tentativi non viene rilevata nessuna scheda
    exit()

#If not identify a board
def boardNotFound():

    print("\nERROR: no board found")    #Se non viene rilevata nessuna scheda
    print("Searching board...")

    time.sleep(1.5)

#####################################################################################################

#If indentify a board
def thereIsAboard():

    board = serial.Serial("/dev/ttyACM0",9600, timeout=0)

    if t_attesa_max != 10:
        print("\nSUCCESS: board found") #se inizialmente non viene rilevata nessuna scheda    
    
    time.sleep(1)
    print("\n\nVALORI:")
    
    while True:

        value = board.readline().decode()

        print(value)  #Lettura sulla porta seriale          
            
        time.sleep(1) 

#####################################################################################################

while True:

    #try to find a board
    try:

        thereIsAboard()

    #error
    except:

        t_attesa_max -= 1

        if t_attesa_max == 0:

            endBoardNotFound()
            
        else:

            boardNotFound()

#####################################################################################################


