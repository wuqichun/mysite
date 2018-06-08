#!/usr/bin/python
#coding=utf-8
from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = "delad"

urlpatterns=[
    path('', views.index, name='index'),
    path('', views.edit, name='edit'),
]