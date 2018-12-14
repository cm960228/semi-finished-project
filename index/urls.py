from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index_views),
    url(r'^index/$',index_views),
    url(r'^register/$',register_views),
    url(r'^login/$',login_views),
    url(r'^check_login/$',check_login_views),
    url(r'^logout',logout_views),
    url(r'^check_register/$',check_register_views),
    url(r'^info/$', info_views),
    url(r'^release/$', release_views),
    url(r'^list/$',list_views),
]