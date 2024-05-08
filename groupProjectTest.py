import time
import wiringpi
import sys

def blinkShort(_pin):
    for pin in _pin:
        wiringpi.digitalWrite(pin, 1)
        time.sleep(0.3)
        wiringpi.digitalWrite(pin, 0)

def blinkLong(_pin):
    for pin in _pin:
        wiringpi.digitalWrite(pin, 1)
        time.sleep(0.6)
        wiringpi.digitalWrite(pin, 0)

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

# setup
print("start")
pins = [2,3,4,5]
wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)

class Blink:
    # Main
    # Example for number 1
    sequence = switch_numbers(1)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pins)
        else:
            blinkLong(pins)

    time.sleep(2)

    # Example for number 9
    sequence = switch_numbers(9)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pins)
        else:
            blinkLong(pins)

    time.sleep(2)


    # Example for number 4
    sequence = switch_numbers(4)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pins)
        else:
            blinkLong(pins)

    time.sleep(2)


    # Example for number 5
    sequence = switch_numbers(5)
    print(sequence)
    for signal in sequence:
        if signal == 'short':
            blinkShort(pins)
        else:
            blinkLong(pins)
        
    time.sleep(2)


    print("done")
