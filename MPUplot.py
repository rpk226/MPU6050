import serial
import matplotlib.pyplot as plt
from collections import deque

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

max_len = 100

# Raw data
ax_raw = deque([0]*max_len, maxlen=max_len)
ay_raw = deque([0]*max_len, maxlen=max_len)
az_raw = deque([0]*max_len, maxlen=max_len)

# Filtered data
ax_filt = deque([0]*max_len, maxlen=max_len)
ay_filt = deque([0]*max_len, maxlen=max_len)
az_filt = deque([0]*max_len, maxlen=max_len)

plt.ion()
fig, ax = plt.subplots()

# Plot lines
line_ax_raw, = ax.plot(ax_raw, label='Ax raw', linestyle='--')
line_ay_raw, = ax.plot(ay_raw, label='Ay raw', linestyle='--')
line_az_raw, = ax.plot(az_raw, label='Az raw', linestyle='--')

line_ax_filt, = ax.plot(ax_filt, label='Ax filtered')
line_ay_filt, = ax.plot(ay_filt, label='Ay filtered')
line_az_filt, = ax.plot(az_filt, label='Az filtered')

ax.set_ylim(-2, 2)
ax.set_title("Accelerometer: Raw vs Filtered")
ax.set_xlabel("Samples")
ax.set_ylabel("Acceleration (g)")
ax.legend()

while True:
    try:
        line = ser.readline().decode().strip()

        if not line:
            continue

        values = list(map(float, line.split(',')))

        if len(values) == 6:
            Ax, Ay, Az, Ax_f, Ay_f, Az_f = values

            # Append raw
            ax_raw.append(Ax)
            ay_raw.append(Ay)
            az_raw.append(Az)

            # Append filtered
            ax_filt.append(Ax_f)
            ay_filt.append(Ay_f)
            az_filt.append(Az_f)

            # Update plots
            line_ax_raw.set_ydata(ax_raw)
            line_ay_raw.set_ydata(ay_raw)
            line_az_raw.set_ydata(az_raw)

            line_ax_filt.set_ydata(ax_filt)
            line_ay_filt.set_ydata(ay_filt)
            line_az_filt.set_ydata(az_filt)

            plt.pause(0.01)

    except Exception as e:
        print("Error:", e)