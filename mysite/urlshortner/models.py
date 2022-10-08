from django.db import models
from django.utils import timezone
# Create your models here.

class urlmodels(models.Model):
    longurl = models.CharField(max_length=100)
    shorturl = models.CharField(max_length=15)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.shorturl