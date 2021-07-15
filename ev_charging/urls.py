"""ev_charging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url ,include

from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index ,name='index' ),
    path( 'register' , views.register , name='register'),
    path('login' , views.login , name='login'),
    path('register_back' , views.register_back , name='register_back'),
    #path( 'login_back' , views.login_back , name='login_back'),
    path('home/<int:id>/' , views.home , name='home'),  #grtting parameters from 'return redirect('home',user)'   
    path('<int:id>/', views.charging ,name='charging'), #getting parameter from 'charging/{{user}}'
    path('<int:id>/specifies/' , views.about_us ,name='about_us'),

    #manager and admin 
    path('manager', views.manager, name="manager"),
    path('manager_page', views.manager_page, name="manager_page"),
    path('acharging', views.acharging, name="acharging"),
    path('allow_user', views.allow_user, name="allow_user"),
    path('activate', views.activate, name="activate"),
    path('desable', views.desable, name="desable"),

    path('ev_admin', views.ev_admin, name="ev_admin"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('addman', views.addman, name="addman"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('addslots', views.addslots, name="addslots"),
    path('admin_activate', views.admin_activate, name="admin_activate"),
    path('admin_desable', views.admin_desable, name="admin_desable"),
]
