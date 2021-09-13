from django.shortcuts import render
from django.urls import reverse_lazy

from.models import Timecard, Job_code_managment, Machine_managment, Submit_Timecard
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from .tables import TimecardTable, JobCodeTable, MachineTable
from django_tables2 import SingleTableView
from .forms import CreateTimeCardForm

class ViewTimecard(ListView):
    model = Timecard
    time_cards = Timecard.objects.all()
    template_name = 'timesheet/timecard.html'


class TimecardTable(SingleTableView):
    model = Timecard
    time_cards = Timecard.objects.all()
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
    model = Timecard
    form_class = CreateTimeCardForm
    template_name = 'timesheet/timesheetSubmit.html'
    success_url = reverse_lazy("index")


# class LaborEntry(CreateView):
#     model = Submit_Timecard
#     template_name = 'timesheet/timesheetSubmit.html'
#     fields = ('labor_code', 'hours_worked', 'total_cost',)

# class FillTimecard(CreateView): #createTimecard
#     model = Submit_Timecard
#     template_name = 'timesheet/timesheetSubmit.html'
#     fields = ('machine_code', 'hours_used', 'total_cost',)
