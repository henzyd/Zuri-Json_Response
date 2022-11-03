from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass



class EnumModel(models.Model):
    operation_type = models.CharField(default=0, max_length=20)
    x = models.IntegerField()
    y = models.IntegerField()