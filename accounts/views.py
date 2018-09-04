from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUserForm, RegisterUserForm
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else :
                return render(request, 'accounts/login_user.html', {'form':form, 'akun_salah':'username atau password anda salah !'})
    else:
        form = LoginUserForm()

    return render(request, 'accounts/login_user.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            user = User.objects.create_user(username=username, email=email, password=password_confirm)
            messages.success(request, 'Terima kasih sudah mendaftar, {} !!!'.format(user.username))
            return redirect('login_user')
    else :
        form = RegisterUserForm()
    return render(request, 'accounts/register_user.html', {'form':form})










#
