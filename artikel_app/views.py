from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
import datetime

# Create your views here.
def artikel_list(request):
    return render(request, 'artikel_app/artikel_list.html', {})

def artikel_tambah(request):
    if request.method == "POST":
        form = ArtikelTambahForm(request.POST)
        if form.is_valid():
            judul = form.cleaned_data['judul']
            isi = form.cleaned_data['isi']
            created_by = form.cleaned_data['created_by']
            sumber = form.cleaned_data['sumber']

            new_artikel = Artikel.objects.create(judul=judul, isi=isi, created_by=created_by, sumber=sumber, pub_date=datetime.datetime.now(), edit_date=datetime.datetime.now())
            new_artikel.save()

            new_kategori = Kategori.objects.create(artikel=new_artikel, nama='nama kategori')
            new_kategori.save()

            messages.success(request, 'berhasil menambahkan Artikel !', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('artikel_list')
    else:
        form = ArtikelTambahForm()
    return render(request, 'artikel_app/artikel_tambah.html', {'form':form})

def artikel_edit(request):
    pass
