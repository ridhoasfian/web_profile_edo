"""artikel_app URL Configuration

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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('artikel_list/', views.artikel_list, name='artikel_list'),
    path('artikel_detail/<int:id_artikel>/', views.artikel_detail, name='artikel_detail'),
    path('artikel_tambah/', views.artikel_tambah, name='artikel_tambah'),
    path('artikel_edit/<int:id_artikel>/', views.artikel_edit, name='artikel_edit'),
    path('artikel_delete/<int:id_artikel>/', views.artikel_delete, name='artikel_delete'),

    path('kategori_list/', views.kategori_list, name='kategori_list'),
    # path('kategori_tambah/', views.kategori_tambah, name='kategori_tambah'),
    path('kategori_edit/<int:id_kategori>/', views.kategori_edit, name='kategori_edit'),
    path('kategori_delete/<int:id_kategori>/', views.kategori_delete, name='kategori_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











#
