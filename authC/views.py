# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import User, Project


def test_crud(request):
    return render(request, 'testcrud.html')


def add_user(request):
    if request.method == 'POST':
        prj1 = Project(name=request.POST.get("prjname", None))
        prj2 = Project(name=request.POST.get("prjname", None))
        user = User(first_name='Maurizio', last_name='Bussi', role='Admin', email='mauriziocontatto@gmail.com')
        user.projects.append(prj1)
        user.projects.append(prj2)
        user.save()
        return HttpResponse("Well Done! Check your email to confirm..")
    else:
        return HttpResponse("Not allowed..")
