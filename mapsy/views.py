# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from termcolor import colored

from djmauridb.settings import API_KEY
from mapsy.models import *

import csv


DEV_MANAGE_SIZE_DB_VIEW = 30

def welcome(request):
    context = {
        'message': 'WELCOME'
    }
    return HttpResponse("welcome page")


def index(request):
    queryset = Point.objects[:DEV_MANAGE_SIZE_DB_VIEW]
    data = [{'name': elem.name, 'lat': elem.lat, 'lng': elem.lng} for elem in queryset]
    context = {
        'google_key': API_KEY,
        'points': data,
    }
    return render(request, 'index.html', context)


def import_csv(request):
    print(request.method)
    print('CACCA')
    if request.method == 'POST':
        with open('data/dataset.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['POINT'], row['LAT'], row['LNG'])
                point = Point(name=row['POINT'], lat=float(row['LAT']), lng=float(row['LNG']))
                point.save()
                print colored("NAME: " + point.name, 'blue')
            print colored("IMPORT COMPLETED!!", 'green')

        return HttpResponse("IMPORT OK!!")
    else:
        return HttpResponse("NO INSERT ALLOW!!")


def mapsy(request):
    queryset = Point.objects[:DEV_MANAGE_SIZE_DB_VIEW]
    data = [{'name': elem.name, 'lat': elem.lat, 'lng': elem.lng} for elem in queryset]
    return JsonResponse(data, safe=False)


# Mongo test views
def userView(request):
    user = User(email='test@title.com', first_name='test content')
    user.save()
    print(user.first_name, user.email)
    return HttpResponse("SAVED USER")


def commentView(request):
    node = Node(lat=9.7866, lng=45.56654, name='node1')
    node.save()
    print (node.lat, node.lng, node.name)
    return HttpResponse("SAVED TextPost")
