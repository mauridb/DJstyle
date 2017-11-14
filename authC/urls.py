from django.conf.urls import url

from authC import views

urlpatterns = [

    # Sign Up registration
    url(r'^signUp/$', views.singUp, name='sign-up'),

    # Sign In log in the platform
    url(r'^signIn/$', views.signIn, name='sign-in'),

    # Send email request membership
    url(r'^requestMembership/$', views.request_membership, name='request-membership'),

]