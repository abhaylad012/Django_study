from django.db import models

# Create your models here.

class demo(models.Model):
    user_name = models.CharField(max_length=50)
    email = models