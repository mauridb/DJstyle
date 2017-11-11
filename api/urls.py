from django.conf.urls import url

from . import views


urlpatterns = [

    # APIrest v1
    # url(r'^v1/$', views.api_root, name='api-root'),
    url(r'^v1/projects$', views.api_projects, name='api-projects'),

]