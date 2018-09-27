from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def testing(request):
    return render(request, 'schedule_app/testing.html',{})


def schedule_list(request):
    schedule = Schedule.objects.all()
    return render(request, 'schedule_app/schedule_list.html', {'schedule':schedule})

def schedule_detail(request, id_schedule):
    schedule = get_object_or_404(Schedule, pk=id_schedule)
    return render(request, 'schedule_app/schedule_detail.html', {'schedule':schedule})

def schedule_delete(request, id_schedule):
    schedule = get_object_or_404(Schedule, pk=id_schedule)
    schedule.delete()
    return redirect('schedule_list')

def schedule_tambah(request):
    if request.method == "POST":
        form = ScheduleTambahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleTambahForm()
    return render(request, 'schedule_app/schedule_tambah.html', {'form':form})












#
