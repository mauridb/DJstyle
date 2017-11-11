from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^test/$', views.test_crud, name='test'),
    url(r'^testskill/$', views.test_skill_crud, name='test-skill'),
    url(r'^testproject/$', views.test_project_crud, name='test-project'),

    # CRUD users
    url(r'^users/$', views.list_user, name='list-user'),
    url(r'^users/add/$', views.add_user, name='add-user'),

    # CRUD skills
    url(r'^skills/$', views.list_skill, name='list-skill'),
    url(r'^skills/add/$', views.add_skill, name='add-skill'),


    # CRUD projects
    url(r'^projects/$', views.list_project, name='list-project'),
    url(r'^projects/add/$', views.add_project, name='add-project'),


]