from django.db import models

class Timecard(models.Model):
    site_code= models.CharField(max_length=200)
    contractor_name = models.CharField(max_length=200)
    hours = models.PositiveIntegerField()
    amount= models.DecimalField(max_digits=10, decimal_places=2)

class Job_code_managment(models.Model):
    job_code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    max_hours = models.PositiveIntegerField()

class Machine_managment(models.Model):
    machine_code = models.CharField(max_length=200)
    machine_rate = models.DecimalField(max_digits=10, decimal_places=2)
