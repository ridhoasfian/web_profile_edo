from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.
def polling_list(request):
    poll = Poll.objects.all()
    return render(request, 'polling_app/polling_list.html', {})

@login_required
def polling_tambah(request):
    if request.method == "POST":
        form = PollingTambahForm(request.POST)
        if form.is_valid():
    else:
        form = PollingTambahForm()
    return render(request, 'polling_app/polling_tambah.html', {'form':form})

@login_required
def polling_detail(request, id_polling):
    pass
