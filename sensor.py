import os
import time

# Define GPIO pins
TRIG_PIN = 9  
ECHO_PIN = 10 

# Set the GPIO pin modes
def setup_gpio(pin, mode):
    try:
        with open('/sys/class/gpio/export', 'w') as export_file:
            export_file.write(str(pin))
        print(f"GPIO pin {pin} exported successfully")
    except Exception as e:
        print(f"Failed to export GPIO pin {pin}: {e}")
        
    try:
        with open(f'/sys/class/gpio/gpio{pin}/direction', 'w') as direction_file:
            direction_file.write(mode)
        print(f"GPIO pin {pin} direction set to {mode}")
    except Exception as e:
        print(f"Failed to set direction for GPIO pin {pin}: {e}")


def set_gpio(pin, value):
    with open(f'/sys/class/gpio/gpio{pin}/value', 'w') as value_file:
        value_file.write(str(value))

def get_gpio(pin):
    with open(f'/sys/class/gpio/gpio{pin}/value', 'r') as value_file:
        return value_file.read()

# Setup GPIO
setup_gpio(TRIG_PIN, 'out')
setup_gpio(ECHO_PIN, 'in')

# Main loop
try:
    while True:
        # Set TRIG_PIN high
        set_gpio(TRIG_PIN, 1)
        
        # Wait for 10 microseconds
        time.sleep(0.00001)
        
        # Set TRIG_PIN low
        set_gpio(TRIG_PIN, 0)

        # Wait until the input pin is low
        while get_gpio(ECHO_PIN) == '0\n':
            pass
        
        # Record the time when the input pin goes high
        signal_high = time.time()

        # Wait until the input pin is high
        while get_gpio(ECHO_PIN) == '1\n':
            pass
        
        # Record the time when the input pin goes low
        signal_low = time.time()
        
        # Calculate time passed
        time_passed = signal_low - signal_high
        
        # Calculate distance (speed of sound is approximately 343 m/s)
        distance = time_passed * 34300 / 2  # Divide by 2 as it's the time for the sound to travel back and forth
        
        print("Distance:", distance, "cm")
        
        # Wait for 0.5 seconds
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Measurement stopped by user")

finally:
    # Clean up GPIO resources
    os.system(f'echo {TRIG_PIN} > /sys/class/gpio/unexport')
    os.system(f'echo {ECHO_PIN} > /sys/class/gpio/unexport')
