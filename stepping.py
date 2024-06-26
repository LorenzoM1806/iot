import wiringpi
from time import sleep
import sys

# Define GPIO pins
coil_A_1_pin = 3
coil_A_2_pin = 4
coil_B_1_pin = 6
coil_B_2_pin = 9

pinSwitch = 1

# Set up GPIO pins
wiringpi.wiringPiSetup()
wiringpi.pinMode(coil_A_1_pin, wiringpi.OUTPUT)
wiringpi.pinMode(coil_A_2_pin, wiringpi.OUTPUT)
wiringpi.pinMode(coil_B_1_pin, wiringpi.OUTPUT)
wiringpi.pinMode(coil_B_2_pin, wiringpi.OUTPUT)
wiringpi.pinMode(pinSwitch, 0)

def spin_motor(steps):
    print("Spinning motor...")
    for _ in range(steps):
        wiringpi.digitalWrite(coil_A_1_pin, 0)
        wiringpi.digitalWrite(coil_A_2_pin, 1)
        wiringpi.digitalWrite(coil_B_1_pin, 1)
        wiringpi.digitalWrite(coil_B_2_pin, 0)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 0)
        wiringpi.digitalWrite(coil_A_2_pin, 0)
        wiringpi.digitalWrite(coil_B_1_pin, 1)
        wiringpi.digitalWrite(coil_B_2_pin, 1)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 1)
        wiringpi.digitalWrite(coil_A_2_pin, 0)
        wiringpi.digitalWrite(coil_B_1_pin, 0)
        wiringpi.digitalWrite(coil_B_2_pin, 1)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 1)
        wiringpi.digitalWrite(coil_A_2_pin, 1)
        wiringpi.digitalWrite(coil_B_1_pin, 0)
        wiringpi.digitalWrite(coil_B_2_pin, 0)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 0)
        wiringpi.digitalWrite(coil_A_2_pin, 1)
        wiringpi.digitalWrite(coil_B_1_pin, 1)
        wiringpi.digitalWrite(coil_B_2_pin, 0)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 0)
        wiringpi.digitalWrite(coil_A_2_pin, 0)
        wiringpi.digitalWrite(coil_B_1_pin, 1)
        wiringpi.digitalWrite(coil_B_2_pin, 1)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 1)
        wiringpi.digitalWrite(coil_A_2_pin, 0)
        wiringpi.digitalWrite(coil_B_1_pin, 0)
        wiringpi.digitalWrite(coil_B_2_pin, 1)
        sleep(0.01)  # Delay 10 milliseconds
        wiringpi.digitalWrite(coil_A_1_pin, 1)
        wiringpi.digitalWrite(coil_A_2_pin, 0)
        wiringpi.digitalWrite(coil_B_1_pin, 0)
        wiringpi.digitalWrite(coil_B_2_pin, 1)
        sleep(0.01)  # Delay 10 milliseconds
        

def main():
        try:
            while True:
                if(wiringpi.digitalRead(pinSwitch) == 0):
                    # vlag
                    spin_motor(25)

                    wiringpi.digitalWrite(coil_A_1_pin, 0)
                    wiringpi.digitalWrite(coil_A_2_pin, 0)
                    wiringpi.digitalWrite(coil_B_1_pin, 0)
                    wiringpi.digitalWrite(coil_B_2_pin, 0)
                    print("start")
        except KeyboardInterrupt:
            print("Stopping motor...")
            wiringpi.digitalWrite(coil_A_1_pin, 0)
            wiringpi.digitalWrite(coil_A_2_pin, 0)
            wiringpi.digitalWrite(coil_B_1_pin, 0)
            wiringpi.digitalWrite(coil_B_2_pin, 0)
            

if __name__ == "__main__":
    main()
