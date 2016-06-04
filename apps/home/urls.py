from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^paneladmin$', views.admin, name='admin'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.newUser, name='register'),
    url(r'^logout/$', views.log_out, name='logout'),
]
