from django.db import models

# Create your models here.

class Event(models.Model):
    consultant = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    day = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    task_summary = models.CharField(max_length=200)
    task_description = models.TextField()

    def schedule(self):
        self.save()

    def __str__(self):
        return self.task_summary
