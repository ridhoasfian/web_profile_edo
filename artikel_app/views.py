from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .models import *
import datetime

# Create your views here.
def artikel_list(request):
    artikel = Artikel.objects.all()
    kategori = Kategori.objects.all()

    if 'kategori' in request.GET:
        ambil_param_url = request.GET.get('kategori', '') # ambil nilai param url 'Kategori'
        object_kategori = get_object_or_404(Kategori, nama=ambil_param_url)
        artikel = object_kategori.artikel_set.all()

    #paginator
    paginator = Paginator(artikel, 5) # batasi 5 data perhalaman
    page = request.GET.get('page')  # ambil nilai param url 'page'
    artikel = paginator.get_page(page) # ambil data dari halaman

    #menggabung param url
    ambil_url = request.GET.copy() # ambil semua param url key dan val
    param_url = ambil_url.pop('page', True) and ambil_url.urlencode()

    return render(request, 'artikel_app/artikel_list.html', {'artikel':artikel, 'kategori':kategori, 'param_url':param_url})


def artikel_tambah(request):
    if request.method == "POST":
        form = ArtikelTambahForm(request.POST, request.FILES)
        if form.is_valid():
            new_artikel = form.save(commit=False)
            new_artikel.pub_date = datetime.datetime.now()
            new_artikel.edit_date = datetime.datetime.now()
            new_artikel.save()
            form.save_m2m()
            messages.success(request, 'berhasil menambahkan Artikel !', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('artikel_list')
    else:
        form = ArtikelTambahForm()
    return render(request, 'artikel_app/artikel_tambah.html', {'form':form})


def artikel_edit(request, id_artikel):
    artikel = get_object_or_404(Artikel, pk=id_artikel)
    if request.method == "POST":
        artikel.foto_sampul.delete()  # hapus fisik foto
        form = ArtikelEditForm(request.POST, request.FILES, instance=artikel)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.edit_date = datetime.datetime.now()
            edit.save()
            form.save_m2m()
            messages.success(request, 'berhasil menyunting Artikel !', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('artikel_detail', id_artikel)
    else:
        form = ArtikelEditForm(instance=artikel)
    return render(request, 'artikel_app/artikel_edit.html', {'form':form})


def artikel_detail(request, id_artikel):
    artikel = get_object_or_404(Artikel, pk=id_artikel)
    kategori = Kategori.objects.all()
    return render(request, 'artikel_app/artikel_detail.html', {'artikel':artikel, 'kategori':kategori})


def artikel_delete(request, id_artikel):
    artikel = get_object_or_404(Artikel, pk=id_artikel)
    artikel.foto_sampul.delete()  # hapus fisik foto
    artikel.delete()
    messages.success(request, 'berhasil menghapus Artikel !', extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('artikel_list')


def kategori_list(request, id_kategori):
    return render(request, 'artikel_app/kategori_list.html', {})


def kategori_edit(request, id_kategori):
    return render(request, 'artikel_app/kategori_edit.html', {})

def kategori_delete(request, id_kategori):
    kategori = get_object_or_404(Kategori, pk=id_kategori)
    kategori.delete()
    messages.success(request, 'berhasil menghapus Data Kategori !', extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('kategori_list')
















    #
