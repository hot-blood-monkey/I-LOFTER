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


from ..models import News,Comments
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt                #用于没有token 的客服端的请求
from django.http import HttpResponse

from rest_framework import serializers                              # 序列化
from rest_framework import generics  #
from rest_framework.decorators import api_view, authentication_classes  #简单的路由装饰器
from rest_framework.authentication import TokenAuthentication       #身份的token认证
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class NewSerializer(serializers.ModelSerializer):
    """把news类序列化 ，也就是变成json"""
    class Meta:
        model = News
        fields = '__all__'
        depth = 2 


@api_view(['GET','POST'])
@authentication_classes((TokenAuthentication,))
def news_list(request):
    print(request.user)
    if request.method == "GET":
        news_list = News.objects.all()
        serializer = NewSerializer(news_list, many=True)    #序列化
        return Response(serializer.data)                    #返回序列化的数据

    elif request.method == "POST":
        
        #ModerSerializer() 含有一个默认的create（）方法
        serializer = NewSerializer(data=request.data)       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        
@api_view(['PUT','DELETE'])
@authentication_classes((TokenAuthentication,))
def news_card(request):
    print(request.data["id"])
    id = request.data["id"]
    obj = News.objects.get(id=id)
    
    if request.method == "DELETE":
        pass

    elif request.method == "PUT":
        print(request.data)
        serializer = NewSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentSerializer(serializers.ModelSerializer):
    """把评论序列化"""
    class Meta:
        model = Comments
        fields = "__all__"
        depth = 2

@api_view(["GET","POST"])
def comments_get_post(request):
    if request.method == "GET":
        comments_list = Comments.objects.order_by()
        seria_data = CommentSerializer(comments_list, many=True)
        return Response(seria_data)

    elif request.method == "POST":
        comment_name = request.data["name"]
        comment_user = User.objects.get(username=comment_name)
        request.data["name"] = comment_user.id

        # comment_news_id = request.data["news"]
        # print("传过来的newsID 的类型")
        # print(type(comment_news_id))
        # comment_news = News.objects.get(id=comment_news_id)
        # request.data["news"] = comment_news

        new_comment = CommentSerializer(data=request.data)
        if new_comment.is_valid():
            new_comment.save()
            print(type(new_comment))
            return Response(new_comment.data, status=status.HTTP_201_CREATED)
        return Response(new_comment.errors,status=status.HTTP_406_NOT_ACCEPTABLE)




class UserSerializer(serializers.ModelSerializer):
    """ 把user序列化"""
    class Meta:
        model = User
        fields = '__all__'
        depth = 2


@api_view(["GET","POST"])
# @authentication_classes((TokenAuthentication,))
def users_list(request):
    print(request.auth)
    if request.method == "GET":
        users_list = User.objects.order_by()
        serializer = UserSerializer(users_list,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        buff = request.data                                             #http 的数据包（请求）

        #buff=JSONParser().parse(buff)
        user = authenticate(username=buff['username'],
                                password=buff['password'])
         # 使用 authenticate来认证传输过来的username 和password 是否有效   
        

        if user is not None:
            print("-----------------i am ok------------------------------")
            if user.is_active:
                # token = Token.objects.get_or_create(user=user)   
                serializer = UserSerializer(user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':'用户没有激活'},status=status.HTTP_400_BAD_REQUEST)
        else:
            print("----------------------------------user is None ----------------")
            return Response({'msg':'没有用户'},status=status.HTTP_400_BAD_REQUEST)


                               
        # created_user = UserSerializer(data=request.data)
        # if created_user.is_valid():
        #     created_user.save()
        #     return Response(created_user.data, status=status.HTTP_201_CREATED)
        # return Response(created_user.errors,status=status.HTTP_400_BAD_REQUEST)