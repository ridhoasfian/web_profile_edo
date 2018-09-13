from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ToDoForm
from django.views.decorators.http import require_POST

# Create your views here.
def to_do_app(request):
    toDoForm = ToDoForm()
    toDoList = ToDo.objects.order_by('id')
    return render(request, 'to_do/to_do.html', {'toDoList':toDoList, 'toDoForm':toDoForm} )

@require_POST
def tambahToDo(request):
    form = ToDoForm(request.POST)

    if form.is_valid():
        newToDo = ToDo(text=form.cleaned_data['text'])
        newToDo.save()

    return redirect('to_do_app')


def completeToDo(request, toDoID):
    toDo = ToDo.objects.get(pk=toDoID)
    toDo.complete = True
    toDo.save()

    return redirect('to_do_app')


def deleteComplete(request):
    ToDo.objects.filter(complete__exact=True).delete()

    return redirect('to_do_app')


def deleteAll(request):
    ToDo.objects.all().delete()

    return redirect('to_do_app')











#
