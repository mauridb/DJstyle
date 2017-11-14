from django.conf.urls import url

from authC import views

urlpatterns = [

    # Sign Up registration
    url(r'^signUp/$', views.singUp, name='sign-up'),

]