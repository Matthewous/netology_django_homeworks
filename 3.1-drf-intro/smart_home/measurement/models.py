from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max=50)
    description = models.TextField()

class Measurement(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField()
    