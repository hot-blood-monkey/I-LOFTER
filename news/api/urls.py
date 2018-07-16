#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/4/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.urls import path
from django.conf.urls import url,include
from . import api_views,api
from rest_framework.authtoken import views


urlpatterns = [
    path('news_list/',api.news_list, name='news_list'),
    path('full/news_list/', api_views.news_list, name='news_list'),

    path(r'token-auth', views.obtain_auth_token),
    path('users_list/', api.users_list, name='users_list'),
    path('full/login/', api_views.login, name="login"),#


    path('news_card/',api.news_card, name="news_card"),
    url(r'news_card/(?P<id>\d+)$', api.news_card, name="news_card"),
    path('comments/',api.comments_get_post,name="comments"),



]

from rest_framework.authtoken import views
urlpatterns += [
    path(r'token-auth', views.obtain_auth_token)
]
