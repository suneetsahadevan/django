from django.urls import path
from . import views

urlpatterns = [
    path('thecalendar/', views.calendar_detail, name='calendar_detail'),
]
