import time
import wiringpi
import spidev
from ClassLCD import LCD
import sys

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

def blinkShort(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.5)

def blinkLong(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(1)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.5)

def switch_numbers(number):
    numbers = {
        1: ['short', 'long', 'long', 'long', 'long'],
        2: ['short', 'short', 'long', 'long', 'long'],
        3: ['short', 'short', 'short', 'long', 'long'],
        4: ['short', 'short', 'short', 'short', 'long'],
        5: ['short', 'short', 'short', 'short', 'short'],
        6: ['long', 'short', 'short', 'short', 'short'],
        7: ['long', 'long', 'short', 'short', 'short'],
        8: ['long', 'long', 'long', 'short', 'short'],
        9: ['long', 'long', 'long', 'long', 'short'],
        0: ['long', 'long', 'long', 'long', 'long'],
    }
    return numbers.get(number, "No number")

def blink():
    # Example for number 1
    sequence = switch_numbers(1)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pin)
        else:
            blinkLong(pin)

    time.sleep(2)

    # Example for number 9
    sequence = switch_numbers(9)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pin)
        else:
            blinkLong(pin)

    time.sleep(2)

    # Example for number 4
    sequence = switch_numbers(4)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pin)
        else:
            blinkLong(pin)

    time.sleep(2)

    # Example for number 5
    sequence = switch_numbers(5)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pin)
        else:
            blinkLong(pin)
        
    time.sleep(2)

    lcd_1.refresh()
    DeactivateLCD()


PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   15, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
pinSwitch = 0
pinSwitch2 = 1
pinSwitchEnter = 5
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)
wiringpi.pinMode(pinSwitch, 0)
wiringpi.pinMode(pinSwitch2, 0)
wiringpi.pinMode(pinSwitchEnter, 0)

pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)

i1=0
i2=0
i3=0
i4=0
position = 1
correctNum = "1945"
try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)

        if(wiringpi.digitalRead(pinSwitch2) == 0):
            if(position == 4):
                position = 1
            else:
                position += 1
        else:
            position += 0

        if(wiringpi.digitalRead(pinSwitch) == 0):
            lcd_1.put_string(str(i1) + str(i2) + str(i3) + str(i4))
            if(position == 1):
                if(i1 == 9):
                    i1 = 0
                else:
                    i1 = i1+1
            elif(position == 2):
                if(i2 == 9):
                    i2 = 0
                else:
                    i2 = i2+1
            elif(position == 3):
                if(i3 == 9):
                    i3 = 0
                else:
                    i3 = i3+1
            elif(position == 4):
                if(i4 == 9):
                    i4 = 0
                else:
                    i4 = i4+1
        else:
            lcd_1.put_string(str(i1) + str(i2) + str(i3) + str(i4))
        
        if(wiringpi.digitalRead(pinSwitchEnter) == 0):
            number = str(i1) + str(i2) + str(i3) + str(i4)
            if(number == correctNum):
                print("juist")

            else:
                print("fout")
                blink()
        
        lcd_1.refresh()
        DeactivateLCD()
    
    
        
        
except KeyboardInterrupt:
    ActivateLCD()
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")