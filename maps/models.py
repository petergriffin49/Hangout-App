from django.db import models

class Spot(models.Model):
    spot_name = models.CharField(max_length=64)
    spot_description = models.TextField(max_length=256)
    spot_latitude = models.FloatField(default=0)
    spot_longitude = models.FloatField(default=0)
    photo = models.ImageField(upload_to = "media/spotPhotos")

