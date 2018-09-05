from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def Contact_me(request):
    return render(request, 'Contact_me.html', {})

def my_project(request):
    return render(request, 'my_project.html', {})
