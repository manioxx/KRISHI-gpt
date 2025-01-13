from django.db import models

class SensorData(models.Model):
    soil_moisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_quality = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Sensor Data {self.timestamp}"
