from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class urlmodels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    longurl = models.CharField(max_length=100)
    shorturl = models.CharField(max_length=15)
    count = models.IntegerField(default=0)
    #added=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.shorturl