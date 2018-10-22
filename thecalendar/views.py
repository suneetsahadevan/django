from django.shortcuts import render
from .models import Event
import datetime , calendar

# Create your views here.
def calendar_detail(request):
    now = datetime.datetime.now()
    numberofdays = calendar.monthrange(now.year, now.month)[1]
    currentmonthname = calendar.month_name[now.month]
    currentyear = now.year
    currentday = now.day
    startdayofmonth = calendar.day_name[datetime.datetime(now.year,now.month,1).weekday()]
    monthdays = []
    for i in range(numberofdays):
        monthdays.append(i+1)
    events = Event.objects.all()
    return render(request, 'thecalendar/base.html', {'monthdays': monthdays , 'currentmonthname': currentmonthname ,'currentyear' : currentyear , 'currentday' : currentday , 'startdayofmonth': startdayofmonth})
