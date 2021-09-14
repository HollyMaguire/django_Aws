# import django_tables2 as tables
from django_tables2 import SingleTableView, Table
from .models import Timecard, Job_code_managment, Machine_managment
from django_tables2 import SingleTableView, Table, TemplateColumn, LinkColumn
from .models import Timecard, Job_code_managment, Machine_managment
from django_tables2.utils import A

class TimecardTableAdmin(Table):
    update = TemplateColumn(
        '<form action="/timesheet/{{record.id}}/" method="put">{% csrf_token %}<input type="hidden" name="_method" value="put"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">approve</button></form>',
        orderable=False,
        verbose_name=''
    )
    class Meta:
        model = Timecard
        template_name = "django_tables2/bootstrap.html"
        fields = ("contractor_name", "site_code", "total_hours", "total_cost", "approved")
        # delete = LinkColumn('main:delete_item', args=[A('pk')], attrs={
        #     'a': {'class': 'btn'}
        # })

class TimecardTable(Table):
    class Meta:
        model = Timecard
        template_name = "django_tables2/bootstrap.html"
        fields = ("contractor_name", "site_code", "total_hours", "total_cost", "approved")
        # delete = LinkColumn('main:delete_item', args=[A('pk')], attrs={
        #     'a': {'class': 'btn'}
        # })

class JobCodeTable(Table):
    class Meta:
        model = Job_code_managment
        template_name = "django_tables2/bootstrap.html"
        fields = ("job_code", "description", "hourly_rate", "max_hours")

    delete = TemplateColumn(
        '<form action="/jobCode/delete/{{record.id}}/" method="delete">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">delete</button></form>',
        orderable=False,
        verbose_name=''
    )

class MachineTable(Table):
    class Meta:
        model = Machine_managment
        template_name = "django_tables2/bootstrap.html"
        fields = ("machine_code", "machine_rate", "details")
