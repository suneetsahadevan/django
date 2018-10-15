from django.shortcuts import render

# Create your views here.
def calendar_detail(request):
    return render(request, 'thecalendar/base.html', {})
