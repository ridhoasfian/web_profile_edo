from django.shortcuts import render

# Create your views here.
def calendar_index(request):
    return render(request, 'calendar_app/calendar_index.html', {})
