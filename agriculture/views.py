from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt
import serial
import json
import time
from .utils.data_analysis import analyze_plant_health  # Import the analysis function

# Function to fetch data from Arduino
def get_arduino_data():
    try:
        print("Attempting to connect to Arduino...")
        # Open serial connection to the Arduino (ensure the port is correct)
        arduino = serial.Serial('COM3', 9600, timeout=5)  # Increased timeout
        time.sleep(2)  # Allow time for Arduino to start sending data
        print("Connected to Arduino successfully.")
        
        data = arduino.readline()  # Read data from Arduino
        print(f"Raw data received: {data}")
        
          # Close the connection after reading

        if data:
            try:
                sensor_data = json.loads(data.decode('utf-8'))  # Decode and convert to JSON
                print(f"Decoded sensor data: {sensor_data}")
                return sensor_data
            except json.JSONDecodeError:
                print("Error decoding JSON data.")
                return {}
        else:
            raise ValueError("No data received from Arduino")
    except Exception as e:
        print(f"Error reading from Arduino: {e}")
        return {}

@csrf_exempt
def process_and_analyze(request):
    """
    This view fetches data from Arduino, processes it, and returns the data as JSON.
    """
    try:
        # Fetch the sensor data from Arduino
        sensor_data = get_arduino_data()

        if sensor_data:
            # Analyze the sensor data using the analysis function
            result = analyze_plant_health(sensor_data)

            # Return the sensor data and analysis result as JSON
            return JsonResponse({
                "sensor_data": sensor_data,
                "analysis_result": result,
            })
        else:
            return JsonResponse({"error": "No data from Arduino"}, status=500)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def plant_health_view(request):
    """
    Fetches data from Arduino, analyzes it, and displays it on the webpage.
    """
    # Fetch the sensor data from Arduino
    sensor_data = get_arduino_data()

    # Analyze the data if available
    if sensor_data:
        analysis_result = analyze_plant_health(sensor_data)
    else:
        sensor_data = {}
        analysis_result = {
            "health_status": "Unknown",
            "health_probability": 0,
            "suggestions": ["No data available"],
            "best_time_to_water": "N/A",
            "error": "No sensor data available",
        }

    # Render the template with sensor data and analysis result
    return render(request, 'dashboard.html', {
        'sensor_data': sensor_data,
        'result': analysis_result,
    })

def display_data(request):
    """
    Fetches data from Arduino, analyzes it, and displays it on the webpage.
    """
    sensor_data = get_arduino_data()

    # Analyze the data if available
    if sensor_data:
        analysis_result = analyze_plant_health(sensor_data)
    else:
        sensor_data = {}
        analysis_result = {
            "health_status": "Unknown",
            "health_probability": 0,
            "suggestions": ["No data available"],
            "best_time_to_water": "N/A",
            "error": "No sensor data available",
        }

    return render(request, 'dashboard.html', {
        'sensor_data': sensor_data,
        'result': analysis_result,
    })

def home(request):
    return render(request, 'dashboard.html')
def send_to_arduino(request):
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=5)
    time.sleep(2)
    if request.method == 'POST':
        # Send fixed data to Arduino when the button is pressed
        arduino.write(b'button_pressed')  
        return JsonResponse({'status': 'success', 'message': 'Data sent to Arduino'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def api_temperature(request):
    sensor_data = get_arduino_data()
    if sensor_data:
        temperature = sensor_data.get("temperature", None)  # Assuming "temperature" key exists in your data
        if temperature is not None:
            return JsonResponse({'temperature': temperature})
    return JsonResponse({'error': 'No temperature data available'}, status=500)