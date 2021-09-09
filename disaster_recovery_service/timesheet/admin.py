from django.contrib import admin
from .models import Job_code_managment
from .models import Timecard
from .models import Machine_managment

admin.site.register(Timecard)
admin.site.register(Job_code_managment)
admin.site.register(Machine_managment)