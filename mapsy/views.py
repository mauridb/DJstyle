# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from mapsy.models import *


def userView(request):
    user = User(email='test@title.com', first_name='test content')
    user.save()
    print user.first_name, user.email
    return HttpResponse("SAVED USER")


def commentView(request):
    node = Node(lat=9.7866, lng=45.56654, name='node1')
    node.save()
    print node.lat, node.lng, node.name
    return HttpResponse("SAVED TextPost")


