import os
from openai import AzureOpenAI
import json

# Azure OpenAI Configuration
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "https://savyachatgpt.openai.azure.com/"),
    api_key=os.getenv("AZURE_OPENAI_KEY", "6ee47602387643609a0c3a24cf46b520"),
    api_version="2024-05-01-preview"
)

def analyze_plant_health(sensor_data):
    """
    Analyze plant health using Azure OpenAI based on sensor data
    
    :param sensor_data: Dictionary containing sensor measurements
    :return: Processed plant health analysis
    """
    try:
        # Prepare the system message and user prompt
        system_message = {
            "role": "system",
            "content": """You are an AI assistant designed to analyze sensor data for smart agriculture. 
            Provide a detailed analysis of plant health based on sensor readings.
            
            You must respond with a JSON object containing the following fields:
            {
                "health_status": "String indicating plant health status",
                "health_probability": "Number between 0-100",
                "suggestions": ["Array of actionable suggestions"],
                "best_time_to_water": "Time in HH:MM format"
            }"""
        }
        
        user_message = {
            "role": "user", 
            "content": f"Analyze the following sensor data and respond with a JSON object: {json.dumps(sensor_data)}"
        }

        # Call Azure OpenAI API
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_MODEL", "gpt-4o"),
            messages=[system_message, user_message],
            temperature=float(os.getenv("AZURE_OPENAI_TEMPERATURE", 0)),
            max_tokens=int(os.getenv("AZURE_OPENAI_MAX_TOKENS", 4000)),
            response_format={"type": "json_object"}
        )

        # Extract and parse the response
        analysis = response.choices[0].message.content
        return json.loads(analysis)

    except Exception as e:
        return {
            "error": str(e),
            "health_status": "Analysis Failed",
            "health_probability": 0,
            "suggestions": ["Check sensor connections", "Retry analysis"],
            "best_time_to_water": "N/A"
        }

# Example usage
def main():
    # Sample sensor data
    sensor_data = {
        'temperature': 28.5,
        'humidity': 65.0,
        'soil_moisture': 45.0,
        'ldr_value': 350,
        'pH': 6.2,
        'rain_detected': False
    }

    # Analyze plant health
    result = analyze_plant_health(sensor_data)
    
    # Extract variables from the result
    health_status = result.get('health_status', 'Unknown')
    health_probability = result.get('health_probability', 0)
    suggestions = result.get('suggestions', [])
    best_time_to_water = result.get('best_time_to_water', 'N/A')

    # Print the results in a formatted way
    print("🌱 Plant Health Analysis Report 🌱")
    print("=" * 40)
    print(f"Health Status: {health_status}")
    print(f"Health Probability: {health_probability}%")
    
    print("\nSuggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")
    
    print("\nWatering Recommendation:")
    print(f"Best Time to Water: {best_time_to_water}")

    # Optional: Error handling
    if 'error' in result:
        print("\n⚠️ Error Details:")
        print(result['error'])

if __name__ == "__main__":
    main()