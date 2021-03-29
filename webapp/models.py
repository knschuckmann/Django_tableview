from django.db import models

    
class Webapp(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    temperature = models.IntegerField()
    duration = models.DurationField()