"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home.views import *
from vege.views import *
urlpatterns = [
    
    path("",home,name= "home"),
    path("reciepes/",reciepes,name = "reciepes"),
    path("delete_receipe/<id>/",delete_receipe,name = "delete_receipe"),
    path("update_receipe/<id>/",update_receipe,name = "update_receipe"),
    path('about/',about,name= 'about'),
    path('contact/',contact,name='contact'),
    path('admin/', admin.site.urls),
    path("login/",login_page,name="login_page"),
    path("register/",register,name= "register"),
    
]
