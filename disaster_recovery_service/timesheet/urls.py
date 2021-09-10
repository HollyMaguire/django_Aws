from django.urls import path
from . import views

urlpatterns = [
    path("", views.ViewTimecard.as_view()),
    path("jobCodes/", views.ViewJobCode.as_view()),
    path("machines/", views.ViewMachines.as_view()),
    path("submitTimecard/", views.FillTimecard.as_view())

    # path('timesheet/view_timecard/', views.view_timecard, name='view_timecard'),
    # path('', views.index, name='index'),
]