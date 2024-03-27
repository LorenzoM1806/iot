import wiringpi
import time

# Set up WiringPi
wiringpi.wiringPiSetup()

# Define the pin connected to the LDR sensor
ldr_pin = 3

# Threshold value to determine light or dark
threshold = 0.001  # Adjust this value based on your LDR sensor and environment

# Function to read data from the LDR sensor
def read_ldr():
    # Set the pin mode to output and low to discharge capacitor
    wiringpi.pinMode(ldr_pin, wiringpi.OUTPUT)
    wiringpi.digitalWrite(ldr_pin, wiringpi.LOW)
    time.sleep(0.1)  # Short delay to discharge capacitor

    # Set pin mode to input to measure the time until the capacitor charges enough
    wiringpi.pinMode(ldr_pin, wiringpi.INPUT)
    # Measure the time until the capacitor charges enough to change the pin state
    start_time = time.time()
    while wiringpi.digitalRead(ldr_pin) == wiringpi.LOW:
        pass
    end_time = time.time()
    return end_time - start_time

try:
    while True:
        # Read data from the LDR sensor
        ldr_data = read_ldr()
        # Check if it's light or dark based on the threshold and inverted logic
        if ldr_data > threshold:
            print("Dark")
        else:
            print("Light")
        time.sleep(1)  # Delay for 1 second
except KeyboardInterrupt:
    print("Exiting...")
