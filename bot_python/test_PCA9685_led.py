import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)


pca.frequency = 60

led_channel = pca.channels[15]


# 3 levels of brightness (max = 65534 = 0xffff)
led_channel.duty_cycle = 0xffff

led_channel.duty_cycle = 0

led_channel.duty_cycle = 30000



# Increase brightness:
for i in range(0xffff):
    led_channel.duty_cycle = i
    print (i)

print ('Max brightness =',i)
c = input('Press any key to continue.')
     
# Decrease brightness:
for i in range(0xffff, 0, -1):
    led_channel.duty_cycle = i
    print (i)