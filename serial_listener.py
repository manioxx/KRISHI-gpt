import serial
import time
import json

# Set up the serial connection to match the Arduino settings
arduino_port = "COM5"  # Change this to your correct serial port (COMx for Windows, /dev/ttyUSBx for Linux/macOS)
baud_rate = 9600        # Match the baud rate used by Arduino

# Open the serial connection
ser = serial.Serial(arduino_port, baud_rate)

# Wait for the Arduino to initialize
time.sleep(2)

print("Listening for data from Arduino...")

# Continuously listen for data
while True:
    try:
        # Read the incoming serial data
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()  # Read data from serial and decode it to string
            
            # Parse the JSON data
            sensor_data = json.loads(data)
            
            # Print the parsed sensor data
            print(f"Temperature: {sensor_data['temperature']} °C")
            print(f"Humidity: {sensor_data['humidity']} %")
            print(f"Soil Moisture: {sensor_data['soil_moisture']} %")
            print(f"LDR Value: {sensor_data['ldr_value']}")
            print(f"pH: {sensor_data['ph']}")
            print(f"Rain Detected: {sensor_data['rain_detected']}")
            print("------------------------")
        
    except KeyboardInterrupt:
        # Handle exit gracefully
        print("\nExiting the listener.")
        break
    except Exception as e:
        print(f"Error: {e}")
        break

# Close the serial connection when done
ser.close()
