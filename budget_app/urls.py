"""budget_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('tambah_anggaran/', views.tambah_anggaran, name='tambah_anggaran'),
    path('anggaran_list/', views.anggaran_list, name='anggaran_list'),
    path('anggaran_detail/<int:id_anggaran>', views.anggaran_detail, name='anggaran_detail'),
    path('anggaran_edit/<int:id_anggaran>/submit_biaya', views.submit_biaya, name='submit_biaya'),
    path('anggaran_hapus/<int:id_anggaran>', views.anggaran_hapus, name='anggaran_hapus'),
    path('anggaran_hapus/<int:id_anggaran>/biaya_hapus/<int:id_biaya>', views.biaya_hapus, name='biaya_hapus'),
]
