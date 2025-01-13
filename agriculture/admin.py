from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity', 'ai_insight')
    list_filter = ('timestamp',)
    def ai_insight(self, obj):
        # Define a method to return the value for the ai_insight field
        return obj.some_related_field_or_method()  # Replace with your actual logic
    ai_insight.short_description = 'AI Insight'  # Optional: gives a custom column name in the admin
