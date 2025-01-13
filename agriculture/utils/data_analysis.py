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
                "best_time_to_water": "Time in HH:MM format with day or night",
                "next_steps": "What the user should do next",
                "error": "Any error that occurred in simple language",
                "irrigation_advice": "How often the plant should be watered",
                "pest_or_disease_warning": "Any pest or disease risks",
                "suitable_plants_or_seeds": "Suggest suitable plants or seeds for the given conditions",
                "growth_stage": "Current growth stage of the plant (e.g., vegetative, flowering)",
                "nutrient_deficiency": "Any nutrient deficiencies if applicable",
                "climate_impact": "How the current climate may affect the plant",
                "location": "Suggested location for the plant (e.g., tropical, temperate)",
                "leaf_temperature": "Leaf temperature (if available)",
                "CO2_levels": "CO2 levels (if available)"
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
            "best_time_to_water": "N/A",
            "next_steps": "Check the system and ensure all connections are working correctly",
            "irrigation_advice": "N/A",
            "pest_or_disease_warning": "N/A",
            "suitable_plants_or_seeds": "N/A",
            "growth_stage": "Unknown",
            "nutrient_deficiency": "Unknown",
            "climate_impact": "Unknown",
            "location": "Unknown",
            "leaf_temperature": "N/A",
            "CO2_levels": "N/A"
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
    next_steps = result.get('next_steps', 'N/A')
    irrigation_advice = result.get('irrigation_advice', 'N/A')
    pest_or_disease_warning = result.get('pest_or_disease_warning', 'None')
    suitable_plants_or_seeds = result.get('suitable_plants_or_seeds', 'N/A')
    growth_stage = result.get('growth_stage', 'Unknown')
    nutrient_deficiency = result.get('nutrient_deficiency', 'Unknown')
    climate_impact = result.get('climate_impact', 'Unknown')
    location = result.get('location', 'Unknown')
    leaf_temperature = result.get('leaf_temperature', 'N/A')
    co2_levels = result.get('CO2_levels', 'N/A')

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
    
    print("\nNext Steps:")
    print(next_steps)

    print("\nIrrigation Advice:")
    print(irrigation_advice)
    
    print("\nPest or Disease Warning:")
    print(pest_or_disease_warning)

    print("\nSuitable Plants or Seeds:")
    print(suitable_plants_or_seeds)

    print("\nGrowth Stage:")
    print(growth_stage)
    
    print("\nNutrient Deficiency:")
    print(nutrient_deficiency)
    
    print("\nClimate Impact:")
    print(climate_impact)
    
    print("\nLocation for Planting:")
    print(location)
    
    print("\nLeaf Temperature:")
    print(leaf_temperature)
    
    print("\nCO2 Levels:")
    print(co2_levels)

    # Optional: Error handling
    if 'error' in result:
        print("\n⚠️ Error Details:")
        print(result['error'])

if __name__ == "__main__":
    main()
