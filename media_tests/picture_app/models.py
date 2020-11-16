from django.db import models


class Cars(models.Model):
    model = models.CharField(blank=False, max_length=20)
    age = models.PositiveIntegerField(blank=False)
    price = models.FloatField(blank=False)
    image = models.ImageField(blank=False, upload_to='cars')
