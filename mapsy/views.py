# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from termcolor import colored

from mapsy.models import *
import csv


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


def index(request):
    print request
    context = {
        'message':'puppuuuuuu'
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
                print colored("NAME: "+point.name, 'blue')
            print colored("IMPORT COMPLETED!!", 'green')

        return HttpResponse("IMPORT OK!!")
    else:
        return HttpResponse("NO INSERT ALLOW!!")






