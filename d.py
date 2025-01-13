import serial
import time

def test_arduino():
    try:
        # Change 'COM5' to the correct port
        arduino = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)  # Wait for the connection to stabilize
        
        print("Connected to Arduino")
        
        while True:
            data = arduino.readline()  # Read data from Arduino
            if data:
                print(f"Raw data received: {data}")
                print(f"Decoded data: {data.decode('utf-8')}")
            else:
                print("No data received from Arduino.")
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

test_arduino()
