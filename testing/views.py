from django.shortcuts import render
from .forms import TestUploadForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = TestUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('berhasil')
    else:
        form = TestUploadForm()
    return render(request, 'testing/testing.html', {'form':form})
