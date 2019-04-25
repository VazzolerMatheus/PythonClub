from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)

    def __str__ (self):
        return self.title

    class Meta:
        db_table='meeting'
        verbose_name_plural = 'meetings'


class MeetingMinutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)
    attendance = models.CharField(max_length=255)
    minutesText = models.CharField(max_length=255)

    def __str__ (self):
        return self.meeting

    class Meta:
        db_table='MeetingMinutes'
        verbose_name_plural = 'MeetingMinutes'



class Resource(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255)
    resourceType = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    dateEntered = models.DateField()
    description = models.CharField(max_length=255)

    def __str__ (self):
        return self.name

    class Meta:
        db_table='Resource'
        verbose_name_plural = 'Resource'

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    user = models.ManyToManyField(User)
    
    def __str__ (self):
        return self.title

    class Meta:
        db_table='Event'
        verbose_name_plural = 'Events'
