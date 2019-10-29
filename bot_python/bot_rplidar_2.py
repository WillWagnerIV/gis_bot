from rplidar import RPLidar
import matplotlib.pyplot as plt







lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

lidar.start_motor()
motor_running = lidar.motor
print ('Start Motor:', str(motor_running))

ax = plt.subplot(111, projection='polar')

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    # print (scan)
    for measurement in scan:
        r = measurement[1]
        theta =measurement[2]
        
        ax.plot(theta, r)

    if i > 10:
        break





# fig, ax = plt.subplots()
# ax.scatter(x, y, c="black", s=2, alpha=0.5)

# ax.set_xlabel(r'$\Delta_i$', fontsize=15)
# ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
# ax.set_title('Volume and percent change')

# ax.grid(True)
# fig.tight_layout()

plt.show()








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