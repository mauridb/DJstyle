# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from mongoengine import DoesNotExist
from termcolor import colored as c

from authC.models import User, Project


def singUp(request):
    if request.method == 'POST':

        user_id = User.objects.all().count() + 1  # TODO: better logic user.last.user_id + 1
        # prj1 = Project(name=request.POST.get("prjname", None))
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        password = request.POST.get("password", None)
        confirm_password = request.POST.get("confirm_password", None)
        email = request.POST.get("sign_email", None)
        role = request.POST.get("role", 'user')

        if password != confirm_password:
            return HttpResponse('different password')

        # Logs sign up
        print c('USER REGISTERED INFO:', 'blue')
        print c('\tUSER FIRST NAME: %s' % first_name, 'green')
        print c('\tUSER LAST NAME: %s' % last_name, 'green')
        print c('\tUSER EMAIL: %s' % email, 'green')
        print c('\tUSER ROLE: %s' % role, 'green')
        print c('\tUSER PASSWORD: ******', 'green')

        user = User(user_id=user_id, first_name=first_name, last_name=last_name, role=role, email=email,
                    password=password)
        # user.projects.append(prj1)
        user.save()
        return HttpResponse("""Well Done! Check your email to confirm..
                <a href="/">Homepage</a>
                """)
    else:
        return render(request, 'testcrud.html')


def signIn(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        email = request.POST.get("login_email", None)
        password = request.POST.get("password", None)

        # Logs sign in
        print c('USER LOGGED INFO:', 'red')
        print c('\tUSER FIRST NAME: %s' % first_name, 'yellow')
        print c('\tUSER LAST NAME: %s' % last_name, 'yellow')
        print c('\tUSER EMAIL: %s' % email, 'yellow')
        print c('\tUSER PASSWORD: ******', 'yellow')

        try:
            user = User.objects.get(first_name=first_name, last_name=last_name, email=email, password=password)
            # print user.user_id
        except DoesNotExist:
            return HttpResponse("""Error, user with this credentials does not exist! <b>Please try again!</b>""")

        return HttpResponse("Login successfully! Welcome back, %s" % user.first_name)

    else:
        return HttpResponse(""" Not allowed!""")


def request_membership(request):
    if request.method == 'POST':
        # send email
        email_address = request.POST.get('memb_email', None)
        print email_address
        mail = EmailMessage(
            'REQUEST MEMBERSHIP',
            'Hi, you are welcome to the dj platfrom.. Enjoy! \nby Mauridb',
            to=[email_address]
        )
        mail.send()
        return HttpResponse('Great, mail succesfully sent..')
    else:
        return HttpResponse("Not allowed!")


