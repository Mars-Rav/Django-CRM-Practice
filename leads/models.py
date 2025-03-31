from django.db import models
from agents.models import Agent


class Lead(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
