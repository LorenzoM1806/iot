import time
from bmp280 import BMP280
from smbus2 import SMBus, i2c_msg
import paho.mqtt.client as mqtt

# Initialize SMBus for lux sensor
lux_bus = SMBus(0)
lux_address = 0x23

# Initialize BMP280
bmp280_bus = SMBus(0)
bmp280_address = 0x76
bmp280 = BMP280(i2c_addr=bmp280_address, i2c_dev=bmp280_bus)

# Define the ThingSpeak MQTT credentials and topic
channelID = "2488188"
mqttUserName = "HiAzGyIgJTwnPQAJHSY2FSs"
clientID = "HiAzGyIgJTwnPQAJHSY2FSs"
mqttPass = "O6FA0SEYS1X9or7rEFE2Y6/d"
topic = "channels/2488188/publish"

server = "mqtt3.thingspeak.com"
port = 1883

client =  mqtt.Client(clientID)

client.username_pw_set(mqttUserName, mqttPass)

client.connect(server, port)

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

    # Format data for ThingSpeak
    payload = "field1={:.2f}&field2={:.2f}&field3={:.2f}".format(lux, temperature, pressure)

    # Publish data to ThingSpeak
    client.publish(topic, payload)

    # Print for debugging
    print("Lux: {:.2f} lux, Temperature: {:.2f} C, Pressure: {:.2f} hPa".format(lux, temperature, pressure))

    time.sleep(10)

