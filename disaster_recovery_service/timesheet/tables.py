import django_tables2 as tables
from .models import Timecard, Job_code_managment, Machine_managment

class TimecardTable(tables.Table):
    class Meta:
        model = Timecard
        template_name = "django_tables2/bootstrap.html"
        fields = ("site_code", "contractor_name", "hours", "amount" )


class JobCodeTable(tables.Table):
    class Meta:
        model = Job_code_managment
        template_name = "django_tables2/bootstrap.html"
        fields = ("job_code", "description", "hourly_rate", "max_hours")


class MachineTable(tables.Table):
    class Meta:
        model = Machine_managment
        template_name = "django_tables2/bootstrap.html"
        fields = ("machine_code", "machine_rate", "details")
