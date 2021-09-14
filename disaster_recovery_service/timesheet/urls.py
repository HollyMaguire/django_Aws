from django.urls import path
from . import views

urlpatterns = [
    path("", views.ViewTimecard.as_view()),
    path("jobCodes/", views.ViewJobCode.as_view()),
    path("machines/", views.ViewMachines.as_view()),
    path("submitTimecard/", views.FillTimecard.as_view()),
    path('<int:timesheet_id>/', views.approve, name='approve'),
    # path('delete/<int:timesheet_id>/', views.delete, name='delete'),
    path('jobCode/delete/<int:jobcode_id>/', views.delete_jobcode, name='delete')
    # path('timesheet/view_timecard/', views.view_timecard, name='view_timecard'),
    # path('', views.index, name='index'),
]

from django.urls import path
from . import views

