from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
# Create your views here.
def artikel_list(request):
    pass

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
