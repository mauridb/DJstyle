"""djmauridb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from mapsy import views

urlpatterns = [

    url(r'^$', views.welcome, name='homepage'),

    # ROUTE: test data with mongo
    url(r'^data/', views.mapsy, name='data'),

    # ROUTE: mapsy app
    url(r'^mapsy/', include('mapsy.urls')),




    # ROUTE: test insert in mongodb
    url(r'^users/add/', views.userView, name='user-add'),
    url(r'^nodes/add/', views.commentView, name='comment-add')
]
