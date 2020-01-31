
  


"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=16)

# Define Standard Servo at pin 0
# servo0 = kit.servo[0].Servo(activa)


print ('Moving standard servo on bus 0')
kit.servo[0].actuation_range = 190
kit.servo[0].set_pulse_width_range(1000, 2000)
kit.servo[0].angle = 0
time.sleep(2.5)
kit.servo[0].angle = 90

c = input ("Press Enter to continue")

# print ('Moving continuous Servo on bus 0')
# kit.continuous_servo[0].throttle = 1
# time.sleep(2.5)
# kit.continuous_servo[0].throttle = -1
# time.sleep(2.5)

print ('Moving continuous Servo on bus 1')
kit.continuous_servo[1].throttle = 1
time.sleep(2.5)
kit.continuous_servo[1].throttle = -1
time.sleep(2.5)


# c = input ("Press Enter to continue")

# print ('Returning standard to center')
# kit.servo[0].angle = 0


c = input ("Press Enter to continue")

print ('Stopping Continuous')
# kit.continuous_servo[0].throttle = 0
time.sleep(.5)
kit.continuous_servo[1].throttle = 0
