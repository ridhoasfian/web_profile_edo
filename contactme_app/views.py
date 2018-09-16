from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import *

# Create your views here.
def contact_me(request):

    subject = 'Thank you for registering to our site'  # judul email
    message = ' it  means a world to us '              # isi email
    email_from = settings.EMAIL_HOST_USER              # dari
    recipient_list = ['gumiritibu@poly-swarm.com',]    # kepada
    # send_mail( subject, message, email_from, recipient_list, fail_silently=False )

    if request.method == "POST":
        form = ContactmeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['lastName']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            alamat = form.cleaned_data['alamat']
            pesan = form.cleaned_data['pesan']

            send_mail( 'dari web asfianridho.pythonanywhere.com', pesan, email, ['ridhoasfian86@gmail.com',], fail_silently=False )
            return redirect('contact_me')
    else:
        form = ContactmeForm()

    return render(request, 'contactme_app/contact_me.html', {'form':form,})
