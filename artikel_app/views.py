from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ArtikelTambahForm

# Create your views here.
def artikel_list(request):
    return render(request, 'artikel_app/artikel_list.html', {})

def artikel_tambah(request):
    if request.method == "POST":
        pass
        # form = ArtikelTambahForm(request.POST)
        # if form.is_valid():
        #
    else:
        form = ArtikelTambahForm()
    return render(request, 'artikel_app/artikel_tambah.html', {'form':form})

def artikel_edit(request):
    pass
