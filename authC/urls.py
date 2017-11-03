from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^test/', views.test_crud, name='test'),

    # users CRUD
    url(r'^users/add', views.add_user, name='add-user'),

]