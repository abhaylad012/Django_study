from django.db import models

# Create your models here.
class List(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
