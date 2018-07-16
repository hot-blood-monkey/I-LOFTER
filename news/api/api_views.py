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
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  #用于没有token 的客服端的请求
@csrf_exempt
def news_list(request):
    return render(request, 'api/news_list.html', {})

@csrf_exempt
def account(request):    
    return render(request, 'api/account.html',{})
    
@csrf_exempt
def login(request):
    return render(request, 'api/login.html', {})



