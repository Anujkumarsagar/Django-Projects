"""
URL configuration for firstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),


    #modularize the routes /auth / ......
    #like , /order/ ...... , admin/ .......
    path('subApp/', include('subApp.urls') , name="sub-app")

    # in this case we are modularize the routes of another seprate app 'subApp' 
    # when user hits the /subApp/ .... then all routes are running of the same subApp that will be written in subApp.urls.py file
]
