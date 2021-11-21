from sys import argv
import serial
import time

t_attesa_max = 10

while True:
    try:

        SerialPortX = serial.Serial("/dev/ttyACM0",9600, timeout=0)

        if t_attesa_max != 10:
            print("\nSUCCESS: a board found")   #se inizialmente non viene rilevata nessuna scheda
        
        time.sleep(1)
        print("\n\nVALORI:")
    
        while True:
            print(SerialPortX.readline()) #Lettura sulla porta seriale
            time.sleep(1)
    #Errore        
    except:

        print("\nERROR: no board found")    #Se non viene rilevata nessuna scheda
        print("Searching board...")

        time.sleep(1.5)
        t_attesa_max -= 1

        if t_attesa_max == 0:
            print("\nNO BOARD FOUND: exit the program") #Quando dopo 10 tentativi non viene rilevata nessuna scheda
            exit()