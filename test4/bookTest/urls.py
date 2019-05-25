#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: urls.py
@version: v1.0 
@author: WeWe 
@time: 2019/05/24 14:18
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""
from django.urls import path
from bookTest import views

urlpatterns = [
    path('', views.index, name="index"),
    path('show', views.show, name="show"),
    path('index2', views.index2, name="index2"),
]
