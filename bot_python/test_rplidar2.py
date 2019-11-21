from rplidar import RPLidar
lidar = RPLidar('/dev/uart_bridge')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

lidar.start_motor()
motor_running = lidar.motor
print ('Start Motor:', str(motor_running))

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    print (scan)
    if i > 10:
        break

print ('Should Stop, sTop Motor, disconnect')
lidar.stop()

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

lidar.stop_motor()
motor_running = lidar.motor
print ('Motor:', str(motor_running))

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

lidar.disconnect()

try:

        info = lidar.get_info()
        print(info)

        health = lidar.get_health()
        print(health)

except:
        print("Disconnected")

