from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from django.contrib import messages

# Create your views here.
def contact_me(request):
    if request.method == "POST":
        form = ContactmeForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated :
                username = request.user.username
                dari = request.user.email
            else:
                username = form.cleaned_data['username']
                dari = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            alamat = form.cleaned_data['alamat']
            pesan = form.cleaned_data['pesan']
            isi_pesan = 'first name = '+first_name+'\nlast name = '+last_name+'\nusername = '+username+'\nemail = '+dari+'\nalamat = '+alamat+'\npesan :\n'+pesan+'  '

            # send_mail( judul, isi_pesan, dari, tujuan, fail_silently=False )
            send_mail( 'dari web asfianridho.pythonanywhere.com', isi_pesan, dari, ['ridhoasfian86@gmail.com',], fail_silently=False )
            messages.success(request, 'terima kasih atas tanggapan anda !', extra_tags='alert alert-warning alert-dismissible fade show')
            return redirect('contact_me')
    else:
        form = ContactmeForm()

    return render(request, 'contactme_app/contact_me.html', {'form':form,})
