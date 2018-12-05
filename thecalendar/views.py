from django.shortcuts import render
from .models import Event
import datetime , calendar
from .forms import Get_year_month

# Create your views here.
def calendar_detail(request):
    if request.method == "POST":
        form = Get_year_month(request.POST)
        if form.is_valid():
            input_year = form.split('-')[0]
            input_month = form.split('-')[1]
            numberofdays = calendar.monthrange(input_year, input_month)[1]
            currentmonthname = calendar.month_name[input_month]
            startdayofmonth = calendar.day_name[datetime.datetime(input_year,input_month,1).weekday()]
            startdaynumber = datetime.datetime(input_year,input_month,1).weekday()
            enddaynumber = datetime.datetime(input_year,input_month,numberofdays).weekday()
            enddays = 6 - enddaynumber
            startblanks = []
            endblanks = []
            i = 0
            for i in range(startdaynumber):
                startblanks.append(i)

            monthdays = []
            i = 0
            for i in range(numberofdays):
                monthdays.append(i+1)
            i = 1
            for i in range(6 - enddaynumber):
                endblanks.append(i)
            events = Event.objects.all()
            return render(request, 'thecalendar/base.html', {'monthdays': monthdays , 'currentmonthname': currentmonthname ,'currentyear' : currentyear , 'currentday' : currentday , 'startdayofmonth': startdayofmonth , 'startblanks' : startblanks , 'endblanks' : endblanks , 'form': form})
    else:
        now = datetime.datetime.now()
        numberofdays = calendar.monthrange(now.year, now.month)[1]
        currentmonthname = calendar.month_name[now.month]
        currentyear = now.year
        currentday = now.day
        startdayofmonth = calendar.day_name[datetime.datetime(now.year,now.month,1).weekday()]
        startdaynumber = datetime.datetime(now.year,now.month,1).weekday()
        enddaynumber = datetime.datetime(now.year,now.month,numberofdays).weekday()
        enddays = 6 - enddaynumber
        startblanks = []
        endblanks = []
        i = 0
        for i in range(startdaynumber):
            startblanks.append(i)

        monthdays = []
        i = 0
        for i in range(numberofdays):
            monthdays.append(i+1)
        i = 1
        for i in range(6 - enddaynumber):
            endblanks.append(i)
        events = Event.objects.all()
        form = Get_year_month(request.POST)
        return render(request, 'thecalendar/base.html', {'monthdays': monthdays , 'currentmonthname': currentmonthname ,'currentyear' : currentyear , 'currentday' : currentday , 'startdayofmonth': startdayofmonth , 'startblanks' : startblanks , 'endblanks' : endblanks, 'form': form})
