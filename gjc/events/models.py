from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False,auto_now_add=False)
    owner = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    
    
class CommitteeMember(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event,null=True,on_delete=models.CASCADE)