#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Filename: urls.py
@version: v1.0 
@author: WeWe
@Time: 2019/5/22 15:04
@Last Modified time: 2019/5/22 15:04
@Explain: This file is for ...
"""

from django.urls import path
from bookTest.views import *

urlpatterns = [
    path('', index),
    path('<int:year>/<int:month>/<int:day>/', detail, name="detail"),
    path('getTest1/', get_test1),
    path('getTest2/', get_test2),
    path('getTest3/', get_test3),

    path('postTest1/', post_test1),
    path('postTest2/', post_test2),

    path('cookieTest/', cookie_test),

    path('redirectTest1', redirect_test1),
    path('redirectTest2', redirect_test2),
]
