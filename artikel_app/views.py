from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def artikel_list(request):
    return render(request, 'artikel_app/artikel_list.html', {})

def artikel_tambah(request):
    return render(request, 'artikel_app/artikel_tambah.html', {})

def artikel_edit(request):
    pass
