from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.HomeTemplateView.as_view(), name='home'),
    url(r'^paneladmin$', views.AdminListView.as_view(), name='admin'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.newUser, name='register'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^blog/(?P<pk>[0-9]+)/delete/$', views.PostDeleteView.as_view(), name='delete'),
    url(r'^blog/(?P<pk>[0-9]+)/update/$', views.PostUpdateView.as_view(), name='update'),
]
