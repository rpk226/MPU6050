import matplotlib
matplotlib.use('TkAgg')
import serial
import matplotlib.pyplot as plt
from collections import deque

# Open serial port (check yours: /dev/ttyACM0 or COMx)
ser = serial.Serial('/dev/ttyACM0', 115200)

# Store last 100 samples
max_len = 100
ax_data = deque([0]*max_len, maxlen=max_len)
ay_data = deque([0]*max_len, maxlen=max_len)
az_data = deque([0]*max_len, maxlen=max_len)

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        values = list(map(float, line.split(',')))

        if len(values) == 7:
            Ax, Ay, Az, Temp, Gx, Gy, Gz = values

            ax_data.append(Ax)
            ay_data.append(Ay)
            az_data.append(Az)

            ax.clear()
            ax.plot(ax_data, label='Ax')
            ax.plot(ay_data, label='Ay')
            ax.plot(az_data, label='Az')

            ax.set_ylim(-2, 2)
            ax.legend()
            plt.pause(0.01)

    except:
        pass