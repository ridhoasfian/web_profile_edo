"""schedule URL Configuration

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
    path('testing/', views.testing, name='testing'),
    path('schedule_list/', views.schedule_list, name='schedule_list'),
    path('schedule_tambah/', views.schedule_tambah, name='schedule_tambah'),
    path('schedule_detail/<int:id_schedule>/', views.schedule_detail, name='schedule_detail'),
    path('schedule_delete/<int:id_schedule>/', views.schedule_delete, name='schedule_delete'),
]
