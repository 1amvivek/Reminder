from django.db import models
from django import forms
from django.utils import timezone


class Task(models.Model):
    summary = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    created = models.DateTimeField(default=timezone.now())
    reminder = models.DateTimeField()
    TL = models.ForeignKey('TaskList')

    def get_time_diff(self):
        if self.reminder:
            if timezone.now() > self.reminder:
                string = 'Already reminded'
            else:
                timediff = self.reminder - timezone.now()
                string = str(timediff)
                if string.__contains__('.'):
                    string = string[0:string.index('.')]
                    hours = string[0: string.index(':')]
                    mid = string[string.index(':')+1:]
                    minutes = mid[0: mid.index(':')]
                    string = '%s hours, %s minutes ' %(hours, minutes)
            return string

    def __str__(self):
        return self.summary


class TaskList(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)


