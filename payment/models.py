from django.db import models
from django.utils.translation import gettext_lazy as _

from car.models import Car, PositionCategory


class Credit(models.Model):
    CHOICE = (
        (1, _('Credit',)),
        (2, _('Leasing',))
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='credits')
    model = models.ForeignKey(PositionCategory, on_delete=models.CASCADE, related_name='credits')
    month = models.IntegerField(default=12)
    status = models.IntegerField(choices=CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.month)

    @property
    def model_title(self):
        return self.model.title


class Payment(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='payments')
    order = models.IntegerField(default=1)
    sum = models.FloatField(default=0)
    percent = models.FloatField(default=12)
    total = models.FloatField(default=0)
    remain = models.FloatField(default=0)

    def __str__(self):
        return str(self.order)

