# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from authC.models import User


def api_projects(request):
    queryset = User.objects.all()
    data = []

    for user in queryset:
        for index, project in enumerate(user.projects):
            prj = {
                'name': project.name,
                'description': project.description,
                'likes':project.likes
            }
            data.append(prj)

    return JsonResponse(data, safe=False)