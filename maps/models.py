from django.db import models

class Spot(models.Model):
    spot_name = models.CharField(max_length=64)
    spot_description = models.CharField(max_length=256)
    spot_latitude = models.IntegerField(default=0)
    spot_longitude = models.IntegerField(default=0)

