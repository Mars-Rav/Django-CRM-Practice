from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Agent(models.Model):
    agent = models.OneToOneField(User, on_delete=models.CASCADE)