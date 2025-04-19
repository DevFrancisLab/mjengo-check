from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

class CheckInLog(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('in', 'Check In'),('out','Check Out')])

class IncidentReport(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateField(auto_now_add=True)