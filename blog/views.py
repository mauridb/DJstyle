# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from authC.models import User, Project


def test_crud(request):
    return render(request, 'testcrud.html')


def list_user(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/user_list.html', context=context)


def add_user(request):
    if request.method == 'POST':
        prj1 = Project(name=request.POST.get("prjname", None))
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        password = request.POST.get("pwd", None)
        email = request.POST.get("email", None)
        role = request.POST.get("role", None)
        user = User(first_name=first_name, last_name=last_name, role=role, email=email, password=password)
        user.projects.append(prj1)
        user.save()
        return HttpResponse("""Well Done! Check your email to confirm..
        <a href="/authC/test/">test again</a>
        """)
    else:
        return HttpResponse("Not allowed..")
