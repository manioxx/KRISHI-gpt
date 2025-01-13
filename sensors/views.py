from django.shortcuts import render

def dashboard(request):
    # Replace with your logic to fetch and display data
    data = {
        'sensor_data': {
            'temperature': 28.5,
            'humidity': 65.0,
            'soil_moisture': 45.0,
            'ldr_value': 350,
            'pH': 6.2,
            'rain_detected': False,
        },
        'ai_analysis': {
            'health_status': "Healthy",
            'health_probability': 95,
            'suggestions': ["Ensure proper sunlight", "Water early in the morning"],
            'best_time_to_water': "07:30",
        }
    }
    return render(request, 'agriculture/templates/dashboard.html', data)


def plant_health(request):
    # Replace this with logic to fetch plant health data
    data = {
        'health_status': "Healthy",
        'probability': 92,
        'recommendations': ["Water the plant in the morning", "Add nitrogen fertilizer"],
    }
    return render(request, 'sensors/plant_health.html', data)

