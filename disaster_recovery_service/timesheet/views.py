from django.shortcuts import render

from django.http import HttpResponse

def view_timecard(request):
    return render(request, 'timesheet/view_timecard.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
