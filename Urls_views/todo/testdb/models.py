from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    mobile_no = models.IntegerField()

    # def __str__(self):
    #     return self


