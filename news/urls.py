from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'news'
urlpatterns =[
    path(r'', views.index, name='list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.news_detail, name='news_detail'),
]