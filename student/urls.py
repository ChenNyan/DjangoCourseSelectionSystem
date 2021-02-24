"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('tea1/', views.tea1, name='tea1'),
    path('newcou/', views.newcou, name='newcou'),
    path('stu1/', views.stu1, name='stu1'),
    path('getcou/', views.getcou, name='getcou'),
    path('score/', views.score, name='score'),
    url(r'^score_stu/(?P<pk>[0-9]+)/$', views.score_stu, name='score_stu'),
    url(r'^scoreinfo/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', views.scoreinfo, name='scoreinfo'),
    url(r'^setsco/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', views.setsco, name='setsco'),
    path('stusco/',views.stusco, name='stusco'),
    url(r'^stuscoinfo/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', views.stuscoinfo, name='stuscoinfo'),
]
