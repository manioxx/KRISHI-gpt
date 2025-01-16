from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    pH = models.FloatField(null=True, blank=True)
    ldr = models.IntegerField(null=True, blank=True)
    moisture = models.IntegerField(null=True, blank=True)
    rain = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data at {self.timestamp}"