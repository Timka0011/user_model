from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    number = models.CharField(max_length = 24, null = True, blank = True)



