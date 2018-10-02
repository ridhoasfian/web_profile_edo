from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def my_project(request):
    return render(request, 'my_project.html', {})

def about(request):
    return render(request, 'about.html', {})

def test(request):
    return render(request, 'test.html', {})
