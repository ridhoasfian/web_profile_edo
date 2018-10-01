from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .forms import *
from .models import *
import datetime

# Create your views here.
def polling_list(request):
    poll = Poll.objects.all()

    if 'abjad' in request.GET:
        poll = poll.order_by('text')

    if 'pub_date' in request.GET:
        poll = poll.order_by('-pub_date')

    if 'peserta_voting' in request.GET:
        poll = poll.annotate(Count('vote')).order_by('-vote__count')


    #paginator
    paginator = Paginator(poll, 5) # batasi 5 data perhalaman
    page = request.GET.get('page')  # ambil nilai param url 'page'
    poll = paginator.get_page(page) # ambil data dari halaman

    #menggabung param url
    ambil_url = request.GET.copy() # ambil semua param url key dan val
    param_url = ambil_url.pop('page', True) and ambil_url.urlencode()

    return render(request, 'polling_app/polling_list.html', {'poll':poll, 'param_url':param_url})

@login_required
def polling_tambah(request):
    if request.method == "POST":
        form = PollingTambahForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            pub_date = datetime.datetime.now()
            choice1 = form.cleaned_data['choice1']
            choice2 = form.cleaned_data['choice2']

            new_poll = Poll.objects.create(owner=request.user, text=text, pub_date=pub_date)
            new_poll.save()

            new_choie1 = Choice.objects.create(poll=new_poll, text=choice1)
            new_choie1.save()
            new_choie2 = Choice.objects.create(poll=new_poll, text=choice2)
            new_choie2.save()
            return redirect('polling_list')
    else:
        form = PollingTambahForm()
    return render(request, 'polling_app/polling_tambah.html', {'form':form})


@login_required
def polling_detail(request, id_polling):
    poll = get_object_or_404(Poll, pk=id_polling)
    hasil = poll.get_hasil_voting()
    user_sudah_voting = poll.user_sudah_voting(request.user)
    return render(request, 'polling_app/polling_detail.html', {'poll':poll, 'hasil':hasil, 'user_sudah_voting':user_sudah_voting})


@login_required
def polling_hapus(request, id_polling):
    get_object_or_404(Poll, pk=id_polling).delete()
    messages.success(request, 'berhasil menghapus polling !', extra_tags='alert alert-danger alert-dismissible fade show')
    return redirect('polling_list')


@login_required
def polling_edit(request, id_polling):
    poll = get_object_or_404(Poll, pk=id_polling)
    if poll.owner != request.user:
        return redirect('polling_list')
    if request.method == "POST":
        pass
        form = PollingEditForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            messages.success(request, 'berhasil merubah polling !', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polling_list')
    else:
        form = PollingEditForm(instance=poll)

    return render(request, 'polling_app/polling_edit.html', {'poll':poll,'form':form})


@login_required
def choice_tambah(request, id_polling):
    poll = get_object_or_404(Poll, pk=id_polling)
    if poll.owner != request.user:
        return redirect('polling_list')
    if request.method == "POST":
        form = ChoiceTambahForm(request.POST)
        if form.is_valid():
            new_choice = Choice.objects.create(poll=poll, text=form.cleaned_data['text'])
            new_choice.save()
            messages.success(request, 'berhasil menambahkan choice pada polling ini', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polling_detail', id_polling)
    else:
        form = ChoiceTambahForm()
    return render(request, 'polling_app/choice_tambah.html', {'poll':poll,'form':form})

@login_required
def poll_vote(request, id_polling):
    poll = get_object_or_404(Poll, pk=id_polling)
    choice_id = request.POST.get('pilihan')

    if poll.user_sudah_voting(request.user):
        messages.error(request, 'Maaf, Anda sudah Voting di Polling ini !', extra_tags='alert alert-danger alert-dismissible fade show')
        return redirect('polling_detail', id_polling)

    if request.method == "POST":
        if choice_id:
            pilihan = Choice.objects.get(id=choice_id)
            new_vote = Vote(user=request.user, poll=poll, choice=pilihan)
            new_vote.save()
            messages.success(request, 'terimakasih telah berpartisipasi ;)', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polling_detail', id_polling)
        else:
            messages.error(request, 'Maaf, Anda belum memilih di Polling ini !', extra_tags='alert alert-danger alert-dismissible fade show')
            return redirect('polling_detail', id_polling)
    return redirect('polling_detail', id_polling)


def choice_edit(request, id_choice):
    choice = get_object_or_404(Choice, pk=id_choice)
    poll = get_object_or_404(Poll, pk=choice.poll.id)
    if request.user != poll.owner:
        return redirect('polling_list')
    if request.method == "POST":
        form = ChoiceEditForm(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            messages.success(request, 'berhasil merubah choice pada polling ini !', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polling_edit', choice.poll.id)
    else:
        form = ChoiceEditForm(instance=choice)
    return render(request, 'polling_app/choice_edit.html', {'form':form, 'choice':choice, 'poll':poll})


def choice_delete(request, id_polling, id_choice):
    choice = get_object_or_404(Choice, pk=id_choice)
    choice.delete()
    messages.success(request, 'berhasil menghapus choice !', extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('polling_edit', id_polling)






#
