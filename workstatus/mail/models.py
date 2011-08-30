from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    #user = models.ForeignKey(User)
    user = models.CharField(max_length = 200)
    name = models.CharField(max_length =200)
    progress = models.IntegerField()