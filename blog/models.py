from django.db import models

# Create your models here.

class post(models.Model):
    title=models.CharField(max_leght=250)
    content=models.TextField()