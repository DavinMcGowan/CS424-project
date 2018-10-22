from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False,auto_now_add=False)