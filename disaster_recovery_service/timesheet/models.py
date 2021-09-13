from django.db import models
from django.utils import timezone

class Timecard(models.Model):
    site_code = models.CharField(max_length=200)
    contractor_name = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def total_hours(self):
        total_hours = 0
        for i in Timecard_Job_code_managment.objects.filter(time_card_id=self.id):
            total_hours = total_hours + i.hours_worked
        return total_hours

    def total_cost(self):
        total_cost = 0
        for i in Timecard_Job_code_managment.objects.filter(time_card_id=self.id):
            total_cost = total_cost + i.hours_worked * Job_code_managment.objects.filter(id=i.job_code_managment.id).last().hourly_rate
        for i in Timecard_Machine_managment.objects.filter(time_card_id=self.id):
            total_cost = total_cost + i.hours_worked * Job_code_managment.objects.filter(id=i.job_code_managment.id).last().machine_rate
        return total_cost


    def __str__(self):
        return '{self.site_code}, {self.contractor_name}'.format(self=self)


class Job_code_managment(models.Model):
    job_code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    max_hours = models.PositiveIntegerField()
    time_card = models.ManyToManyField(Timecard, through="Timecard_Job_code_managment")

    def __str__(self):
        return '{self.description}'.format(self=self)

class Machine_managment(models.Model):
    machine_code = models.CharField(max_length=200)
    machine_rate = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=200)
    time_card = models.ManyToManyField(Timecard, through="Timecard_Machine_managment")

class Timecard_Job_code_managment(models.Model):
    time_card = models.ForeignKey(Timecard, on_delete=models.CASCADE)
    job_code_managment = models.ForeignKey(Job_code_managment, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)

class Timecard_Machine_managment(models.Model):
    time_card = models.ForeignKey(Timecard, on_delete=models.CASCADE)
    Machine_managment = models.ForeignKey(Machine_managment, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)


class Submit_Timecard(models.Model):
    site_code = models.CharField(max_length=200)
    contractor_name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    labor_code = models.ForeignKey(Job_code_managment, on_delete=models.CASCADE)
    # hours_worked = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    machine_code = models.ForeignKey(Machine_managment, on_delete=models.CASCADE)
    hours_used = models.PositiveIntegerField()
    total_cost_m = models.DecimalField(max_digits=10, decimal_places=2)




