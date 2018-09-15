from django.shortcuts import render, redirect
import requests
from .models import Kota
import datetime

# Create your views here.
def weather_list(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=356b2fdb14fc40881b782e048064275f'
    # kota = 'Rantau'

    kota = Kota.objects.all()

    data_cuaca = []

    for kota in kota :
        hasil = requests.get(url.format(kota)).json()
        cuaca_kota = {
            'kota':kota.nama,
            'temperature':hasil['main']['temp'],
            'deskripsi':hasil['weather'][0]['description'],
            'icon':hasil['weather'][0]['icon'],
        }
        data_cuaca.append(cuaca_kota)

    print(data_cuaca)
    return render(request, 'weather_app/weather_list.html', {'data_cuaca':data_cuaca, 'datetime':datetime.datetime.now()})
