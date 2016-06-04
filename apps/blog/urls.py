from django.conf.urls import url
from django.contrib import admin
from . import views
from .models import Post

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
    url(r'^new/$', views.NewPostView.as_view(), name='new_post'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
]
