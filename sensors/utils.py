import requests
import os

def analyze_sensor_data(sensor_data):
    endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
    api_key = os.getenv('AZURE_OPENAI_KEY')
    model = os.getenv('AZURE_OPENAI_MODEL')
    system_prompt = os.getenv('AZURE_OPENAI_SYSTEM_PROMPT')

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Sensor Data:\n"
                                         f"Humidity: {sensor_data.humidity}%\n"
                                         f"Soil Moisture: {sensor_data.soil_moisture}\n"
                                         f"Temperature: {sensor_data.temperature}°C\n"
                                         f"Air Quality: {sensor_data.air_quality}"}
        ],
        "max_tokens": 4000,
        "temperature": 0,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }

    response = requests.post(f"{endpoint}/openai/deployments/{model}/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"Azure OpenAI API Error: {response.status_code}, {response.text}")
