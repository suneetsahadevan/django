from django.shortcuts import render
from .models import Event
import datetime , calendar

# Create your views here.
def calendar_detail(request):
    now = datetime.datetime.now()
    numberofdays = calendar.monthrange(now.year, now.month)[1]
    monthname = calendar.month_name[now.month]
    year = now.year
    monthdays = []
    for i in range(numberofdays):
        monthdays.append(i+1)
    events = Event.objects.all()
    return render(request, 'thecalendar/base.html', {'monthdays': monthdays , 'monthname': monthname ,'year' : year})
