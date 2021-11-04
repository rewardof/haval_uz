from django.db import models
from car.models import Position


class Dealer(models.Model):
    title = models.CharField(max_length=255)
    position = models.ManyToManyField(Position, related_name='dealers')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    working_time = models.CharField(max_length=255)
    location_length = models.DecimalField(max_digits=10, decimal_places=5)
    location_width = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.title
