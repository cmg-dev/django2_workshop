from django.db import models
from django.utils import timezone

class Geburtstage(models.Model):
    geburtstag = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30)

# Create your models here.
