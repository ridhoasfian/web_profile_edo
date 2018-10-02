from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from .forms import TambahAnggaranForm, SubmitBiayaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def anggaran_list(request):
    anggaran_list = Anggaran.objects.all()
    anggaran_kosong=False
    if len(anggaran_list) == 0:
        anggaran_kosong=True

    #paginator
    paginator = Paginator(anggaran_list, 5) # batasi 5 data perhalaman
    page = request.GET.get('page')  # ambil nilai param url 'page'
    anggaran_list = paginator.get_page(page) # ambil data dari halaman

    #menggabung param url
    ambil_url = request.GET.copy() # ambil semua param url key dan val
    param_url = ambil_url.pop('page', True) and ambil_url.urlencode()

    return render(request, 'budget_app/anggaran_list.html', {'anggaran_list':anggaran_list, 'anggaran_kosong':anggaran_kosong})

def anggaran_detail(request, id_anggaran):
    anggaran = get_object_or_404(Anggaran, pk=id_anggaran)
    kategori_list = Kategori.objects.filter(anggaran=anggaran)
    biaya_list = anggaran.biaya_set.all().order_by('-id')
    return render(request, 'budget_app/anggaran_detail.html', {'anggaran':anggaran, 'biaya_list':biaya_list, 'kategori_list':kategori_list})

def tambah_anggaran(request):
    if request.method == "POST":
        form = TambahAnggaranForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            budget = form.cleaned_data['budget']
            new_anggaran = Anggaran.objects.create(nama=nama, budget=budget)
            new_anggaran.save()

            hasil_input_kategori = request.POST.get('hasil_input_kategori')
            split_hasil_input_kategori = hasil_input_kategori.split(',')
            for split_hasil_input_kategori in split_hasil_input_kategori:
                if split_hasil_input_kategori == '':
                    continue
                Kategori.objects.create(anggaran=new_anggaran, nama=split_hasil_input_kategori).save()
            return redirect('anggaran_list')
    else:
        form = TambahAnggaranForm()
    return render(request, 'budget_app/tambah_anggaran.html', {'tambah_anggaran':tambah_anggaran, 'form':form})

def submit_biaya(request, id_anggaran):
    anggaran = get_object_or_404(Anggaran, pk=id_anggaran)
    if request.method == "POST" :
        form = SubmitBiayaForm(request.POST)
        if form.is_valid():
            keperluan = form.cleaned_data['keperluan']
            amount = form.cleaned_data['amount']
            kategori = get_object_or_404(Kategori, anggaran=anggaran, nama=form.cleaned_data['kategori'])

            Biaya.objects.create(anggaran=anggaran, nama=keperluan, amount=amount, kategori=kategori).save()
            return redirect('anggaran_detail', id_anggaran)
    else:
        form = SubmitBiayaForm()
    return render(request, 'budget_app/submit_biaya.html', {'anggaran':anggaran, 'form':form})


def anggaran_hapus(request, id_anggaran):
    get_object_or_404(Anggaran, pk=id_anggaran).delete()
    return redirect('anggaran_list')


def biaya_hapus(request, id_anggaran, id_biaya):
    anggaran = get_object_or_404(Anggaran, pk=id_anggaran)
    biaya = get_object_or_404(Biaya, anggaran=anggaran, id=id_biaya)
    biaya.delete()
    return redirect('anggaran_detail', id_anggaran)










#
