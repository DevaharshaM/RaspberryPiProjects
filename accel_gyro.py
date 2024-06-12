from sense_hat import SenseHat
import time

sense = SenseHat()

# Function to get and print sensor data
def get_sensor_data():
    # Get accelerometer data
    accel = sense.get_accelerometer_raw()
    accel_x = accel['x']
    accel_y = accel['y']
    accel_z = accel['z']

    # Get gyroscope data
    gyro = sense.get_gyroscope_raw()
    gyro_x = gyro['x']
    gyro_y = gyro['y']
    gyro_z = gyro['z']

    # Print sensor data
    print(f"Accelerometer: x={accel_x:.2f}, y={accel_y:.2f}, z={accel_z:.2f}")
    print(f"Gyroscope: x={gyro_x:.2f}, y={gyro_y:.2f}, z={gyro_z:.2f}")


while True:
    get_sensor_data()
    time.sleep(1)
