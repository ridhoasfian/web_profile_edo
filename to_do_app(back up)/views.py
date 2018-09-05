from django.shortcuts import render

# Create your views here.
def to_do_index(request):
    return render(request, 'to_do_app/to_do_index.html', {})
