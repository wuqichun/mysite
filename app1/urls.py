#!/usr/bin/python
#coding=utf-8
from django.urls import path, re_path
from django.conf.urls import url
from app1 import views
from django.contrib import admin

app_name = "app1"

urlpatterns=[
    path('index/', views.index, name='index'),
    path('get_form/', views.get_form, name = 'get_form'),
    path('uploadfile', views.uploadfile, name="uploadfile"),
    path('echo', views.echo, name='echo'),
]
