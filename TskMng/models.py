from django.db import models
from django.utils import timezone

class Task(models.Model):
    task_author = models.ForeignKey('auth.User')
    task_name = models.CharField(max_length = 200)
    task_description = models.TextField()
    task_open = models.DateTimeField(default=timezone.now)
    task_closed = models.DateTimeField(blank=True, null=True)
    task_in_process = models.DateTimeField(blank=True, null=True)
    task_progress = models.ForeignKey('Progress' , editable = 'false')
    task_prioritet = models.ForeignKey('Prioritet', editable = 'false')
    task_class = models.ForeignKey('Clases', editable = 'false')

    def publish(self):
        self.save()

    def __str__(self):
        return self.task_name
# Create your models here.
class Progress(models.Model):
    flag = models.CharField(max_length = 200, editable = 'false')

    def publish(self):
        self.save()

    def __str__(self):
        return self.flag

class Prioritet(models.Model):
    prioritet = models.CharField(max_length=200, editable='false')

    def publish(self):
        self.save()

    def __str__(self):
        return self.prioritet
class Clases(models.Model):
    clases = models.CharField(max_length=200, editable='false')

    def publish(self):
        self.save()

    def __str__(self):
        return self.clases