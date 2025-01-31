import serial
import matplotlib.pyplot as plt
from collections import deque

# Serial configuration
SERIAL_PORT = 'COM6'  # Change this to the correct port
BAUD_RATE = 115200
DATA_POINTS = 100  # Number of points on the graph

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Real-time plot setup
plt.ion()
fig, ax = plt.subplots()
y_data = deque([0] * DATA_POINTS, maxlen=DATA_POINTS)
x_data = list(range(DATA_POINTS))
line, = ax.plot(x_data, y_data)

ax.set_ylim(0, 4095)  # ADC range for 12-bit
ax.set_xlabel('Time')
ax.set_ylabel('Sensor Value')
ax.set_title('EMG Sensor Live Plot')

try:
    while True:
        line_data = ser.readline().decode('utf-8').strip()  # Read and decode the data
        if line_data:  # Check if the data is not empty
            try:
                value = int(line_data)  # Convert the data to an integer (sensor value)
                y_data.append(value)  # Add the value to the y_data deque
                line.set_ydata(y_data)  # Update the y-data of the plot line
                plt.draw()  # Redraw the plot
                plt.pause(0.01)  # Pause to update the plot
            except ValueError:
                pass  # If the data can't be converted to an integer, skip it
except KeyboardInterrupt:
    print("Plotting stopped by user.")
finally:
    ser.close()
    plt.ioff()
    plt.show()
