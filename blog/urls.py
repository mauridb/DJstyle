from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^test/$', views.test_crud, name='test'),
    url(r'^testskill/$', views.test_skill_crud, name='test-skill'),

    # CRUD users
    url(r'^users/$', views.list_user, name='list-user'),
    url(r'^users/add/$', views.add_user, name='add-user'),

    # CRUD skills
    url(r'^skills/$', views.list_skill, name='list-skill'),
    url(r'^skills/add/$', views.add_skill, name='add-skill'),

]