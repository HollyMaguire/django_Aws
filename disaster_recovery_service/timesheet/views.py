from django.shortcuts import render
from.models import Timecard, Job_code_managment, Machine_managment, Submit_Timecard
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from .tables import TimecardTable, JobCodeTable, MachineTable
from django_tables2 import SingleTableView

class ViewTimecard(ListView):
    model = Timecard
    template_name = 'timesheet/timecard.html'


class TimecardTable(SingleTableView):
    model = Timecard
    table_class = TimecardTable
    template_name = 'timesheet/timecard.html'

class ViewJobCode(ListView):
    model = Job_code_managment
    template_name = 'timesheet/JobCodeManagement.html'


class JobCodeTable(SingleTableView):
    model = Job_code_managment
    table_class = JobCodeTable
    template_name = 'timesheet/JobCodeManagement.html'

class ViewMachines(ListView):
    model = Machine_managment
    template_name = 'timesheet/machines.html'


class MachineTable(SingleTableView):
    model = Machine_managment
    table_class = MachineTable
    template_name = 'timesheet/machines.html'


class FillTimecard(CreateView):
    model = Submit_Timecard
    template_name = 'timesheet/timesheetSubmit.html'
    fields = ('site_code', 'contractor_name', 'date',)


    # labor_code = models.ForeignKey(Job_code_managment, on_delete=models.CASCADE)
    # hours_worked = models.PositiveIntegerField()
    # total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # machine_code = models.ForeignKey(Machine_managment, on_delete=models.CASCADE)
    # hours_used = models.PositiveIntegerField()
    # total_cost_m = models.DecimalField(max_digits=10, decimal_places=2)
