# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from authC.models import User, Project, Skill


def test_crud(request):
    return render(request, 'testcrud.html')


def test_skill_crud(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'testcrudskill.html', context=context)


def list_user(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/user_list.html', context=context)


def list_skill(request):
    result = []
    users = User.objects.all()
    for user in users:
        for skill in user.skills:
            if skill not in result:
                result.append(skill)
    # print skills
    context = {
        "skills": result
    }
    return render(request, 'skills/skill_list.html', context=context)


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
        <a href="/blog/test/">test again</a>
        """)
    else:
        return HttpResponse("Not allowed..")


def add_skill(request):
    if request.method == 'POST':
        skill = Skill(name=request.POST.get("skill", None))
        user_id = request.POST.get("user", None)
        user = User.objects.get(id=user_id)
        user.update(push__skills__0=skill)
        user.reload()
        return HttpResponse("""Well Done! Skill was successfully updated..
        <a href="/blog/testskill/">test again</a>
        """)
    else:
        return HttpResponse("Not allowed..")


