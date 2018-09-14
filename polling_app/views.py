from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *
import datetime

# Create your views here.
def polling_list(request):
    poll = Poll.objects.all()
    return render(request, 'polling_app/polling_list.html', {'poll':poll})

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
    return render(request, 'polling_app/polling_detail.html', {'poll':poll})


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
        pass
        # form = ChoiceTambahForm(request.POST)
        # if form.is_valid():
        #
    else:
        form = ChoiceTambahForm()
    return render(request, 'polling_app/choice_tambah.html', {'form':form, 'poll':poll})






#
