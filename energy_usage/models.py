from django.db import models
from django.contrib.auth import get_user_model


class Usage(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    electricity = models.FloatField(default=0)
    gas = models.FloatField(default=0)
    water = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)

    @property
    def total(self):
        return self.electricity + self.gas + self.water

