"""polling_app URL Configuration

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
    path('polling_list/', views.polling_list, name='polling_list'),
    path('polling_tambah/', views.polling_tambah, name='polling_tambah'),
    path('polling_detail/<int:id_polling>/', views.polling_detail, name='polling_detail'),
    path('polling_hapus/<int:id_polling>/', views.polling_hapus, name='polling_hapus'),
    path('polling_edit/<int:id_polling>/', views.polling_edit, name='polling_edit'),
    path('polling_edit/<int:id_polling>/choice_tambah/', views.choice_tambah, name='choice_tambah'),
    path('poll_vote/<int:id_polling>/', views.poll_vote, name='poll_vote'),
    path('choice_edit/<int:id_choice>/', views.choice_edit, name='choice_edit'),
    path('polling_edit/<int:id_polling>/choice_delete/<int:id_choice>/', views.choice_delete, name='choice_delete'),
]
