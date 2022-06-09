from django.db import models

# Create your models here.
class weather(models.Model):
    url = models.CharField(max_length=1000)
    