from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^test/$', views.test_crud, name='test'),

    # CRUD operation
    url(r'^users/$', views.list_user, name='list-user'),
    url(r'^users/add/$', views.add_user, name='add-user'),

]