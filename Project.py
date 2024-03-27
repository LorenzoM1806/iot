import time
from bmp280 import BMP280
from smbus2 import SMBus, i2c_msg

# Initialize SMBus for lux sensor
lux_bus = SMBus(0)
lux_address = 0x23

# Initialize BMP280
bmp280_bus = SMBus(0)
bmp280_address = 0x76
bmp280 = BMP280(i2c_addr=bmp280_address, i2c_dev=bmp280_bus)

def read_lux(bus, address):
    bus.write_byte(address, 0x10)
    bytes_read = bytearray(2)
    write = i2c_msg.write(address, [0x10])
    read = i2c_msg.read(address, 2)
    bus.i2c_rdwr(write, read)
    bytes_read = list(read)
    return (((bytes_read[0]&3)<<8) + bytes_read[1])/1.2

while True:
    # Read and print lux
    lux = read_lux(lux_bus, lux_address)
    print("{:.2f} lux".format(lux))

    # Read and print temperature and pressure
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    degree_sign = u"\N{DEGREE SIGN}"
    format_temp = "{:.2f}".format(temperature)
    print('Temperature = ' + format_temp + degree_sign + 'C')
    format_press = "{:.2f}".format(pressure)
    print('Pressure = ' + format_press + ' hPa \n')

    time.sleep(1)
