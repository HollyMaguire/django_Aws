from django.urls import path

from . import views

urlpatterns = [
    path('timesheet/view_timecard/', views.view_timecard, name='view_timecard'),
    # path('', views.index, name='index'),
]