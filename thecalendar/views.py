from django.shortcuts import render
from .models import Event

# Create your views here.
def calendar_detail(request):
    events = Event.objects.all()
    return render(request, 'thecalendar/base.html', {'events': events})
