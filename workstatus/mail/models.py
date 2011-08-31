from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User)
    emailaddress = models.EmailFrield()
    content = models.CharField(max_length =200)
    time = models.CharField()