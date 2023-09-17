from django.db import models
from django.utils import timezone
# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    Video_url= models.URLField()
    description= models.CharField(max_length=200)
    create_date = 
        