# import django_tables2 as tables
from django_tables2 import SingleTableView, Table
from .models import Timecard, Job_code_managment, Machine_managment

class TimecardTable(Table):
    class Meta:
        model = Timecard
        template_name = "django_tables2/bootstrap.html"
        fields = ( "contractor_name","site_code", "total_hours", "total_cost")

class JobCodeTable(Table):
    class Meta:
        model = Job_code_managment
        template_name = "django_tables2/bootstrap.html"
        fields = ("job_code", "description", "hourly_rate", "max_hours")


class MachineTable(Table):
    class Meta:
        model = Machine_managment
        template_name = "django_tables2/bootstrap.html"
        fields = ("machine_code", "machine_rate", "details")