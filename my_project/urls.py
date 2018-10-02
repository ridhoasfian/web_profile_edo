"""my_project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),

    path('contactme_app/', include('contactme_app.urls')),
    path('artikel_app/', include('artikel_app.urls')),

    path('my_project/', views.my_project, name='my_project'),
    path('my_project/to_do_app/', include('to_do_app.urls')),
    path('my_project/budget_app/', include('budget_app.urls')),
    path('my_project/polling_app/', include('polling_app.urls')),
    path('my_project/weather_app/', include('weather_app.urls')),
    path('my_project/schedule_app/', include('schedule_app.urls')),

    path('my_project/testing/', include('testing.urls')),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
