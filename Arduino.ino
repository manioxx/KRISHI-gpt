#include <DHT.h>

// Pin definitions
#define DHTPIN 2         // Pin connected to DHT sensor
#define DHTTYPE DHT11    // DHT 11
#define PH_ANALOG_PIN A0 // Analog signal from pH sensor
#define PH_TEMP_PIN A1   // Analog pin for temperature compensation, if available
#define LDR_PIN A2       // LDR sensor pin
#define MOISTURE_PIN A3  // Moisture sensor pin
#define RAIN_PIN A4      // Rain sensor pin (analog)

// Initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  dht.begin();
  pinMode(PH_ANALOG_PIN, INPUT);
  pinMode(LDR_PIN, INPUT);
  pinMode(MOISTURE_PIN, INPUT);
  pinMode(RAIN_PIN, INPUT); // Initialize rain sensor pin as input
}

void loop() {
  // Read temperature and humidity
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Check if reads are valid
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("{\"error\": \"Failed to read from DHT sensor!\"}");
    delay(1000);
    return;
  }

  // Read pH value (assume analog input)
  int phRawValue = analogRead(PH_ANALOG_PIN);
  float voltage = (phRawValue / 1024.0) * 3.3; // Convert to voltage (for 5V ADC reference)
  float pHValue = 3.5 * voltage + 0.8;         // Example calibration equation for pH sensor

  // Optional: Read temperature from pH sensor if available
  int tempRawValue = analogRead(PH_TEMP_PIN);
  float phTempVoltage = (tempRawValue / 1024.0) * 5.0;
  float sensorTemp = phTempVoltage * 100;      // Convert to temperature if needed (adjust scaling)

  // Read LDR value
  int ldrValue = analogRead(LDR_PIN);

  // Read Moisture value
  int moistureValue = analogRead(MOISTURE_PIN);

  // Read Rain sensor value
  int rainValue = analogRead(RAIN_PIN);

  // Send data as JSON
  String sensor_data = "{\"temperature\": " + String(temperature) +
                       ", \"humidity\": " + String(humidity) +
                       ", \"pH\": " + String(pHValue) +
                       ", \"ldr\": " + String(ldrValue) +
                       ", \"moisture\": " + String(moistureValue) +
                       ", \"rain\": " + String(rainValue) +
                       "}";
  Serial.println(sensor_data);

  delay(1000);  // Wait for 1 second before sending data again
}
