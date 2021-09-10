from django.db import models
from django.utils import timezone

class Timecard(models.Model):
    site_code= models.CharField(max_length=200)
    contractor_name = models.CharField(max_length=200)
    hours = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Job_code_managment(models.Model):
    job_code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    max_hours = models.PositiveIntegerField()

class Machine_managment(models.Model):
    machine_code = models.CharField(max_length=200)
    machine_rate = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=200)

class Submit_Timecard(models.Model):
    site_code = models.CharField(max_length=200)
    contractor_name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    labor_code = models.ForeignKey(Job_code_managment, on_delete=models.CASCADE)
    hours_worked = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    machine_code = models.ForeignKey(Machine_managment, on_delete=models.CASCADE)
    hours_used = models.PositiveIntegerField()
    total_cost_m = models.DecimalField(max_digits=10, decimal_places=2)




